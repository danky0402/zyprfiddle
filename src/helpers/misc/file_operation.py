import os, re, json


from src.helpers.local_message.message  import Message

class File():

    @staticmethod
    def Append(filepath:str,
               content,
               suppressMsg:bool = False,
               operation_name:str = None):
        
        try:
            if operation_name is not None:
                operation_name = f"{operation_name}"   

            if os.path.exist(filepath):                
                                                                                            #   append mode at end of file
                with open(filepath, "a") as file:                                           #   automatically should close file
                    file.write(f"{content} \n")                                             #   single \n adds one new line
                    
                    if suppressMsg is False and operation_name is None:
                        Message.Post("Append file success")
                    if suppressMsg is False and operation_name is not None:
                        Message.Post(f"{operation_name}: Success")

            else:
                Message.Post(f"Append file failure: File {filepath} doesn't exist")
        
        except Exception as e:
            Message.Post(f"Append file error: {e}")
            print(f"Error: {e}")    # print error to terminal


    
    @staticmethod
    def Save(filepath,
             content: str,
             suppressMsg:bool = False,
             operation_name:str = None):
        
        try:
            if operation_name is not None:
                operation_name = f"{operation_name}"   

            with open(filepath, "w") as file:                                               #   if file exists, then over-write existing content 
                file.write(content)                                                         #   if file doesn't exist, creates new file and writes
                
                if suppressMsg is False and operation_name is None:
                        Message.Post("Save file success")
                if suppressMsg is False and operation_name is not None:
                        Message.Post(f"{operation_name}: Success")

        except Exception as e:
            Message.Post(f"Save file error: {e}")
            print(f"Error: {e}")    # print error to terminal

    @staticmethod
    def Read(mode: str,     # try to return a specific type - may throw an error if cannot cast to the selected type 
                            # 's' = clean string (no formatting or whitespace)
                            # 'd' = dictionary
                            # 'j' = json-to-clean minified json (no formatting or whitespace)


             filepath: str,
             suppressMsg:bool = False,
             operation_name:str = None):
            
        try:
            if operation_name is not None:
                operation_name = f"{operation_name}"    

            if os.path.exists(filepath):

                with open(filepath, 'r') as file:   # 
                    
                    try:
                        
                        if mode == 'd':
                            content = dict(json.loads(re.sub(r"[\n\t\s+]", " ", file.read())))

                        elif mode == 'j': 
                            content = re.sub(r"[\n\t\s]*", "", str(file.read()))

                        else:   # default is string  
                            content = file.read()

                    except ValueError as e:
                        Message.Post(f"ValueError: {e}")
                        return None

                if suppressMsg is False and operation_name is None:
                        Message.Post("Read file success")
                if suppressMsg is False and operation_name is not None:
                        Message.Post(f"{operation_name}: Success")
                
                return content                
            else:
                Message.Post(f"Read file failure: File {filepath} doesn't exist")
                
        except Exception as e:
            Message.Post(f"Read file error: {e}")
            print(f"Error: {e}")    # print error to terminal

        return None

    

