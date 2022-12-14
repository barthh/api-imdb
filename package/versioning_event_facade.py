# Import requests event
from .imdb_requests_event import IMDBRequest

# Import versioning facade events
from .imdb_search_movies import SearchMoviesEvent
from .imdb_search_series import SearchSeriesEvent
from .imdb_search_all import SearchAllEvent
from .imdb_info_advanced import AdvancedEvent
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
    def title_advanced(id:str) -> [AdvancedEvent]:
        """Get the IMDb informations of a specific title.

        Input:
        - id: the movie id.

        Onput:
        - An object.
        """
        event = IMDBRequest.title_advanced(id).content

        versioning_event = AdvancedEvent(
            title = event["title"],
            year = event["year"],
            image = event["image"],
            releaseDate = event["releaseDate"],
            time = event["runtimeStr"],
            plot = event["plot"],
            genres = event["genres"],
            ratings = event["ratings"],
            directors = event["directors"],
            writers = event["writers"],
            stars = event["stars"],
            keywords = event["keywords"],
            similars = event["similars"],
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
        events = IMDBRequest.search_movies(research)

        versioning_events = []

        if events.content:
            for event in events.content:
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
        events = IMDBRequest.search_series(research).content
            
        versioning_events = []

        for event in events:
            versioning_event = SearchSeriesEvent(
                id = event['id'],
                image = event['image'],
                title = event['title'],
                description = event['description']
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
            
        versioning_events = []

        for event in events:
            versioning_event = SearchAllEvent(
                id = event['id'],
                type = event['resultType'],
                image = event['image'],
                title = event['title'],
                description = event['description'],
                errorMessage = event['errorMessage'],
                )
            versioning_events.append(versioning_event)
            
        return versioning_events