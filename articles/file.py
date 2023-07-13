class ArticleController:
    #不知道自己写了啥玩意
    def __init__(self, model):
        self.model = model

    def update_article(self):
        self.model.update()

    def delete_article(self):
        self.model.delete()

    def set_article_name(self, name):
        self.model.name = name

    def set_article_author(self, author_name):
        self.model.author_name = author_name