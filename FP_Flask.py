# Import statements necessary
from flask import Flask, render_template, request
from flask_script import Manager
import requests
from FP_codes import *
from FP_recs import *
from FP_user import *


# Set up application
app = Flask(__name__)

manager = Manager(app)

# Routes

@app.route('/', methods = ['GET'])
def get_movie():
    m = """
<h1>Welcome to Movie Recs!</h1>
<h3>Please input two movies that you like below:</h3>
<form action = 'http://localhost:5000/movieuser' method='GET'>
Movie 1:<br>
<input type="text" name="mov1" value=""><br>
Movie 2:<br>
<input type="text" name="mov2" value=""><br>
<input type="submit" value="Submit">
</form>
    """
    return m


@app.route('/movieuser', methods = ['GET'])
def confirm_movie():
    if request.method == "GET":
        result = request.args
        mov_one = result.get("mov1")
        mov_two = result.get("mov2")
        m1_list = movie_dict(mov_one)
        #print(type(m1_list))
        #for each in m1_list:
        return "Here are the movies I found. Which one did you mean? {}".format(m1_list)
#"Here are the movies I found for the movies you inputted. Which one did you mean?\n {}".format(m1_list)
# @app.route('/user/<yourname>')
# def hello_name(yourname):
#     return '<h1>Hello {}</h1>'.format(yourname)

if __name__ == '__main__':
    manager.run() # Runs the flask server in a special way that makes it nice to debug
