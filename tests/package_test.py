# main.py
import package

def test1():
    assert package.VersioningEventFacade.get_movie_ratings("leon the professional").imdb_score == '8.5'