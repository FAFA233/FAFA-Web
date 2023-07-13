import time
class ArticleModel:
    def __init__(self, name, author_name=""):
        self.name = name
        self.author_name = author_name
        self.publish_date = time.localtime()
        self.latest_edited_date = time.localtime()
        self.file_name: str

    def update(self):
        self.latest_edited_date = time.localtime()
        
    def delete(self):
        self.name = ""
        self.author_name = ""
        self.publish_date = None
        self.latest_edited_date = None
        self.file_name = ""
    

    