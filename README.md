What Is This?
-------------

This is a simple Python/Flask application intended to provide movie rating of IMDb's external API.

How To Use This
---------------

1. Navigate over to [IMDb's API website](https://imdb-api.com), sign up and go to the profile section to get a API token.
1. Clone the repository :
    ```
    https://github.com/barthh/api-imdb.git
    ```
1. Put your API token in a ```.env``` file :
    ```sh
    export API_token=thisismyAPItoken
    ```
1. Create a virtual environment :
    ```python
    python3 -m venv .venv
    ```
    > If you miss the module :
    >```python
    >pip install virtualenv
    >```
    And activate the environment
    ```sh
    source .venv/bin/activate
    ```
1. Install modules :
    ```python
    pip install -r requirements.txt
    ```
1. Run the app :
    ```python
    python app.py
    ```
1. Navigate to http://127.0.0.1:5000/ in your browser

/!\  The token allows 100 requests each day
