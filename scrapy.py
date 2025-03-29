import requests
from bs4 import BeautifulSoup

# IMDb top 250 URL
url = "https://www.imdb.com/chart/top/"

# Headers to prevent 403 errors
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Request the IMDb page
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Select all rows in the top movies table
    movies = soup.select("tbody.lister-list tr")

    top_50_movies = []

    for i, movie in enumerate(movies[:50], start=1):
        title_column = movie.select_one("td.titleColumn")
        rating_column = movie.select_one("td.ratingColumn strong")

        if title_column and rating_column:
            title = title_column.a.text.strip()  # Movie title
            year = title_column.span.text.strip("()")  # Release year
            rating = rating_column.text.strip()  # IMDb rating

            # Append only if both title and rating exist
            top_50_movies.append(f"{i}. {title} ({year}) - ⭐ {rating}")

    # Print top 50 movies (force immediate output)
    for movie in top_50_movies:
        print(movie, flush=True)  # ✅ Forces print to appear in Jupyter Notebook

else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}", flush=True)
