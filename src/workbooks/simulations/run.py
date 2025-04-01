import json, os, datetime

from src.helpers.local_message.message import Message
from src.helpers.deserializers.deserializer import Deserialize
from src.helpers.file_operations.file_operation import File
from src.services.zypr.health_check import HealthCheck
from src.services.zypr.simulation import Simulation



Message.Clear()


#   1. check zypr is available
hc = HealthCheck()
status_code = hc.Get()
if int(status_code) != 200:                                                                             #  explicitly cast status_code to an integer type for comparison
    Message.Post( f"Zypr health check failed with status code: {str(status_code)}")
    quit()


#   2. enter the location of the pool model to run a simulation
read_local_filepath = "src\\test\\content\\input_models\\neutral.json"                                  #   fetch from your preferred folder structure
filepath = os.path.join(os.getcwd(), read_local_filepath)                                               #   getcwd() method is get current working directory 
poolModel = File.Read('j', filepath, False, "Read pool model neutral.json")                             #   which is the root folder ZyprFiddle


#   3. define a new Simulation object, execute and receive the response object  
simulation = Simulation()
response = simulation.Execute(poolModel)    # this is the requests library response obj


#   4. check response of http request (not zypr response status)
Message.Post(str(f"Http status code:  {response.status_code}")) 
if int(response.status_code) != 200:
    quit()


#   5. convert response object from JSON to python dictionary and check zypr response status
scenario_dict = json.loads(response.text)                                                               # this deserializes JSON into python dictionary
if int(scenario_dict["StatusNbr"]) > 7:                                                                 # check the response status using dictionary key (a zypr property name) 
    # did not sucessfully complete, so stop
    quit()


#   6. creates file name with this structure:  "name"_"timestamp"_"scenario id (partial)"             
ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")                                              # create file timestamp value
sid = str(scenario_dict["Id"])[:7]                                                                      # use first 7 digits of scenario id
write_local_filepath = f"src\\test\\content\\output_scenarios\\completed\\neutral_{ts}_{sid}.json"      # place into your preferred folder structure
filepath = os.path.join(os.getcwd(), write_local_filepath)
File.Save(filepath, str(response.text)) 
Message.Post(str(scenario_dict["Id"]))


#   7. optional
#       if you need to further work with the scenario response, it easier to work with a scenario object 
#       below is how to deserialize scenario dictionary into the custom Scenario object (see src.helpers/zypr_classes/scenario)
#       this provides access to intellisense 

scenario = Deserialize.Scenario(scenario_dict)
Message.Post(str(scenario.Id))


#   8. end message to report script is complete
Message.Post("End")
