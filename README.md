# final-work

1. Get a free API Key at [IMDb API website](https://imdb-api.com)

1. Clone the repository
    ```
    https://github.com/barthh/api-imdb.git
    ```

1. Put your API token in a .env file.
    ```sh
    export API_token=thisismyAPItoken
    ```

1. Create a virtual environment

    ```python
    python3 -m venv .venv
    ```

    > If you miss the module :
    >```python
    >pip install virtualenv
    >```

    Activate the environment
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

