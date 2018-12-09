## Final Project Codes ##

# Functions needed:
# (1) unique identifier for cache
# (2) requesting info from TMDb API
# (3) scrape Rotten Tomatoes and put things in a dictionary
# (4) compare movie genre and rating searched to list a movie
# (5) emotions from movie tags and the most famous
# (6) ratings from most famous movies

## IMPORTS ##
from FP_cache import *
from bs4 import BeautifulSoup
from FP_secrets import *
import requests

## CACHE ##
cache_file = "movies.json"
cache = Cache(cache_file)

def check_cache(site, param=None):
    UID = site + str(param)
    response = cache.get(UID)
    if response == None:
        response = requests.get(site, params=param).text
        cache.set(UID, response)
    return response

## REQUEST TMDB API ##
# diction will come from the input for the query.
def request_movie(diction):
    base = "https://api.themoviedb.org/3/search/movie"
    response = check_cache(base, diction)
    json_response = json.loads(response)
    return json_response

#test_movie_diction = {"api_key": tmdb_key, "query": "parent trap"}
#print(request_movie(test_movie_diction))

## REQUEST  GENRE ID NAMES ##
def request_genreID():
    base = "https://api.themoviedb.org/3/genre/movie/list"
    diction = {"api_key": tmdb_key}
    response = check_cache(base, diction)
    json_response = json.loads(response)
    genre_dict_list = json_response["genres"]
    return genre_dict_list

#print(request_genreID())

## CHANGE LIST OF GENRE DICTIONARY TO ONE DICTIONARY ##
genre_list = request_genreID()
genre_dict = {}
for each_genre in genre_list:
    genre_dict[each_genre["id"]] = each_genre["name"]
#print(genre_dict)

## GET GENRE ID NAME ##
def genre_name(num_id):
    if num_id not in genre_dict.keys():
        print("Genre ID is not valid")
    movie_genre = genre_dict[num_id]
    return movie_genre

#print(genre_name(28))

class Movie():
    def __init__(self, movie_info):
        self.id = movie_info.get("id", "None")
        self.title = movie_info.get("title", "None")
        self.release = movie_info.get("release_date", "None")
        self.plot = movie_info.get("overview", "None")
        self.genre = movie_info.get("genre_ids", "None")

    def __str__(self):
        info = "{}\n{}\n{}".format(self.title, self.release, self.plot)
        return info

    def __repr__(self):
        rep = self.title
        return rep

#print(Movie(["Inception", "2017", "A man dreaming", "28"]))

# get movie dictionary from request. Info needed:
# movie ID (key)
# movie title
# movie release date
# movie plot
# movie rating
# movie genre
# movie tag

def movie_dict(movie):
    """This is a movie dictionary function"""
    movie_diction = {"api_key": tmdb_key, "query": movie}
    movie_response = request_movie(movie_diction)
    #print(movie_response)
    results_list = movie_response["results"]
    user_movie_dict = {}
    movie_objects = []
    for per_movie in results_list:
        # print("---------------")
        # print(per_movie)
        class_movie = Movie(per_movie)
        movie_objects.append(class_movie)
    return movie_objects

#print(movie_dict("parent trap"))

# change str title chosen to a string for Rotten Tomatoes
# def cleaned_title(user_movie_str):
#     title_clean = []
#     str_title = user_movie_str.title
#     for each in str_title:
#         if not each.isalnum():
#             if each == " " or each == "-":
#                 title_ch = each.replace(each,"_")
#                 title_clean.append(title_ch)
#         else:
#             title_ch = each.lower()
#             title_clean.append(title_ch)
#     clean_title = "".join(title_clean)
#     return clean_title
#
# # scrape Rotten Tomatoes browse all page
# def dvd_stream_browse_all(movie):
#     rotten_site = "https://www.rottentomatoes.com/browse/dvd-streaming-all"
#     response = requests.get(rotten_site).text
#     soup = BeautifulSoup(response, 'html.parser')
#     movie_link = soup.find_all(mps = "mps")
#     return movie_link
#
# #print(dvd_stream_browse_all("a"))
# # scrape Rotten Tomatoes for ratings
# def dvd_stream_movie(movie):
#     rotten_site = "https://www.rottentomatoes.com/m/" + movie
#     response = check_cache(rotten_site)
#     #req_resp = requests.get(rotten_site).text
#     soup = BeautifulSoup(response, 'html.parser')
#     ratings = soup.find_all(class_ = "meter-value")
#     if ratings == []:
#         return movie + " is not found in Rotten Tomatoes."
#     tomatoer = ratings[0].text.replace("\n","")
#     audience = ratings[1].text.replace("\n", "")
#     return tomatoer, audience

#print(dvd_stream_movie("the_cinderella_story"))

# get genre for movie chosen
# genre is in the Movie class
# def list_of_genre(movie_obj):
#     list_genre_id = movie_obj.genre
#     genre_id_name = []
#     for each_id in list_genre_id:
#         genre_n = genre_name(each_id)
#         genre_id_name.append(genre_n)
#     return genre_id_name


## TEST ##
# test_movie = movie_dict("spiderman")
# genre_test = test_movie[5]
# print(list_of_genre(genre_test))
