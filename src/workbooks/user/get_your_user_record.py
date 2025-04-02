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


#   2. get user record - relies on api-key in secrets
user = User()
response = user.GetUserInfo() 

#   requests library json() method attempts to decode the "content" property of response 
json_data = response.json()                                                        
formatted_json = json.dumps(json_data, indent=4)
Message.Post(formatted_json)
