class SearchSeriesEvent:

    def __init__(self, id, image, title, description, errorMessage):
        self.id = id
        self.image = image
        self.title = title
        self.description = description
        self.errorMessage = errorMessage