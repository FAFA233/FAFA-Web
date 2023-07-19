from flask import Flask, request, jsonify
from controller import control
import sys
sys.path.append('E:/workspace/FAFA-Web/')
app=Flask('__name__')

if __name__ == "__main__":
    app.run()