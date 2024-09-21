'''
    route performing crud operation
'''
from system import app


@app.route('/')
def home():
    return "Welcome to our library management system"