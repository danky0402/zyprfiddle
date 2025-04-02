import json
import pip._vendor.requests as requests

from src.helpers.misc.application_settings import ApplicationSettings
from src.helpers.local_message.message import Message

class User():
    _base_url: str = "https://api.zypr.app/v1/users"
  

    @classmethod
    def NewUserRegistration(cls, firstName:str, emailAddress:str, organization:str):
            
        #   basic param validators
        if firstName is None or len(firstName) == 0:
            Message.Post("First Name must have a value")
            return
        
        if emailAddress is None or len(emailAddress) == 0:
            Message.Post("Email Address must have a value")
            return
        
        if organization is None or len(organization) == 0:
            Message.Post("Organization must have a value")
            return

        url = cls._base_url + "/registration"

        #   no api-key is required - it doesn't yet exist 
        headers = {"Content-Type": "application/json"}
        
        try:

            #  package user variables into a python dictionary using a dictionary literal
            #  the keys must match Zypr api specs
            
            body =  f'{{"FirstName" : "{firstName}", "Email" : "{emailAddress}", "Organization" : "{organization}"}}'    # To include a curly brace in string literal, it must be doubled
                        
            response = requests.post(url, headers=headers, data=body)
            
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            Message.Post(response)

            return response

                
        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None
        
    @classmethod    
    def ConfirmNewUserRegistration(cls, activationCode:str, emailAddress:str):
        
        if activationCode is None or len(activationCode) == 0:
            Message.Post("Activation Code must have a value")
            return
        
        if emailAddress is None or len(emailAddress) == 0:
            Message.Post("Email Address must have a value")
            return
        
        
        
        #   no api-key is required - it doesn't yet exist 
        headers = {"Content-Type":"application/json"}

        try:
            # requests library requires directly appending query string to url when using its post method
            url = f"{cls._base_url}/{activationCode}/registration?email={emailAddress}"
            
            response = requests.post(url, headers=headers)
            
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            # output to both because the response contains the user's new api-key
            Message.Post(f"Http response:  {response.status_code}")
            print(response.text)    # alternative output as backup for new api-key 

            return response

        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None
        
    @classmethod
    def RequestNewApiKey(cls, emailAddress:str):
        
        if emailAddress is None or len(emailAddress) == 0:
            Message.Post("Activation Code must have a value")
            return
        
        #   no api-key is required - assume the api key expired or the user doesn't know what it is 
        headers = {"Content-Type": "application/json"}

        try:
            
            # requests library requires directly appending query string to url when using its post method
            url = f"{cls._base_url}/registration?email={emailAddress}"

            response = requests.post(url, headers=headers)
            
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            Message.Post(response)
            

            return response

        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None
        

    def ConfirmNewApiKeyRequest(cls, authorizationCode:str, emailAddress:str):

        if authorizationCode is None or len(authorizationCode) == 0:
            Message.Post("Activation Code must have a value")
            return

        if emailAddress is None or len(emailAddress) == 0:
            Message.Post("Activation Code must have a value")
            return
        
        #   no api-key is required 
        headers = {"Content-Type": "application/json"}

        try:
            
            # requests library requires directly appending query string to url when using its post method
            url = f"{cls._base_url}/{authorizationCode}/registration?email={emailAddress}"

            response = requests.post(url, headers=headers)
            
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            # output to both because the response contains the user's new api-key
            Message.Post(f"Http response:  {response.status_code}")
            print(response.text)    # alternative output as backup for new api-key 

            return response

        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None


    @classmethod    
    def GetUserInfo(cls):
        
        url = cls._base_url + "/info"
        
        try:

            apikey = ApplicationSettings.GetZyprApiKey()
            headers = {"Content-Type": "application/json",
                        "x-api-key": f"{apikey}" }

            response = requests.get(url, headers=headers)
            
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            return response

        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None

    def DeleteUserAccount(cls, emailAddress:str):
        
        if emailAddress is None or len(emailAddress) == 0:
            Message.Post("Activation Code must have a value")
            return

        url = cls._base_url + "/registration"
        
        try:

            apikey = ApplicationSettings.GetZyprApiKey()
            headers = {"Content-Type": "application/json",
                       "x-api-key": f"{apikey}" }
            
            queryStringAsDictionary = dict(email=emailAddress)

            response = requests.delete(url, headers=headers, params=queryStringAsDictionary)
            
            if int(response.status_code) != 200:
                Message.Post(f"Error: {response.status_code}")
                return response

            # output to both because the response confirms user deletion
            Message.Post(f"Http response:  {response.status_code}")
            print(response.text)    # alternative output as backup for new api-key 
            
            return response

        except Exception as e:
            Message.Post(f"Critical error: {e}")
            print(f"Error: {e}")                                                    
            return None
