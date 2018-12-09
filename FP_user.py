## IMPORTS ##
from FP_cache import *
from bs4 import BeautifulSoup
from FP_secrets import *
import requests
from FP_codes import *
from FP_recs import *

# ASK FOR MOVIE #
# print("HELLO! Welcome to my movie rec!")
# user_in = input("Please input two movies you like separated by a comma(,) -  ")
#
# # PRODUCE LIST #
# user_in_list = user_in.split(",")
# user_in_one = user_in_list[0]
# user_in_two = user_in_list[1]

def produce_list(user, m_num):
    obj_list = movie_dict(user)
    print("Here are the movies I found for the " + m_num + " movie you inputted.\nWhich one of these movies did you mean?\n")

    count = 1
    for mov in obj_list:
        print(str(count) + ": " + mov.__str__())
        print("---------------------------\n")
        count += 1
    # CHOOSE MOVIE #
    # user_num = input("Choose the number next to the " + m_num +" movie that you would like recommendations for - ")
    # user_chosen = obj_list[int(user_num) - 1].title
    return
# movie_confirm = input("Is this the correct movie? [Y/N] - ")
# if movie_confirm.upper() == "N":
#     user_num = input("Choose the correct number - ")
#print(change_obj_str(user_chosen_movie))

# rotten_title = cleaned_title(user_chosen_movie)
# print(dvd_stream_movie(rotten_title))

# mov_one = produce_list(user_in_one, "1st")
# mov_two = produce_list(user_in_two, "2nd")
# mov_one_obj = movie_dict(mov_one)
# mov_two_obj = movie_dict(mov_two)
# #print([mov_one, mov_two])
# #movie_genre_dict = {}
# print("---------------------------------------------------------------")
# print("Here are the movies similar to the two movies you chose. ENJOY!")
# print("---------------------------------------------------------------")
# recs = tastedive_rec(mov_one+","+mov_two)
# for each in recs:
#     genre_list = recs_steps(each, mov_one_obj[0], mov_two_obj[0])
#     dict_genre_count(genre_list)
# sort_genre_count(movie_genre_dict)
