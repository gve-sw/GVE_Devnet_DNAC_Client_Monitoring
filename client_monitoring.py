# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Eda Akturk <eakturk@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import time

import urllib3
from urllib3.exceptions import InsecureRequestWarning

from requests.auth import HTTPBasicAuth

from env_var import *
from dnacentersdk import DNACenterAPI

import slack

urllib3.disable_warnings(InsecureRequestWarning)

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)

MAX_ALERT = 2


def send_slack_message(channel_name, message):
    """
    This function will send a  message {message} to the Slack channel with the {channel_name}
    :param channel_name: slack channel name
    :param message: slack message
    :return: none
    """
    client = slack.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=channel_name, text=message)


def client_health_check(alert, client_health):
    """
    This function will check if the client health score {client_health} is above the predefined threshold
    :param alert: parameter for alert to check if alert needs to be sent or not
    :param client_health: client health score
    :return: alert
    """
    if client_health <= HEALTH_LOW:
        alert = True
        print(f"**client Health too low: {client_health}, send bot message**")
    return alert


def main():
    print('**DNA Center client to be monitored: **', CLIENT_MAC)

    # alerts will be send until the alert counter reaches the max alert count
    alert_count = 0

    while alert_count < MAX_ALERT:

        alert = False

        dna_center = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, verify=False)
        client_info = dna_center.clients.get_client_detail(mac_address=CLIENT_MAC)

        # parse the client health score, ap name, snr, location
        try:
            health_score = client_info['detail']['healthScore']
            for score in health_score:
                if score['healthType'] == 'OVERALL':
                    client_health = score['score']
            ap_name = client_info['detail']['clientConnection']
            snr = float(client_info['detail']['snr'])
            location = client_info['detail']['location']
        except:
            print('**client not in DNA Center**')

        alert = client_health_check(alert, client_health)

        if alert:
            print("**sending bot message**")

            message = f"DNA Center VIP Client Alert:\n" \
                      f" Please review the information for the VIP Client-{CLIENT_MAC}:\n" \
                      f"Location: {location}\n" \
                      f"AP: {ap_name}\n" \
                      f"Health: {client_health}\n" \
                      f"SNR: {snr}"
            
            # send message from slack bot to the specified space: #bot-project
            send_slack_message('#bot-project', message)

            alert_count += 1
            time.sleep(5)


if __name__ == '__main__':
    main()
