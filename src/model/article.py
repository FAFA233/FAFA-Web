import time
class article:
    def __init__(self, name, author_name=""):
        self.name = name
        self.author_name = author_name
        self.publish_date = time.localtime()
        self.latest_edited_date = time.localtime()
        self.file_name : str

    def update(self):
        pass
    
    def delete(self):
        pass

    

    