from package.imdb_request import IMDBRequest
from package.versioning_event import VersioningEvent

class VersioningEventFacade:

    @staticmethod
    def get_movie_ratings(movie:str) -> [VersioningEvent]:

        event = IMDBRequest.search_movie_rating(movie).content

        versioning_event = VersioningEvent(
            fullTitle = event["fullTitle"],
            imdb_score = event["imDb"])

        return versioning_event