from src.model.article import ArticleDB
from flask import Flask, request, jsonify
import logging
import os
# 配置日志记录
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建日志记录器
logger = logging.getLogger(__name__)
class ArticleController:
    def __init__(self):
        self.articleDB = ArticleDB()
        
    def creat(self):
        try:
            data = request.get_json()
            author_name = data['author_name']
            article_name = data['article_name']
            article_body = data['article_body']
            logger.info('文章信息存储成功：{}'.format(article_name))
        
            file_name = '{}.txt'.format(article_name)  # 文本文件名以文章名命名
            with open(file_name, 'w') as file:
                file.write(article_body)
            logger.info('文章内容存储成功{}'.format(article_name))   
        except Exception as e:
            logger.error('文章信息存储失败:{}'.format(e))

    def update(self):
        try:
            data = request.get_json()
            new_author_name = data['author_name']
            new_article_name = data['article_name']
            new_article_body = data['article_body']
        
            self.articleDB.update_article(new_article_name,new_author_name)
            file_name='{}.txt'.format(new_article_name)
            with open(file_name,'w')as file:
                file.write(new_article_body)
            logger.info('更新成功：{}'.format(new_article_name))
        except Exception as e:
            logger.error('更新失败:{}'.format(e))
    
    def delete_article(self):
        try:
            data = request.get_json()
            author_name = data['author_name']
            article_name = data['article_name']
            article_body = data['article_body']
            self.articleDB.delete_article(article_name,author_name)
            file_name = '{}.txt'.format(article_name)
            os.remove(file_name)
            logger.info('删除成功：{}'.format(article_name))

            return jsonify({'message': '文章删除成功'})
        except Exception as e:
            logger.error('删除失败:{}'.format(e))
            return jsonify({'message': '文章删除失败'})
