import time
from sqlmodel import SQLModel,create_engine,Session
class ArticleModel(SQLModel):
    article_name: str
    author_name: str
    create_time: float
    update_time: float

class ArticleDB:
    def _init__(self):
        self.engine = create_engine("s_qlite:///articles.db")
        SQLModel.metadata.create_all(self.engine)

    def add_article(self, article_name, author_name):
        with Session(self.engine) as session:
            create_time = time.time()
            update_time = time.time()
            article = ArticleModel(article_name=article_name, author_name=author_name,
                                    create_time=create_time, update_time=update_time)
            session.add(article)
            session.commit()
    
    def update_article(self, article_name, author_name, new_article_name=None, new_author_name=None):
        with Session(self.engine) as session:
            update_time = time.time()
            article = session.query(ArticleModel).filter(ArticleModel.article_name == article_name,
                                                        ArticleModel.author_name == author_name).first()
            #query查询第一个匹配的对象
            if article:
                if new_article_name:
                    article.article_name = new_article_name
                if new_author_name:
                    article.author_name = new_author_name
            #如果有新的作者名或者新的文章标题，进行更改
                article.update_time = update_time
                session.commit()

    def delete_article(self, article_name, author_name):
        with Session(self.engine) as session:
            article = session.query(ArticleModel).filter(ArticleModel.article_name == article_name, ArticleModel.author_name == author_name).first()
            if article:
                session.delete(article)
                session.commit()
                #查询并删除