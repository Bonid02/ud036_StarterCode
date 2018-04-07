import media, fresh_tomatoes, requests, sys
import sys

# Set default encoding to be able to hand utf-8 characters sent by the api response
reload(sys)
sys.setdefaultencoding('utf-8')
# List of movies to search
movie_list = ["Pacific Rim","Interstellar","Schindler's List",
              "Lord Of The Rings Fellowship Of The Ring","The Matrix", "Father Of Lights"]
movies_arr = []

# Function to call api from themoviedb.org website
# Accepts parameter movie_name from movie_list
def movie_api(movie_name):
    # API key
    api_key = "2de53ae81b4e8be4a67a8614e0fad933"
    # To query movie details run this url using the movie_name and api_key
    # This requires requests module to be imported
    response1 = requests.get("https://api.themoviedb.org/3/search/movie?api_key="
                             +api_key+"&query="+movie_name)
    # Use json function to get the json object from API
    movie_details_json = response1.json()
    # Assign value of movie_title
    movie_title = movie_details_json["results"][0]["title"]
    # Assign value of story_line
    story_line = movie_details_json["results"][0]["overview"]
    # Assign value of poster_jpg and then build the url for the poster_url
    poster_jpg = movie_details_json["results"][0]["poster_path"]
    poster_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+poster_jpg
    # Assign value of movie_id
    # Which will be used in second API call to get the youtube key
    movie_id = movie_details_json["results"][0]["id"]
    response2 = requests.get("https://api.themoviedb.org/3/movie/"+
                             str(movie_id)+"/videos?api_key="+api_key+"&language=en-US")
    # Here we get json response from API call
    video_search_json = response2.json()
    # Assign value of youtube_key
    # Which will be used to build the youtube url
    youtube_key = video_search_json["results"][0]["key"]
    youtube_url = "https://www.youtube.com/watch?v="+youtube_key
    # Instantiate the Movie() to create object using the the arguments as parameters    
    tmp_movie = media.Movie(movie_title, story_line, poster_url, youtube_url)
    # Add object to movies_arr
    movies_arr.append(tmp_movie)

# Loop thru movie_list and pass each element to the movie_api() function   
for movie_name in movie_list:
    movie_api(movie_name)

# Call fresh_tomatoes.py file and call open_movies_page() to pass the movies_arr list
fresh_tomatoes.open_movies_page(movies_arr)




