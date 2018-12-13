# Import statements necessary
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_script import Manager
import requests
from FP_codes import *
from FP_recs import *
#from FP_user import *


# Set up application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'elissafinalproject508'

manager = Manager(app)

# Routes

@app.route('/', methods = ['GET'])
def get_movie():

    return render_template('index.html')


@app.route('/movieuser', methods = ['GET'])
def confirm_movie():
    if request.method == "GET":
        result = request.args
        mov_one = result.get("mov1")
        mov_two = result.get("mov2")
        if mov_one == "" or mov_two == "":
            flash("Please input TWO movies")
            return redirect(url_for('get_movie'))
        if mov_one == "" and mov_two =="":
            flash("Please input TWO movies")
            return redirect(url_for('get_movie'))
        m1_list = movie_dict(mov_one)
        if m1_list == None:
            flash(mov_one + " is not a valid movie in our database :( Please try another movie!")
            return redirect(url_for('get_movie'))
        mov1_html = """<form action="http://localhost:5000/chosenmovies"method="GET">
                            <font face="helvetica"><ol>"""
        for m1 in m1_list[0:10]:
            #print(m1.title.__str__())
            mov1_html = mov1_html + "<li> <input type='radio' name='mov_one' value='" + m1.title.__str__() + "' checked>" + m1.__str__()+ "</li>"
        mov1_html = mov1_html + "</font></ol>"

        m2_list = movie_dict(mov_two)
        if m2_list == None:
            flash(mov_two + " is not a valid movie in our database :( Please try another movie!")
            return redirect(url_for('get_movie'))
        mov2_html = "<font face='helvetica'><ol>"
        for m2 in m2_list[0:10]:
            #print(m2.title.__str__())
            #mov2_html = mov2_html + "<li> <input type='radio' name='mov_two' value=" + m2.title.__str__() + ">" + m2.__str__()+ "</li>"
            mov2_html = mov2_html + "<li> <input type='radio' name='mov_two' value='" + m2.title.__str__() + "' checked>" + m2.__str__()+ "</li>"
        mov2_html = mov2_html + "</ol>" + "<input type='submit' value='Submit'> </form></font>"

        m1_header = """
<h2 style='color:#5D6D7E'><font face="helvetica">Here are the movies I found. Which ones of these did you mean?</h2>
<h4>(Choose one from the first list and one from the second list, then hit Submit at the bottom of the page)</font></h4>
        """
        m1_error = """ <h4 style='color:#7B241C; background-color:#F4F6F7'> Make sure you CLICK TWO BUTTONS or the page WILL break :( </h4>"""
        return "{}<h3><i>Your Movie 1 input: {}</i></h3>{}<br><h3><i>Your Movie 2 input: {}</i></h3>{}{}".format(m1_header, mov_one, mov1_html, mov_two, mov2_html,m1_error)

@app.route('/chosenmovies', methods = ['GET'])
def movie_chosen():
    if request.method == "GET":
        results = request.args
        print(results)
        movie_one = results.get("mov_one")
        print(movie_one)
        movie_two = results.get("mov_two")
        print(movie_two)
        movie_one_obj = movie_dict(movie_one)
        movie_two_obj = movie_dict(movie_two)
        movie_recs = tastedive_rec(movie_one + "," + movie_two)
        #print(movie_recs)
        # get the genre compare with original movies
        for per_rec in movie_recs:
            rec_genre = recs_steps(per_rec, movie_one_obj[0], movie_two_obj[0])
            dict_genre_count(rec_genre)
        top_ten_recs = sort_genre_count(movie_genre_dict)
        #print(top_ten_recs)
        rec_mov = "<ul><font face='helvetica'>"
        for rec in top_ten_recs:
            rec_info = movie_dict(rec[0])
            #print(rec_info)
            rec_mov = rec_mov + "<li>" + rec_info[0].__str__() + "</li>"
        rec_mov = rec_mov + "</font></ul>"
        return "<font face='helvetica'><i>The movies you chose are: {} and {}.</i><br> <h3 style='color:#5D6D7E'>Based on the movies you chose, you might also like these movies. ENJOY!</font></h3>{}".format(movie_one,movie_two,rec_mov)

if __name__ == '__main__':
    manager.run() # Runs the flask server in a special way that makes it nice to debug
