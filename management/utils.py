import datetime
from hashlib import sha512
import codecs
import os
import json

class General:
    class Getters:
        
        def load_json(file_path):
            with open(file_path, "r") as f:
                return json.loads(f.read())
        
        def get_int(prompt, default=None):
            while True:
                try:
                    cmd = input(prompt)
                    if not cmd:
                        if default is not None:
                            return default
                        else:
                            print("Sorry, you must enter a value.")
                    else:
                        return int(cmd)
                except ValueError:
                    print("Sorry, that is not a valid integer.")
        
        def get_date_and_time():
            now = datetime.datetime.now()
            return now.strftime("%Y-%m-%d %I:%M:%S %p")
        
        def get_hash(text):
            return sha512(text.encode("utf-8")).hexdigest()
        
        def get_list(prompt, type_=None, limit=None):
            print(prompt)
            output = []
            if limit is None:
                while True:
                    cmd = input(">> ")
                    
                    if cmd.lower() in ["q", "quit", "exit"]:
                        break
                    
                    output.append(cmd)
            else:
                for _ in range(limit):
                    cmd = input(">> ")
                    
                    if cmd.lower() in ["q", "quit", "exit"]:
                        break
                    
                    output.append(cmd)
            
            return output

        def get_post_id():
            load = General.Getters.load_json("./BLOG_DATA/data.json")
            _id = load["blog_data"]["created_posts"]+1
            load["blog_data"]["created_posts"] = _id
            General.Setters.save_json("./BLOG_DATA/data.json", load)
            return _id
        
        def get_tag_id():
            load = General.Getters.load_json("./BLOG_DATA/data.json")
            _id = load["blog_data"]["created_tags"]+1
            load["blog_data"]["created_tags"] = _id
            General.Setters.save_json("./BLOG_DATA/data.json", load)
            return _id
            
            
            
    class Setters:
        
        def save_json(file_path, new_data):
            file = codecs.open(file_path, "w", "utf-8")
            json.dump(new_data, file, indent=4)
            
        def uppercase_list(list_):
            return [x.upper() for x in list_]
        
        def lowercase_list(list_):
            return [x.lower() for x in list_]
        
        def capitalize_list(list_):
            return [x.capitalize() for x in list_]
    
    class FileManager:
        def get_files(dir_path):
            files = []
            for obj in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, obj)):
                    files.append(obj)
                else:
                    files += General.FileManager.get_files(os.path.join(dir_path, obj))
            return files
        
        def create_folder (folder_name, dir_path):
            if dir_path == "..":
                dir_path = os.getcwd()
                
            if not os.path.exists(os.path.join(dir_path, folder_name)):
                os.mkdir(os.path.join(dir_path, folder_name))
                
            else:
                print("Folder already exists.")
        
        def create_folders(folder_names, dir_path):
            if dir_path == "..":
                dir_path = os.getcwd()
                
            for folder_name in folder_names:
                General.FileManager.create_folder(folder_name, dir_path)
        
        def create_file(file_name, dir_path, content=None):
            if dir_path == "..":
                dir_path = os.getcwd()
                
            if not os.path.exists(os.path.join(dir_path, file_name)):
                file = codecs.open(os.path.join(dir_path, file_name), "w", "utf-8")
                if content is not None:
                    file.write(str(content))
                file.close()
            else:
                print("File already exists.")
        
        def read_file(file_path):
            file = codecs.open(file_path, "r", "utf-8")
            return file.read()
        
        def remove_file(file_path):
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                print("File does not exist.")
        
        def remove_folder(folder_path):
            if os.path.exists(folder_path):
                os.rmdir(folder_path)
            else:
                print("Folder does not exist.")
        
        def folder_exists(folder_path):
            return os.path.exists(folder_path)