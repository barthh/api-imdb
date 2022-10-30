# main.py
import package

versioning_events = package.VersioningEventFacade.get_movie_ratings("leon the professional")
# print(versioning_events)

# for versioning_event in versioning_events:
#     assert isinstance(versioning_event, package.VersioningEvent)

print(versioning_events.imdb_score)
print("ok")
# I cant now work with Python Objects