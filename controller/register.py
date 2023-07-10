from flask import Flask, request, jsonify
from model import user
app = Flask(__name__)

@app.route('/login', methods=['POST'])#'/login'为url
def register(): 
