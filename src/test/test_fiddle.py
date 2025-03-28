from urllib.parse import urlparse, urlunparse, urljoin, quote
import json, os


from src.utilities.helpers.local_message.message import Message
from src.utilities.helpers.deserializers.deserializer import Deserialize
from src.utilities.helpers.file_operations.file_operation import File
from src.services.zypr.health_check import HealthCheck
from src.services.zypr.simulation import Simulation

# from src.utilities.zypr_classes.scenario.scenario import Scenario

Message.Clear()

# file_path = os.path.join(str(os.getcwd()), "src", "test", "content", "save_file_test.json")
# _content = {"Item" : "value" }
# File.Save(file_path, json.dumps(_content))

# local_filepath = "src\\test\\content\\output_scenarios\\partials\\scenario_first_response_obj.json"
# filepath = os.path.join(os.getcwd(), local_filepath)
# scenario_response_dict = File.Read('d', filepath)

# scenario = Deserialize.Scenario(scenario_response_dict)



_r = HealthCheck()
_response = _r.Get()

scenarioId = "da.xkauzkkt3n7dhnknwjhjh"
simulation = Simulation()
record = simulation.GetScenarioRecord(scenarioId)

Message.Post(str(record.Progress))

# _t = { "ZyprApiKey": "Z.1G9sJ8am7qmT4xSKDvgQOYtPDjIJvn0Pl6z"}
# print(type(_t))
# print("Key: " + str(_t["ZyprApiKey"]))

local_filepath = "src\\test\\content\\input_models\\neutral.json"
filepath = os.path.join(os.getcwd(), local_filepath)
poolModel = File.Read('j', filepath, False, "Read pool model neutral.json")
Message.Post("Pool Model Type is: " + str(type(poolModel)))
simulation = Simulation()
scenario = simulation.Execute(poolModel)



Message.Post(str(scenario.Id))






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

Message.Post("End")