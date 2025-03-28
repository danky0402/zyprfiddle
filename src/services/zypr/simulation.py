import time, json, os
import pip._vendor.requests as requests
from urllib.parse import urljoin
from typing import Optional

from src.utilities.helpers.deserializers.deserializer import Deserialize
from src.utilities.helpers.local_message.message import Message
from src.utilities.helpers.application_settings import ApplicationSettings
from src.utilities.helpers.file_operations.file_operation import File

class Simulation():
                     
    _base_url: str = "https://api.zypr.app/v1/simulations"
  
    # intended as a local private method (by naming convention use the "__")
    def __PostMessage(scenario):
            
            Message.Post(f"Status Nbr: {str(scenario.StatusNBr)} \n"
                        f"Status: {str(scenario.StatusDescription)} \n" 
                        f"Started: {str(scenario.Progress.Started)} \n"
                        f"Completed: {str(scenario.Progress.Completed)} \n"
                        f"Percent Complete: {str(scenario.Progress.PercentComplete)} \n"
                        f"Transaction Count: {str(scenario.Progress.TransactionCount)} \n"
                        f"Percent Complete: {str(scenario.Progress.SequenceCount)}"
                        )

    # a public method
    @classmethod
    def Execute(cls, poolModel, tag:Optional[str] = None):                          # the tag parameter is a query string parameter
                                                                                    # use it to tag a group of simulations with the 
                                                                                    # same identifier (e.g., sensitivity_test_1) 
                                                                                    
        url = cls._base_url

        if tag is not None and len(tag) > 0:    
            tag = tag.replace(" ", "_")                                             # replace any whitespace with "_"
            url = urljoin(cls._base_url, f"?tag={tag}")                             # the tag opt
        
        try:
            apikey = ApplicationSettings.GetZyprApiKey()
            headers = {"Content-Type": "application/json",
                        "x-api-key": f"{apikey}" }
            
            response = requests.post(url, headers=headers, data=poolModel)
            
            if response.status_code != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

                                                                                    # this scenario response object is a json object, which can be referenced as a 
                                                                                    # python dictionary using the key to return the value:  scenario["Id"], or scenario["StatusNbr"]    


            response_json = response.json() # returns python dictionary or list

                                                                                    # file_path = os.path.join(str(os.getcwd()), "src", "test", "content", "scenario_first_response_obj.json")
                                                                                    # File.Save(file_path, response.text, False)

            scenario = Deserialize.Scenario(response_json)                          # deserializing is essentially casting the entire response object
                                                                                    # from a JSON string (readable as a python dictionary) into a  
                                                                                    # custom "Zypr" Scenario object, which is accessible via
                                                                                    # dot syntax (i.e., scenario.xxxx.xxxx).  With a list in the  
                                                                                    # object graph, like: scenario.HardwareInventory[0].IntervalNbr 
                                                                                    # where HardwareInventory is the list and [0] refers to the 
                                                                                    # first item in its list
                                                                
           
            Message.Post(f"Id: {str(scenario.Id)} \n"
                         f"Status: {str(scenario.StatusDescription)}")

            if scenario.StatusNbr > 7:                                              # check if first response contains an error
                                                                                    # if this was a dictionary cast to integer for comparison 
                                                                                    # casting changes the data type of the variable

                Message.Post(f"Error Message: {str(scenario.Errors.Message)}")      # will goto 'return scenario' below
                
            else:
                                                                                    
                _loop = True                                                        # set initial state of while loop
                                                                                    # enter into a while loop to and continue while _loop is true 
                                                                                    # this loop is to check (i.e., poll) the running status of the simulation
                while _loop: 

                    time.sleep(5)                                                   # suspends execution for 5 seconds, then continues

                    scenario = cls.GetScenarioRecord(scenario.Id)                   # returned response is a scenario obj
                    cls.__PostMessage(scenario)                                       # call local PostMethod method to post same info
                    
                    if scenario.StatusNbr >= 7:                                     # simulator reaches successful completion
                       _loop = False                                                # terminates the loop

            return scenario

        except Exception as e:
            Message.Post(f"Read file error: {e}")
            print(f"Error: {e}")                                                    # print error to terminal
            return None

    

    @classmethod
    def GetScenarioRecord(cls, id: str):
        
        apikey = ApplicationSettings.GetZyprApiKey()
        headers = {"Content-Type": "application/json",
                   "x-api-key": f"{apikey}" }
        
        url = f"{cls._base_url}/{id}"

        response = requests.get(url, headers=headers)
        
        obj = response.json()

        return Deserialize.Scenario(obj)


    @classmethod
    def SearchScenarios(cls, queryString:dict = None):

        apikey = ApplicationSettings.GetZyprApiKey()
        headers = {"Content-Type": "application/json",
                   "x-api-key": f"{apikey}" }
        
        if queryString is not None and type(queryString) is not dict:
              Message.Post("Search scenario 'query string' is not a dictionary")
              return
        
        # requests library docs say a querystring of None will not be added to url's query string 

        relative_url = "search"
        
        url = urljoin(cls._base_url, relative_url)

        response = requests.get(url, headers=headers, params=queryString)


    @classmethod
    def DeleteScenario(cls, mode:str, qsValue):   # valid mode is "id" or "tag"

        apikey = ApplicationSettings.GetZyprApiKey()
        headers = {"Content-Type": "application/json",
                   "x-api-key": f"{apikey}" }
            
        params = f"{ {mode} : {qsValue} }"

        url = cls._base_url
                
        response = requests.delete(url, headers=headers, params=params)
        msg = response.json()
        Message.Post(f"Http Status Code: {response.status_code} \n"
                     f"Message: {msg}" )
        
        return Deserialize.Scenario(msg)