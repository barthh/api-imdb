from package.imdb_requests import IMDBRequest
from package.imdb_movies_event import MoviesEvent
from package.imdb_ratings_event import RatingEvent
from package.imdb_series_event import SeriesEvent
class VersioningEventFacade:

    @staticmethod
    def get_rating(id:str) -> [RatingEvent]:
        """Get the IMDb rating of a specific movie.

        Input:
        - id: the movie id.

        Onput:
        - An object.
        """
        event = IMDBRequest.search_rating(id).content
        versioning_event = RatingEvent(
            title = event["title"],
            fullTitle = event["fullTitle"],
            rating = event["imDb"],
            )
        return versioning_event
    

    @staticmethod
    def get_movies(movie:str) -> [MoviesEvent]:
        """Get movies related to a research.

        Input:
        - movie: a string containing the user search.

        Onput:
        - A list of objects. 
        """
        events = IMDBRequest.search_movies(movie).content

        if events is None :
            return None 
            
        versioning_events = []
        for event in events:
            versioning_event = MoviesEvent(
                id = event['id'],
                title = event['title'],
                description = event['description'],
                )
            versioning_events.append(versioning_event)
        return versioning_events


    @staticmethod
    def get_series(serie:str) -> [SeriesEvent]:
        """Get series related to a research.

        Input:
        - serie: a string containing the user search.

        Onput:
        - A list of objects. 
        """
        events = IMDBRequest.search_movies(serie).content

        if events is None :
            return None 
            
        versioning_events = []
        for event in events:
            versioning_event = MoviesEvent(
                id = event['id'],
                title = event['title'],
                description = event['description'],
                )
            versioning_events.append(versioning_event)
        return versioning_events