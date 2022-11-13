
# Find Movie Ratings App

[![Contributors][contributors-shield]][contributors-url]
[![Dimitri][linkedin-dimitri-shield]][linkedin-dimitri-url]
[![Barth][linkedin-barthh-shield]][linkedin-barthh-url]

This app is a school project to learn how to retrieve data from an api, exploit it and make versioning code 

<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ul>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#content">Content</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ul>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This app allows you to find information about a movie as well as its notes. The data comes from the [IMDb API website](https://imdb-api.com). The project is built with [python 3.9](https://docs.python.org/3.9/) and the [Flask framework](https://flask.palletsprojects.com/en/2.2.x/).


Here is an overview : 
![[Search a Movie]](./images/search_a_movie.png)
![[Search a Movie]](./images/movie_informations.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Content

Usefull content table :

| Template name | Description |
| ------------- | ----------- |
| [App folder](./app/) | The website app |
| [Package folder](./package/) | Package to get the data from IMDb API |
| [Tests folder](./tests/) | Some package tests |
| [app.py](./app.py) |  The file to launch the app |

### Built With

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need at [python 3.9](https://docs.python.org/3.9/) to run this project.

### Installation

_Below are the instructions_

1. Clone the repository :
    ```
    https://github.com/barthh/api-imdb.git
    cd api-imdb
    ```
1. Navigate over to [IMDb's API website](https://imdb-api.com), sign up and go to the profile section to get a API token.
  
1. Put your API token in a ```.env``` file :
    ```sh
    export API_token=thisismyAPItoken
    ```
1. Create a virtual environment :
    ```python
    pipenv install
    ```
    > If you are missing the module, install it according to your system : [Get commands](https://pypi.org/project/pipenv/#installation)

2. Run the app :
    ```python
    pipenv run python3 app.py
    ```
3. Navigate to http://127.0.0.1:5000/ in your browser
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can search for a movie or a series from the site menu.
You will be redirected to a list of movies/series that best match your search.
Select the one you want.
You will be taken to a page that contains information about the selected movie/series.
In the navigation bar you can go back to the main menu or in the movie search or the series search.

Here are some additional features:

- If the user goes to a link not found, a 404 error is displayed. 
- If the user's key has reached its daily limit (100 uses), an error is displayed.
- If no movie/serie was found, the user will be notified.
- If the movie/serie has no information, the user will be notified.
- If the movie/serie does not have a cover image, a template image is displayed


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/barthh/api-imdb.svg?style=for-the-badge
[contributors-url]: https://github.com/barthh/api-imdb/graphs/contributors

[linkedin-dimitri-shield]: https://img.shields.io/badge/-Dimitri-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-dimitri-url]: https://www.linkedin.com/in/dimitri-prieur/

[linkedin-barthh-shield]: https://img.shields.io/badge/-Barthelemy-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-barthh-url]: https://www.linkedin.com/in/https://www.linkedin.com/in/barthh/

[Flask]:https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=ffffff
[Flask-url]:https://flask.palletsprojects.com/en/2.2.x/

[Python]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=FFD43B
[Python-url]:https://www.python.org/

[product-screenshot]: images/screen1.png