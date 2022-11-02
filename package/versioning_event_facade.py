from package.imdb_request import IMDBRequest
from package.movies_event import MoviesEvent
from package.rating_event import RatingEvent

class VersioningEventFacade:

    @staticmethod
    def get_rating(movie:str) -> [RatingEvent]:

        event = IMDBRequest.search_rating(movie).content
        
        versioning_event = RatingEvent(
            title = event["title"],
            fullTitle = event["fullTitle"],
            rating = event["imDb"],
            )
            
        return versioning_event
    
    @staticmethod
    def get_movies(movie:str) -> [MoviesEvent]:

        events = IMDBRequest.search_movies(movie).content

        versioning_events = []

        for event in events:
            versioning_event = MoviesEvent(
                id = event['id'],
                title = event['title'],
                description = event['description'],
                )
            versioning_events.append(versioning_event)

        return versioning_events