import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

url = "https://www.imdb.com/chart/top/"

page = requests.get(url)
page

## display the page source code (sayfa kaynak kodunu göster) ##
page.content

soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())

## scrap movie names ##
film_scraped = soup.find_all('td', class_='titleColumn')
film_scraped

## parse movie names ##
movies = []

for movie in film_scraped:
    movie = movie.get_text().replace('\n', "")
    movie = movie.strip(" ")
    movies.append(movie)

movies

## get rating for movies ##

rating_scraped = soup.find_all('td', class_="ratingColumn imdbRating")
rating_scraped

## parse rating movies ##
ratings = []

for rating in rating_scraped:
    rating = rating.get_text().replace('\n', "")
    ratings.append(rating)

ratings

## converting to data ##

df = pd.DataFrame()
df["Movie Names"] = movies
df["Ratings"] = ratings
df.head()

df.head(250)

df.to_csv("IMDB Top 250 Movies.csv", index=False)