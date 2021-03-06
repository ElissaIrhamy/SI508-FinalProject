# This is where TasteDive API function lives and checking with genre in TMDB API and ratings in rotten tomatoes

## IMPORT ##
from FP_cache import *
from bs4 import BeautifulSoup
from FP_secrets import *
import requests
from FP_codes import *
import matplotlib.pyplot as plt

## REQUEST FROM TASTEDIVE API ##
def tastedive_rec(movie):
    taste_base = "https://tastedive.com/api/similar"
    taste_param = {"q": "movie:" + movie.lower(), "type": "movies", "k": taste_dive_key}
    response = check_cache(taste_base, taste_param)
    json_response = json.loads(response)
    #print(json_response)
    mov_rec_dict = json_response["Similar"]["Results"]
    if mov_rec_dict == []:
        return None
    #print(mov_rec_dict)
    mov_names = []
    for each in mov_rec_dict:
        each_name = each.get("Name", "None")
        mov_names.append(each_name)
    #print(mov_names)
    return mov_names

#print(tastedive_rec("jnfjberfb,fdjhbvj"))

## CHECK EACH MOVIE FROM TASTEDIVE WITH GENRE ID FROM TMDB, PUT IN DICTIONARY ##
def recs_steps(movie, ori_movie_obj1, ori_movie_obj2):
    tmdb_req = movie_dict(movie)
    tmdb_mov_list = []
    genre = tmdb_req[0].genre
    #print("user movie: ", genre)
    ori_genre1 = ori_movie_obj1.genre
    #print("first movie genre: ", ori_genre1)
    ori_genre2 = ori_movie_obj2.genre
    #print("second movie genre: ", ori_genre2)
    ori_genre = ori_genre1 + list(set(ori_genre2) - set(ori_genre1))
    #print("combined list: ", ori_genre)
    if genre == []:
        return None
    elif ori_genre1 == []:
        return None
    elif ori_genre2 == []:
        return None
    count = 0
    same_genre_id = []
    for each in genre:
        if each in ori_genre:
            same_genre_id.append(each)
            count += 1
    same_genre = []
    for each in same_genre_id:
        gen_id_name = genre_name(each)
        same_genre.append(gen_id_name)
    tmdb_mov_list.append(tmdb_req[0].title)
    tmdb_mov_list.append(count)
    tmdb_mov_list.append(same_genre)
    #print(tmdb_mov_list)
    return tmdb_mov_list

## CHECK DICTIONARY WITH GENRE COUNT AND SORT THEM FROM MOST TO LEAST ACCORDING TO COUNT ##
movie_genre_dict = {}
def dict_genre_count(movie_genre_list):
    # movie_genre_dict is a global dictionary
    movie_genre_dict[movie_genre_list[0]] = [movie_genre_list[1], movie_genre_list[2]]
    #print(movie_genre_dict)
    return movie_genre_dict

def sort_genre_count(dict):
    genre_sorted = sorted(dict.items(), key = lambda x:x[1], reverse = True)
    #print(genre_sorted)
    top_ten_list = []
    #print(len(genre_sorted))
    if len(genre_sorted) < 10:
        for each in genre_sorted:
            top_ten_list.append(each[0])
            #print(top_ten_list)
    else:
        count = 0
        while count < 10:
            #print(genre_sorted[count])
            top_ten_list.append(genre_sorted[count])
            count += 1

    return top_ten_list

# use class movie numbers to print out a pie chart/graph of budget, revenue use matplotlib
def plot_numbers(budget, revenue):
    labels = "Budget", "Revenue"
    sizes = [budget, revenue]
    explode = (0.1,0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    return 
