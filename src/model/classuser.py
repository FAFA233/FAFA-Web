from flask import Flask, request, jsonify
from sql import UserDB
class user():
    def __init__(self) :
        self.user=UserDB()

    def login (self,user_name ,password):
        self.user.find(user_name )
            
    def register(self, user_name,password ):
            self.register(user_name,password)
        
    def change(self,user_name,new_password):
            self.change(user_name, new_password) 

    def delete(self,user_name, new_password):
         self.delete(user_name, new_password)
       
    def login_stastus(self,user_name,is_login):
        self.user.change_login_status(user_name,is_login)
        