# print("Hello World")
from flask import Flask
server =Flask(__name__)

@server.route("/page")
def page():
    return "Hello Python"



server.run()