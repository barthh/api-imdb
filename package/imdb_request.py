import requests
import os
from dotenv import load_dotenv

class IMDBRequest:
    load_dotenv()
    token = os.getenv("API_token")
    _base_url = "https://imdb-api.com/en/API/"

    @classmethod
    def search_movie_rating(cls, movie:str):
        movie_id = IMDBRequest.__search_movie_id(movie).content
        response =  requests.get(
            cls._base_url
            + "Ratings/"
            + cls.token 
            + "/" 
            + movie_id
            )
        return Response(status_code = response.status_code, content = response.json())
        
    @classmethod
    def __search_movie_id(cls, movie:str):
        response =  requests.get(
            cls._base_url
            + "SearchMovie/"
            + cls.token
            + "/"
            + movie
            )
        return Response(status_code = response.status_code, content = response.json()['results'][0]["id"])


class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content