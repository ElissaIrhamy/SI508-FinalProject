ELISSA ALANNA BINTI IRHAMY
# SI508-FinalProject

Steps to run this program:

STEP 1 - Keys

Keys needed to be obtained:
1. The Movie Database API
2. Taste Dive API
These keys should be inputted in the FP_secrets.py file.

STEP 2 - Flask

Download all the files in the repository.
Run python FP_Flask.py runserver in the terminal.
All other files and libraries should already be imported.

STEP 3 - Program

1. This is a movie recommendation program. After you run FP_Flask.py, a main page asking you to input two movies should appear on your localhost:5000
2. Input two movies and click Submit. If you input a string that doesn't make sense or if a movie doesn't exist in the database, an error message will appear at the top of the main page.
3. After two successful movies are inputted, the program will produce a list containing movies with the similar name that you inputted. Choose two movies that you actually want and click Submit. If you don't choose anything and then click Submit, the default movies are the last movies in the two lists.
4. Then the program will bring you to the next page where it lists at most 10 recommended movies based on the two movies you chose.
5. There is a bonus section where you can find out if the movie you chose earlier has made a lot of money. Choose a movie and click "Show Me!". A pie chart will pop up showing the budget and revenue of the movie.
6. Exit out the pop up window and a "Thank you" message page will appear.

THE MECHANICS.

(Images of how the application looks like is in the Screenshots folder)

1. Two data sources are used for this project. The Movie Database API (for movie information including budget and revenue) and Taste Dive API (for recommendations).
2. Further filter is used  by sorting the genre of the recommended movies with the genre of the two inputted movies. The more similar genre those three movies have together, the further up the recommended movie goes up the list. In the end, only the top 10 movies are chosen to be displayed.
3. A class Movie is made to collect information about a particular movie, inputted or recommended. The Movie class has attributes such as title, plot, release date and these attributes are used in other functions.
Another class MovieNumbers is made to collect the budget, revenue and runtime of the movie.
4. All the requested response from APIs are cached in a cache file, movies.json.
5. The interactive web application is done using Flask as described above and matplotlib is used for the pie chart of budget and revenue.
6. 4 TestCase classes are made using unittest with overall 13 methods to test the program. The TestCase classes tests the class Movie and it's attributes, the requesting functions, the cache file and the sorted genre function.

Requirements checked:
1. Base Requirements
- Two data sources (TMBD and TasteDive API)
- Caching implemented in movies.json
- processed data using classes Movie and MovieNumbers
- imported matplotlib
- test file has 4 classes and 13 methods
- 2 classes Movies and MovieNumbers and used their attributes
- Interactive application
- errors handles with messages

2. Second Level Requirements
- Used matplotlib
- accessed a new REST API, TasteDive

3. Third Level Requirements
- Interactive user input
- Generated a pie chart
