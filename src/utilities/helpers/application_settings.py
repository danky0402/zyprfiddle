
import os
from src.utilities.helpers.file_operations.file_operation import File

class ApplicationSettings:

    @staticmethod
    def GetZyprApiKey():
        filepath = os.path.join(os.getcwd(), "content\\secrets\\zypr\\secrets.json")
        dict = File.Read('d', filepath, False, "Get zypr api key")
        return str(dict["ZyprApiKey"])
    
    @staticmethod
    def GetZyprBaseUrl():
        return "https://zypr.app"


