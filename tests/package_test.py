# main.py
import package

# Define test here

def test():
    assert package.VersioningEventFacade.get_rating("leon the professional").imdb_score == '8.5'