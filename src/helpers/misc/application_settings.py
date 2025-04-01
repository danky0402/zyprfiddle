
import os
from src.helpers.misc.file_operation import File

class ApplicationSettings:

    @staticmethod
    def GetZyprApiKey(suppressMsg = False):
        filepath = os.path.join(os.getcwd(), "content\\secrets\\zypr\\secrets.json")
        dict = File.Read('d', filepath, suppressMsg, "Get zypr api key")
        return str(dict["ZyprApiKey"])
    
    @staticmethod
    def GetZyprBaseUrl():
        return "https://zypr.app"


