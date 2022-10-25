# final-work

First, put your API token in .env file.
```python
export API_token=thisismyAPItoken
```

Install a module :
```bash
pip install python-dotenv
```


Then, in python file, you need to import os library :
```python
import os
```

And get the token like this :
```python
api_token = os.environ["API_token"]
```