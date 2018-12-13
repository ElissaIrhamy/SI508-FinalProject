## IMPORTS ##
import unittest
from FP_codes import *
from FP_recs import *
from FP_secrets import *
from FP_cache import *

# 3 classes, test the Movie class, test the API retrieval, test the running of the code

class test_class_Movie(unittest.TestCase):
    """ This test class is to check the contents of the class Movie """
    def setUp(self):
        test_movie_diction = {"api_key": tmdb_key, "query": "hercules"}
        self.testmovie = request_movie(test_movie_diction)['results'][0]

    # test if the string id are all numbers
    def test_movie_id_isdigit(self):
        test_id = Movie(self.testmovie)
        self.assertTrue(str(test_id.id).isdigit())

    def test_movie_title_istitle(self):
        test_title = Movie(self.testmovie)
        self.assertEqual(test_title.title, 'Hercules')

    def test_movie_releasedate(self):
        test_release = Movie(self.testmovie)
        self.assertEqual(test_release.release, '2014-07-23')

    def test_movie_genre(self):
        test_genre = Movie(self.testmovie)
        self.assertTrue(type(test_genre.genre), list)

    def test_movie_plot(self):
        test_plot = Movie(self.testmovie)
        self.assertTrue(type(test_plot.plot), str)

    def test_if_title_is_not_a_key(self):
        test_empty = Movie({"name":''})
        self.assertTrue(test_empty.title, 'None')

class test_requests_from_API(unittest.TestCase):
    """ This is to test requesting API """
    def setUp(self):
        self.test_response = "bhfbjnfdjkns"
        self.test_movie = "moana"

    def test_movie_dict_response_if_invalid_input(self):
        test_movie_dict = movie_dict(self.test_response)
        self.assertEqual(test_movie_dict, None)

    def test_tastedive_API_if_invalid_input(self):
        tastedive_test = tastedive_rec(self.test_response + "," + self.test_response)
        self.assertEqual(tastedive_test, None)

    def test_movie_dict_return_list(self):
        movie_dict_return = movie_dict(self.test_movie)
        self.assertTrue(movie_dict_return, list)

    def test_request_genreID_returns_dict(self):
        genreID_return = request_genreID()
        self.assertIn('id', str(genreID_return[0].keys()))
        self.assertIn('name', str(genreID_return[0].keys()))

class test_cache(unittest.TestCase):
    """ This will check the cache file """
    def test_if_TMDB_unique_id_exist(self):
        test_unique_params = {"api_key": tmdb_key, "query": "hercules"}
        test_unique_site = 'https://api.themoviedb.org/3/search/movie'
        check_cache(test_unique_site,test_unique_params)
        test_unique = test_unique_site + str(test_unique_params)
        self.assertIn(test_unique.upper(), cache.cache_diction)

    def test_if_TASTEDIVE_unique_id_exist(self):
        test_TD_site = "https://tastedive.com/api/similar"
        test_TD_params = {"q": "movie:" + "hercules,moana", "type": "movies", "k": taste_dive_key}
        check_cache(test_TD_site,test_TD_params)
        test_TD_unique = test_TD_site + str(test_TD_params)
        self.assertIn(test_TD_unique.upper(), cache.cache_diction)

class test_genre_sort(unittest.TestCase):
    """ This will test the sorting of recommendations using number of genres """
    # test if the sorting is in descending order and it returns the correct title

    def test_sort_order(self):
        test_genre_dict = {"Movie Genre 3": [1, ["genre2"]], "Movie Genre 1": [3, ["genre4", "genre1", "genre2"]], "Movie Genre 2": [2, ["genre1", "genre2"]]}
        test_sort = sort_genre_count(test_genre_dict)
        self.assertEqual(test_sort, ["Movie Genre 1", "Movie Genre 2", "Movie Genre 3"])


if __name__ == '__main__':
    unittest.main(verbosity = 2)
