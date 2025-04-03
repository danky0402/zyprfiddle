#from urllib.parse import urlparse, urlunparse, urljoin, quote
import json, os, datetime


from src.helpers.local_message.message import Message
from src.helpers.deserializers.deserializer import Deserialize
from src.helpers.misc.file_operation import File
from src.services.zypr.health_check import HealthCheck
from src.services.zypr.simulation import Simulation

# from src.helpers.zypr_classes.scenario.scenario import Scenario

Message.Clear()

# file_path = os.path.join(str(os.getcwd()), "src", "test", "content", "save_file_test.json")
# _content = {"Item" : "value" }
# File.Save(file_path, json.dumps(_content))

# local_filepath = "src\\test\\content\\output_scenarios\\partials\\scenario_first_response_obj.json"
# filepath = os.path.join(os.getcwd(), local_filepath)
# scenario_response_dict = File.Read('d', filepath)

# scenario = Deserialize.Scenario(scenario_response_dict)

# _sorted = sorted(scenario.SimulationStates, key=lambda event: event.StatusNbr)
# for state in _sorted:
#         Message.Post(f"Status Nbr:  {str(state.StatusNbr)} \n"
#                     f"Message:  {str(state.Message)} \n"
#                     f"Timestamp:  {str(state.StatusTimestamp)} \n"
#                     )

# _sorted = sorted(scenario.SimulationStates, key=lambda event: event.StatusTimestamp, reverse=True)[0]
# state = _sorted[0]   
# Message.Post(f"Status Nbr:  {str(state.StatusNbr)} \n"
#                 f"Message:  {str(state.Message)} \n"
#                 f"Timestamp:  {str(state.StatusTimestamp)} \n"
#             )
# scenarioId = "da.xkauzkkt3n7dhnknwjhjh"
# simulation = Simulation()
# record = simulation.GetScenarioRecord(scenarioId)

# Message.Post(str(record.Progress))

# _t = { "ZyprApiKey": "Z.1G9sJ8am7qmT4xSKDvgQOYtPDjIJvn0Pl6z"}
# print(type(_t))
# print("Key: " + str(_t["ZyprApiKey"]))

Message.Clear()

hc = HealthCheck()
status_code = hc.Get()
if status_code != 200:
    Message.Post( f"Zypr health check failed with status code: {str(status_code)}")



read_local_filepath = "src\\test\\content\\input_models\\neutral.json"
filepath = os.path.join(os.getcwd(), read_local_filepath)
poolModel = File.Read('j', filepath, False, "Read pool model neutral.json")


simulation = Simulation()
response = simulation.Execute(poolModel)    # this is the requests library response obj

scenario_dict = json.loads(response.text)   # get the zypr response object (json) in text property

if int(scenario_dict["StatusNbr"]) > 7:                               # use python json library to serialize to a python dictionary (key-value pair)
    # did not sucessfully complete, so stop
    quit()


ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")  # create file timestamp value
sid = str(scenario_dict["Id"])[:7]                          # use first 7 digits of scenario id

write_local_filepath = f"src\\test\\content\\output_scenarios\\completed\\neutral_{ts}_{sid}.json"
filepath = os.path.join(os.getcwd(), write_local_filepath)

File.Save(filepath, str(response.text)) 


Message.Post(str(scenario_dict["Id"]))
scenario_obj = Deserialize.Scenario(scenario_dict)
Message.Post(str(scenario_obj.Id))


Message.Post("End")




# apikey = "mykey"
# base_url = "https://zypr.app"
# relative_url= f"/v1/simulations"
# tag = "optum"
# if tag is not None or tag is not "":
#     relative_url = f"/v1/simulations?tag={tag}"

# headers = {"Content-Type": "application/json"}, {"x-api-key": f"{apikey}" }

# headers = {"Content-Type": "application/json"},{"x-api-key": f"{apikey}" }
# args = "f{ 'tag'={tag}}"
# url = urljoin(base_url, relative_url)

# filepath = "content\\secrets\\zypr\\secrets.json"


# json_content = File.Read(filepath, True, False, False, "Read secrets key")
# Message.Post(str(type(json_content)))
# Message.Post(str(json_content))


# filepath = "src\\test\\content\\scenario.json"
# json_content = File.Read(filepath, True, False, False, "Read Scenario JSON file")
# json_content = File.Read(filepath, True, False, False)
# # print(json_content)
# scenario = Deserialize.Scenario(json_content)
# Message.Post(scenario.Id)


# file_path = os.path.join(str(os.getcwd()), "src", "test", "content", "scenario.json")
# if os.path.exists(file_path):
#     with open(file_path, 'r') as file:
#             dict = json.load(file)
#             scenario = Deserialize.Scenario(dict)
            
#             Message.Post("NoSolutionGraphs: " + str(scenario.NoSolutionGraphs))
#             Message.Post("Errors: " + str(scenario.Errors))
#             Message.Post("Transaction count: " + str(scenario.Progress.TransactionCount))
#             Message.Post("Email Results: " + str(scenario.Settings.EmailResults))
#         #    

