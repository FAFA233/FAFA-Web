from model.sql import DB

class ArticleDB(DB):
    def __init__(self):
        super(ArticleDB, self).__init__("article.db")

    def add(self, article):
        """向articles中添加一篇文章,插入文章标题内容

        Args:
            article (str): _description_
        """
        with self.connection.begin() as transaction:
            self.connection.execute(
                "INSERT INTO articles (title, content) VALUES (:title, :content)",
                {"title": article["title"], "content": article["content"]}
            )

    def delete(self, article_id):
        """_summary_

        Args:
            article_id (_type_): _description_
        """
        with self.connection.begin() as transaction:
            self.connection.execute(
                "DELETE FROM articles WHERE id = :article_id",
                {"article_id": article_id}
            )

    def change(self, article_id, new_data):
        """_summary_

        Args:
            article_id (_type_): _description_
            new_data (_type_): _description_
        """
        with self.connection.begin() as transaction:
            self.connection.execute(
                "UPDATE articles SET content = :new_content WHERE id = :article_id",
                {"new_content": new_data, "article_id": article_id}
            )

    
    def find(self, condition):
        """_summary_

        Args:
            condition (_type_): _description_

        Returns:
            _type_: _description_
        """
        result = self.connection.execute(
            "SELECT * FROM articles WHERE title = :title",
            {"title": condition}
        )
        return result