import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

TAGS_FILE = 'BLOG_DATA/tags.json'
POSTS_FILE = 'BLOG_DATA/posts.json'

class MyGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Load the tags and posts from the JSON files
        self.tags = self.load_tags()
        self.posts = self.load_posts()
        
        # Create widgets to display the tags and posts
        self.tags_layout = BoxLayout(orientation='vertical')
        for tag in self.tags:
            tag_label = Label(text=tag['tag_title'])
            self.tags_layout.add_widget(tag_label)
            
        self.posts_layout = BoxLayout(orientation='vertical')
        for i, post in enumerate(self.posts):
            post_button = Button(text=post['post_title'])
            setattr(post_button, 'post_index', i)
            post_button.bind(on_press=self.show_post)
            self.posts_layout.add_widget(post_button)
            
        # Add the widgets to the GUI layout
        self.add_widget(self.tags_layout)
        self.add_widget(self.posts_layout)
        
    def load_tags(self):
        with open(TAGS_FILE) as f:
            tags = json.load(f)
        return tags
        
    def load_posts(self):
        with open(POSTS_FILE) as f:
            posts = json.load(f)
        return posts
        
    def show_post(self, button):
        # Retrieve the post index from the button attribute
        post_index = button.post_index
        
        # Create a new screen to display the full post content
        post = self.posts[post_index]
        post_layout = BoxLayout(orientation='vertical')
        post_title = Label(text=post['post_title'])
        post_description = Label(text=post['post_description'])
        post_layout.add_widget(post_title)
        post_layout.add_widget(post_description)
        # ... add additional widgets to display the full post content ...
        self.clear_widgets()
        self.add_widget(post_layout)
        
    def update_tag(self, tag_id, new_title):
        tags = self.load_tags()
        for tag in tags:
            if tag['tag_id'] == tag_id:
                tag['tag_title'] = new_title
                break
        with open(TAGS_FILE, 'w') as f:
            json.dump(tags, f)
            
    def update_post(self, post_id, new_title, new_description):
        posts = self.load_posts()
        for post in posts:
            if post['post_id'] == post_id:
                post['post_title'] = new_title
                post['post_description'] = new_description
                break
        with open(POSTS_FILE, 'w') as f:
            json.dump(posts, f)
        
class MyApp(App):
    def build(self):
        return MyGUI()

if __name__ == '__main__':
    MyApp().run()
