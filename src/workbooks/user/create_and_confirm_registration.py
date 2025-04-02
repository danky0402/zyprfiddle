import json

from src.services.zypr.utility import Utility
from src.helpers.local_message.message import Message

from src.services.zypr.user import User


#   1. check zypr is available

Message.Clear()

utility  = Utility()
status_code = utility.HealthCheck()
if status_code != 200:
    Message.Post( f"Zypr health check failed with status code: {str(status_code)}")
    quit()


#   2. register
firstName = "Dan"
emailAddress = "dan@ravelloanalytics.com"
organization = "Ravello Analytics"

user = User()
response = user.NewUserRegistration(firstName, emailAddress, organization)
Message.Post(response.text)


#   3. confirm using activation code received via email (uncomment the code below)

activationCode = "86399754"


#   code below is commented out to stop script because it requires the activation code to continue

# response = user.ConfirmNewUserRegistration(activationCode, emailAddress)
#                                                                             #   response is the requests library's response object
# json_data = response.json()                                                 #   requests library json() method attempts to decode the "content" property of response         
# formatted_json = json.dumps(json_data, indent=4)
# print(formatted_json)
# Message.Post(formatted_json)

 
