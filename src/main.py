from flask import Flask, request, jsonify
from model.classuser import user

app=Flask(__name__)
user=user()

