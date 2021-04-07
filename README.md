# GVE Devnet DNA Center Client Monitoring

## Contacts
* Eda Akturk

## Solution Components
*  Python 3.8
*  Cisco DNA Center 
    - [API Documentation](https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-1-2-x-api-overview)
* Slack 
    - [API Documentation](https://api.slack.com/)

## Solution Overview
The app will monitor a wireless user client device with a specified mac address.

It will check the following parameter(s) to evaluate the network experience:
* client health score

If the parameter(s) do not meet the predefined threshold values the app will send a bot message from slack. 


## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 

*DNA Center*
1. Add the DNA Center Lab credentials in env_var.py
```
DNAC_URL = " "
DNAC_USER = " "
DNAC_PASS = " "
```

*Slack*

2. Create a Slack App from https://api.slack.com/. You need to specify a name for your app and add to your space. 
    
3. Add permissions to your App. From the OAuth scope select "chatWrite" permissions so that your Bot can have the rights to write a message in a channel.
    
4. Install App to Workspace. This will automatically give a token for your App to be used. Add your Slack App token to env_var.py
```
SLACK_TOKEN = " "
```

5. In your slack space connect your Slack Bot to the channel that you want to have it in. 

*DNA Center VIP Client*

6. Add the MAC Address for VIP client in env_var.py
```
CLIENT_MAC = " "
```
*Network Metrics*

7. Set the network threshold value in env_var.py
```
HEALTH_LOW = " "
```


## Usage

1. Run the script 
```
python client_monitoring
```

Once the network experience for the client falls under the pre-defined thresholds a Slack notification will be sent to 
the admin with the client information. 

# Screenshots
![/IMAGES/slack_bot.PNG](/IMAGES/slack_bot.PNG)


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
