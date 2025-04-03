import json

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

#   2. set a variable to your target scenario id 
scenario_id = "da.fov6u0mkjfkiuv1bwekor"

#   2. define a new Simulation object, execute and receive the response object  
simulation = Simulation()
response = simulation.GetScenarioRecord(str(scenario_id))                               #   this method requires your api-key, which is automatically fetched by the method

#   3. check response of http request 
Message.Post(str(f"Http status code:  {response.status_code}")) 
if int(response.status_code) != 200:
    quit()


#   4. to further manipulate, first deserialize JSON string to a python dictionary then deserialize dictionary into Scenario class object 
scenario_dict = json.loads(response.text)  
scenario = Deserialize.Scenario(scenario_dict)

Message.Post(scenario.Id)

#   5. build tab-seperated values lists for Resource Requirements Forecast time series objects

Message.Clear()
tsv = scenario.ResourceRequirementsForecast.Convert().All()
Message.Post(tsv)

Message.Clear()
tsv = scenario.CalendarizedForecast.Convert().All()
Message.Post(tsv)
quit()


Message.Post("End")