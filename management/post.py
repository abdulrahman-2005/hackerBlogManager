from utils import General
from tag import create_tag

setters = General.Setters
getters = General.Getters


def create_post(post_title=None, post_description=None, post_tags=None):
    if post_title is not None and post_tags is not None:
        post_data = {
            "post_title": post_title,
            "post_description": post_description,
            "post_tags": General.Setters.uppercase_list(post_tags),
            "post_date": General.Getters.get_date_and_time(),
            "post_last_modified": "CREATION",
            "post_id": General.Getters.get_post_id()
        }
    else:
        post_data = {
            "post_title": input("post title: "),
            "post_description": input("post description: (press enter to skip)"),
            "post_tags": General.Setters.uppercase_list(General.Getters.get_list("tags for the post, type q to exit")),
            "post_date": General.Getters.get_date_and_time(),
            "post_last_modified": "CREATION",
            "post_id": General.Getters.get_post_id()
        }
        if post_data["post_description"] == "":
            post_data["post_description"] = None
        
    for tag_title in post_data["post_tags"]:
        create_tag(tag_title, post_data["post_id"])
    
    load = General.Getters.load_json("./BLOG_DATA/posts.json")
    load.append(post_data)
    General.Setters.save_json("./BLOG_DATA/posts.json", load)


import tabulate

def show_posts(style):
    data = General.Getters.load_json("./BLOG_DATA/posts.json")
    headers = ["Title", "ID", "Date"]
    table_data = [[d["post_title"], d["post_id"], d["post_date"]] for d in data]
    print(tabulate.tabulate(table_data, headers=headers, tablefmt=style))
    
    
