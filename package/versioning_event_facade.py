from .imdb_requests_event import IMDBRequest

from .imdb_search_movies import SearchMoviesEvent
from .imdb_search_series import SearchSeriesEvent
from .imdb_search_all import SearchAllEvent

from .imdb_info_ratings import RatingsEvent

class VersioningEventFacade:

    @staticmethod
    def title_ratings(id:str) -> [RatingsEvent]:
        """Get the IMDb ratings of a specific title.

        Input:
        - id: the movie id.

        Onput:
        - An object.
        """
        event = IMDBRequest.title_ratings(id).content

        versioning_event = RatingsEvent(
            title = event["title"],
            fullTitle = event["fullTitle"],
            rating = event["imDb"],
            errorMessage = event["errorMessage"],
            )
        return versioning_event
    

    @staticmethod
    def search_movies(research:str) -> [SearchMoviesEvent]:
        """Search movies related to a research.

        Input:
        - movie: a string containing the user search.

        Onput:
        - A list of objects. 
        """
        events = IMDBRequest.search_movies(research).content

        if not events:
            return None 
            
        versioning_events = []
        for event in events:
            versioning_event = SearchMoviesEvent(
                id = event['id'],
                image = event['image'],
                title = event['title'],
                description = event['description'],
                )
            versioning_events.append(versioning_event)
        return versioning_events


    @staticmethod
    def search_series(research:str) -> [SearchSeriesEvent]:
        """Search series related to a research.

        Input:
        - serie: a string containing the user search.

        Onput:
        - A list of objects. 
        """
        events = IMDBRequest.search_movies(research).content

        if not events:
            return None 
            
        versioning_events = []
        for event in events:
            versioning_event = SearchSeriesEvent(
                id = event['id'],
                image = event['image'],
                title = event['title'],
                description = event['description'],
                )
            versioning_events.append(versioning_event)
        return versioning_events
    
    @staticmethod
    def search_all(research:str) -> [SearchAllEvent]:
        """Search into all items (Movies, Series TVs, TV Episodes, Names, Companies, Keywords and more).

        Input:
        - serie: a string containing the user search.

        Onput:
        - A list of objects. 
        """
        events = IMDBRequest.search_all(research).content

        if not events:
            return None 
            
        versioning_events = []
        for event in events:
            versioning_event = SearchAllEvent(
                id = event['id'],
                type = event['resultType'],
                image = event['image'],
                title = event['title'],
                description = event['description'],
                )
            versioning_events.append(versioning_event)
        return versioning_events