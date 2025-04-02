import json, datetime

from src.helpers.local_message.message import Message
from src.helpers.deserializers.deserializer import Deserialize
from src.services.zypr.simulation import Simulation
from src.services.zypr.utility import Utility

Message.Clear()


#   1. check zypr is available

utility  = Utility()
status_code = utility.HealthCheck()
if status_code != 200:
    Message.Post( f"Zypr health check failed with status code: {str(status_code)}")
    quit()


dt = "2025-03-30"

#   2. set a variable to your target scenario id 

querystring = f'{{"created-date" : "{dt}"}}'
querystring = eval(querystring)
print(type(querystring))


#   2. define a new Simulation object and execute search method

simulation = Simulation()
response = simulation.SearchScenarios(querystring)                               #   this method requires your api-key, which is automatically fetched by the method


#   3. check response of http request 

Message.Post(str(f"Http status code:  {response.status_code}")) 
if int(response.status_code) != 200:
    quit()


#   4. output results in local window

scenario_dict = json.loads(response.text)                                       #   convert to a python dictionary
lst = list(scenario_dict["ScenarioSummaries"].values())                         #   Scenario Summaries returns list as a key-value pair
                                                                                #       where the key is scenario's date (for pagination)
                                                                                #       so the scenario summaries are contained in the value 
                                                                                #       in the key-value pair

Message.Post("Scenario count: " + str(scenario_dict["Count"]))                  
Message.Post(json.dumps(lst, indent=4))                                         #   output as formatted json


Message.Post("End")

