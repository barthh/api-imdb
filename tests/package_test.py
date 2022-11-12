import pytest
from package import versioning_event_facade
from package import imdb_requests_event
from app import app # Flask instance of the API


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200


def test_score():
    title_rating = versioning_event_facade.RatingsEvent("leon the","leon the professional","8.5","")
    assert title_rating.title == "leon the"
    assert title_rating.fullTitle == "leon the professional"
    assert title_rating.rating == "8.5"
    assert title_rating.errorMessage == ""

def test_APIKey():
    APIkey_message = imdb_requests_event.IMDBRequest.search_movies("leon").errorMessage
    assert APIkey_message == ""