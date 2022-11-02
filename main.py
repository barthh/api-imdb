# main.py
import package



# versioning_events = package.VersioningEventFacade.get_movie_ratings("leon the professional")
# print(versioning_events)

# versioning_events = package.VersioningEventFacade.get_movies("inception")
# # for versioning_event in versioning_events:
# #     assert isinstance(versioning_event, package.VersioningEvent)
# # print(versioning_events)

# for versioning_event in versioning_events:
#     print(versioning_event.id, versioning_event.title, versioning_event.description)


versioning_events = package.VersioningEventFacade.get_rating("inception")

print(versioning_events.fullTitle, versioning_events.rating)
# print("ok")
# I cant now work with Python Objects