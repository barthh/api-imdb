# main.py
import package

def test_answer():
    assert package.VersioningEventFacade.get_movie_ratings("leon the professional").imdb_score == '8.5'