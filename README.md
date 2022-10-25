# final-work

For the API token, create .env file and put this inside :

```python
export GITHUB_TOKEN=thisismyAPItoken
```

In python file you need to import os library :
```python
import os
```

And get the token like this :
```python
github_token = os.environ["GITHUB_TOKEN"]
```