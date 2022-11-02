import requests
import os
from dotenv import load_dotenv
import json

class IMDBRequest:
    load_dotenv()
    token = os.getenv("API_token")
    _base_url = "https://imdb-api.com/en/API/"

    # Use local json requests
    _local_mode = False

    @classmethod
    def search_rating(cls, movie_id:str):
        # if(cls._local_mode):
        #     # Opening local JSON file
        #     f = open('./package/request6.json', "r")
        #     print("Get local json for rating")
        #     response = json.load(f)
        #     f.close()
        #     return Response(status_code = "json loaded", content = response)
        
        # else:
            response = requests.get(
                cls._base_url
                + "Ratings/"
                + cls.token 
                + "/" 
                + movie_id
                )
            return Response(status_code = response.status_code, content = response.json())
        
    @classmethod
    def search_movies(cls, movie:str):
        # if(cls._local_mode):
        #     # Opening local JSON file
        #     f = open('./package/request5.json', "r")
        #     print("Get local json for movies")
        #     response = json.load(f)
        #     f.close()
        #     return Response(status_code = "json loaded", content = response['results'])

        # else:
            print("Request for movies")
            response =  requests.get(
                cls._base_url
                + "SearchMovie/"
                + cls.token
                + "/"
                + movie
            )
            return Response(status_code = response.status_code, content = response.json()['results'])
        

class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content