# main.py
from package import versioning_event_facade

# Define test here
def test_score():
    title_rating = versioning_event_facade.RatingsEvent("leon the","leon the professional","8.5","")

    assert title_rating.title == "leon the"
    assert title_rating.fullTitle == "leon the professional"
    assert title_rating.rating == "8.5"
    assert title_rating.errorMessage == ""