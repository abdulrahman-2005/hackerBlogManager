from utils import General

getters = General.Getters
setters = General.Setters
fileManager = General.FileManager
# FIRST
    #USER
    #BLOG INFO

def initialize_blog_data():
    
    if fileManager.folder_exists("./BLOG_DATA"):
        print("BLOG DATA ALREADY EXISTS")
        return
    
    user_data = {
        "author" : input("Author (the name will be displayed on the blogs): "),
        "email": input("Email [OPTIONAl] if you want to recive updates: "),
        "username": input("Create a username: "),
        "password": getters.get_hash(input("Make some good password: ")),
        "date_created": getters.get_date_and_time(),
        "last_time_modified": "CREATION"
    }
    
    blog_data = {
        "blog_name": input("blog name: "),
        "blog_field": getters.get_list("main fields for your blog, type q to exit"),
        "blog_languages": getters.get_list("languages you are going to write for"),
        "github_username": "",
        "github_blog_repo": "",
        "date_created": getters.get_date_and_time(),
        "last_time_modified": "CREATION",
        "created_posts": 0,
        "created_tags": 0,
    }
    
    paths = {
        "posts": f"./BLOG_DATA/posts.json",
        "tags": f"./BLOG_DATA/tags.json",
        "data": f"./BLOG_DATA/data.json"
    }
    
    data = {
        "user_data": user_data,
        "blog_data": blog_data,
        "paths": paths
    }
    
    # initiating blog data files
    fileManager.create_folder("BLOG_DATA", "..")
    fileManager.create_file("posts.json", "./BLOG_DATA", [])
    fileManager.create_file("tags.json", "./BLOG_DATA", [])
    fileManager.create_file("data.json", "./BLOG_DATA", data)
    
    # initating blog file structure
    fileManager.create_folder("blog", "..")
    fileManager.create_folders(blog_data["blog_languages"], "./blog")
    
    #return data
