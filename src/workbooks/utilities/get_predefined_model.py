import json, os

from src.services.zypr.utility import Utility
from src.helpers.local_message.message import Message
from src.helpers.misc.file_operation import File
from src.services.zypr.user import User


#   1. check zypr is available

 
Message.Clear()

utility  = Utility()
status_code = utility.HealthCheck()
if status_code != 200:
    Message.Post( f"Zypr health check failed with status code: {str(status_code)}")
    quit()


#   2. set starter model code and version
poolModelCode = "U01"
version = "1.0"


#   3. Fetch start model
response = utility.GetStarterPoolModel(poolModelCode, version)
                                                                            #   
#   response is the requests library's response object 
#   requests library json() method attempts to decode the "content" property of response         

json_string_data = response.json()                                                 
formatted_json = json.dumps(json_string_data, indent=4)     # formatting to human readable format
Message.Post(formatted_json)

#   4. Save 
write_local_filepath = f"content\\input_models\\starter_models\\{poolModelCode}_{version}.json" 
filepath = os.path.join(os.getcwd(), write_local_filepath)
File.Save(filepath, str(formatted_json)) 

Message.Post("End")