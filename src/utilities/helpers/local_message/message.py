# cannot use file_operations.py in this file because it would cause a circular reference
# file_operations.py uses this file to post messages

from filelock import FileLock       # added file locking to avoid conflicts

class Message:
    
    @staticmethod
    def Post(msg):
        
        try:
            #   this is the location of the message_file.txt
            filepath = "src\\utilities\\helpers\\local_message\\messages.txt"
            lock_path = filepath + ".lock"
            lock = FileLock(lock_path, timeout=1)
            
            with lock:
                # append mode at end of file
                with open(filepath, "a") as file:   
                    file.write(f"{msg} \n\n")  # single \n adds one new line
                                            # second \n creates a line space 
                                            # before next entry
        
        except FileNotFoundError:
            print(f"File not found: {filepath} ")

        
 
    @staticmethod
    def Clear():
        try:

            filepath = "src\\utilities\\helpers\\local_message\\messages.txt"
            lock_path = filepath + ".lock"
            lock = FileLock(lock_path, timeout=1)
            
            with lock:
                # over-write mode - write starts 0
                with open(filepath, "w") as file:
                    # removes existing content in file - truncates back to 0
                    file.truncate(0)  
                    file.close()

        except FileNotFoundError:
            print(f"File not found: {filepath} ")