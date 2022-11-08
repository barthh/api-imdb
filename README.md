What Is This?
-------------

This is a simple Python/Flask application intended to provide movie rating of IMDb's external API.

How To Use This
---------------

1. Navigate over to [IMDb's API website](https://imdb-api.com), sign up and go to the profile section to get a API token.
1. Clone the repository :
    ```
    https://github.com/barthh/api-imdb.git
    cd api-imdb
    ```
1. Put your API token in a ```.env``` file :
    ```sh
    export API_token=thisismyAPItoken
    ```
1. Create a virtual environment :
    ```python
    pipenv install
    ```
    > If you miss the module :
    >```python
    >pip install pipenv
    >```

1. Run the app :
    ```python
    pipenv run python3 app.py
    ```
1. Navigate to http://127.0.0.1:5000/ in your browser

Other
---------------

The token allows 100 requests each day

This README isn't finished
