import pip._vendor.requests as requests

from src.helpers.misc.application_settings import ApplicationSettings
from src.helpers.local_message.message import Message



class Utility():
    _base_url: str = "https://api.zypr.app"
        

    @classmethod
    def HealthCheck(cls):
      
        url = cls._base_url + "/healthcheck"
        
        try: 
        
            response = requests.get(url)
        
            if(int(response.status_code) == 200):
                Message.Post(f"Healthcheck status: {response.status_code}")
            
            return int(response.status_code)

        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None
        
    
    @classmethod
    def GetStarterPoolModel(cls, code:str, version:str ):
    
        #   basic param validators
        if code is None or len(code) == 0:
            Message.Post("Code must have a value")
            return
    
        if version is None or len(version) == 0:
            Message.Post("Version must have a value")
            return  
        
        url = cls._base_url + "/v1/pool-models/search" 

        try:
            
            apikey = ApplicationSettings.GetZyprApiKey()
            headers = {"Content-Type": "application/json",
                    "x-api-key": f"{apikey}" }
            queryString = f"{'code' : '{code}', 'version' : {version}}"
            
            response = requests.get(url, headers=headers, params=queryString)
        
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            # output to both because the response confirms user deletion
            Message.Post(response)
            print(str(response))
            
            return response



        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None