# main.py
import package



# versioning_events = package.VersioningEventFacade.get_movie_ratings("leon the professional")
# print(versioning_events)

versioning_events = package.VersioningEventFacade.get_movies("inception")

id = versioning_events[0].id
print("Movie selected :", versioning_events[0].title)
print("His ID :", id)

versioning_events = package.VersioningEventFacade.get_rating(id)
print("Title :",versioning_events.fullTitle)
print("Rating :",versioning_events.rating)
