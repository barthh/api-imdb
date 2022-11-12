class Response:
    
    def __init__(self, status_code, content, errorMessage):
        self.status_code = status_code
        self.content = content
        self.errorMessage = errorMessage