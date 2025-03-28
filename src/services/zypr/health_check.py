import pip._vendor.requests as requests
from urllib.parse import urljoin
from src.utilities.helpers.local_message.message import Message

# no apikey is required

class HealthCheck():
    _base_url: str = "https://api.zypr.app"
        

    @classmethod
    def Get(cls):
        
        relative_url = "/healthcheck"
        url = urljoin(cls._base_url, relative_url)
        response = requests.get(url)
        if(int(response.status_code) == 200):
            Message.Post(f"Healthcheck status: {response.status_code}")
        
        return response.status_code
        


    