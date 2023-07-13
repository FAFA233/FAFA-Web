from model.sql import DB

class ArticleDB(DB):
    def __init__(self):
        super(ArticleDB, self).__init__("article.db")

    def add(self, article):
        pass

    def delete(self, article_id):
        pass

    def change(self, article_id, new_data):
        pass
    
    def find(self, condition):
        pass