import sys
sys.path.append('E:/workspace/FAFA-Web/')
from src.model.article import ArticleDB
from flask import request, jsonify, Flask
import logging
import os
# 配置日志记录
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建日志记录器
logger = logging.getLogger(__name__)

class ArticleController:
    articleDB = ArticleDB()
    def __init__(self):
        pass
        
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
            return jsonify({'message': '文章存储成功'})   
        except Exception as e:
            logger.error('文章信息存储失败:{}'.format(e))
            return jsonify({'message': '文章存储失败'})
        
    def update(self):
        try:
            data = request.get_json()
            author_name = data['author_name']
            article_name = data['article_name']
            new_author_name = data['new_author_name']
            new_article_name = data['new_article_name']
            new_article_body = data['article_body']
        
            self.articleDB.update_article(article_name,author_name,new_article_name,new_author_name)
            file_name='{}.txt'.format(new_article_name)
            with open(file_name,'w')as file:
                file.write(new_article_body)
            logger.info('更新成功：{}'.format(new_article_name))
            return jsonify({'message': '文章更新成功'})
        except Exception as e:
            logger.error('更新失败:{}'.format(e))
            return jsonify({'message': '文章更新失败'})
    
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

app = Flask(__name__)

# 创建文章控制器实例
article_controller = ArticleController()

# 路由 - 创建文章
@app.route('/creat_article', methods=['POST'])
def creat_article():
    return article_controller.creat()

# 路由 - 更新文章
@app.route('/update_article', methods=['POST'])
def update_article():
    return article_controller.update()

# 路由 - 删除文章
@app.route('/delete_article', methods=['POST'])
def delete_article():
    return article_controller.delete_article()

# 运行 Flask 应用
if __name__ == '__main__':
    app.run()