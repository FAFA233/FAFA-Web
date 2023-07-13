from flask import Flask, request, jsonify
from controller import control

app=Flask('__name__')

if __name__ == "__main__":
    app.run()