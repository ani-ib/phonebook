
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        name = "John Smith"
        number = "234-210-4275"
        location = "USA"


        return jsonify({'name': name , 'number': number , 'location': location })
  

  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)