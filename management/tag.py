from utils import General
import tabulate

setters = General.Setters
getters = General.Getters


def create_tag(tag_data=None):
    
    if tag_data is not None:
        tag_title = tag_data["tag_title"]
        tag_description = tag_data.get("tag_description", None)
        taged_post = tag_data.get("taged_post", None)
    else:
        tag_title = input("Tag Title: ")
        tag_description = input("Tag Description: ")
        
    tag_data = {
        "tag_title": tag_title,
        "tag_date": General.Getters.get_current_date(),
        "tag_last_modified": "CREATION",
        "tag_id": General.Getters.get_tag_id(),
        "tag_posts": [taged_post] if taged_post is not None else [],
        "tag_description": tag_description,
    }
    
    load = getters.load_json("./BLOG_DATA/tags.json")
    load.append(tag_data)
    General.Setters.save_json("./BLOG_DATA/tags.json", load)
    
    print(f"Tag {tag_title} created successfully.")

def show_tags(style):
    data = General.Getters.load_json("./BLOG_DATA/tags.json")
    headers = ["Title", "Number of Posts", "ID", "Date"]
    table_data = [[d["tag_title"], len(d["tag_posts"]), d["tag_id"], d["tag_date"]] for d in data]

    print(tabulate.tabulate(table_data, headers=headers, tablefmt=style))