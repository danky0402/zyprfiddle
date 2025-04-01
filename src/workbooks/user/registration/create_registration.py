
from src.services.zypr.user import User
from src.services.zypr.utility import Utility
from src.helpers.local_message.message import Message

#   1. check zypr is available

Message.Clear()

utility  = Utility()
status_code = utility.HealthCheck()
if status_code != 200:
    Message.Post( f"Zypr health check failed with status code: {str(status_code)}")
    quit()


user = User()
response = user.NewUserRegistration()
