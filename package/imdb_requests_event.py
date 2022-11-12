import requests
import os
from dotenv import load_dotenv
import json
from .response import Response


class IMDBRequest:
    
    
    load_dotenv()
    _token = os.getenv("API_token")
    _base_url = "https://imdb-api.com/en/API/"
    _local_mode = True

    # Search ratings for a specific id
    @classmethod
    def title_ratings(cls, movie_id:str):
            response = requests.get(
                cls._base_url
                + "Ratings/"
                + cls._token 
                + "/" 
                + movie_id
                )
            return Response(status_code = response.status_code, content = response.json(), errorMessage = response.json()["errorMessage"])

    # Search lots of informations for a specific id
    @classmethod
    def title_advanced(cls, movie_id:str):
        if(cls._local_mode):
            # Opening local JSON file
            f = open('./package/local_jsons/requests_basic/Advanced_search.json', "r")
            response = json.load(f)
            f.close()
            return Response(status_code = "json loaded",content = response['results'])
        else:
            response =  requests.get(
                cls._base_url
                + "Title/"
                + cls._token
                + "/"
                + movie_id
                + "/Ratings,"
            )
            return Response(status_code = response.status_code, content = response.json()['results'], errorMessage = response.json()["errorMessage"])

    # Search for movies only
    @classmethod
    def search_movies(cls, movie:str):
            response =  requests.get(
                cls._base_url
                + "SearchMovie/"
                + cls._token
                + "/"
                + movie
            )
            return Response(status_code = response.status_code, content = response.json()['results'], errorMessage = response.json()["errorMessage"])

    # Search for series only    
    @classmethod
    def search_series(cls, serie:str):
            response =  requests.get(
                cls._base_url
                + "SearchSeries/"
                + cls._token
                + "/"
                + serie
            )
            return Response(status_code = response.status_code, content = response.json()['results'], errorMessage = response.json()["errorMessage"])

    # Search for main result for a search (Main titles, actores, company, keywords...)
    @classmethod
    def search_all(cls, serie:str):
            response =  requests.get(
                cls._base_url
                + "SearchAll/"
                + cls._token
                + "/"
                + serie
            )
            return Response(status_code = response.status_code, content = response.json()['results'], errorMessage = response.json()["errorMessage"])
