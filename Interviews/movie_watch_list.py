# // 1. Build a digital representation of a movie, where a movie has a
# // title and an optional rating between 1-5. Also add a way to rate a movie later.

# // 2. Build a watch list of movies.
# //   Functionality:
# //   - Add movies
# //   - Get the next unwatched movie in the list and set that movie as watched
# //   - Display a list of all movies on list and their watched statuses and ratings.

# // 3. Build a function that takes a list of movies and builds a frequency distribution of each possible rating (1-5).
# //   -  Example: 3 movies rated as 1, 2 rated as 2, etc…

# 4. Add movie categories.
# Movies can have multiple categories.
# List of categories: Romance, Scifi, History, Action, Kids

# 5. Add a function that returns the users favorite category based on highest
# average ratings per category from already watched movies.

from typing import Optional, List
from collections import defaultdict

MIN_RATING = 1
MAX_RATING = 5


class Movie:
    def __init__(
        self,
        title: str,
        rating: Optional[int] = None,
        watched: bool = False,
        categories: List[str] = [],
    ):
        self.title = title
        self.rating = rating
        self.watched = watched
        self.categories = categories
        self.check_rating(rating)

    def check_rating(self, rating) -> bool:
        if rating:
            if rating < MIN_RATING or rating > MAX_RATING:
                raise Exception("Invalid rating")

        return True

    def set_rating(self, rating: int):
        self.check_rating(rating)
        self.rating = rating


class WatchList:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def get_next_unwatched(self) -> Optional[Movie]:
        for movie in self.movies:
            if not movie.watched:
                movie.watched = True
                return movie

    def get_favorite_categories(self) -> List[tuple]:
        category_ratings = defaultdict(list)

        for movie in self.movies:
            if movie.watched and movie.rating:
                for category in movie.categories:
                    category_ratings[category].append(movie.rating)

        average_ratings = {
            category: sum(ratings) / len(ratings)
            for category, ratings in category_ratings.items()
            if ratings
        }

        # Sort categories by average rating in descending order
        sorted_categories = sorted(
            average_ratings.items(), key=lambda x: x[1], reverse=True
        )

        return sorted_categories

    def print_movies(self):
        print("Title \t Rating \t Watched")
        for movie in self.movies:
            watched = "Watched" if movie.watched else "Unwatched"
            rating = str(movie.rating) if movie.rating else "None"
            print(movie.title + "\t" + rating + "\t" + watched)

    def print_movies_2(self):
        if not self.movies:
            print("No movies in the list.")
            return

        # Calculate column widths
        title_width = max(len(movie.title) for movie in self.movies)
        title_width = max(
            title_width, len("Title")
        )  # At least as wide as header

        rating_width = max(
            len(str(movie.rating) if movie.rating else "None")
            for movie in self.movies
        )
        rating_width = max(rating_width, len("Rating"))

        watched_width = max(len("Watched"), len("Unwatched"))

        # Print header
        print(
            f"{'Title':<{title_width}} {'Rating':<{rating_width}} {'Watched':<{watched_width}}"
        )
        print(
            "-" * (title_width + rating_width + watched_width + 4)
        )  # +4 for spaces

        # Print movies
        for movie in self.movies:
            watched = "Watched" if movie.watched else "Unwatched"
            rating = str(movie.rating) if movie.rating else "None"
            print(
                f"{movie.title:<{title_width}} {rating:<{rating_width}} {watched:<{watched_width}}"
            )


def rating_distribution(
    movies: list[Movie], print_output: bool = True
) -> dict:
    ratings = defaultdict(int)

    for movie in movies:
        if not movie.rating:
            ratings[0] += 1
        else:
            ratings[movie.rating] += 1

    if print_output:
        print("Rating Distribution:")
        for rating in range(MIN_RATING, MAX_RATING + 1):
            count = ratings[rating]
            print(f"{count} movies rated {rating}")
        print(f"{ratings[0]} movies unrated")

    return ratings


movie1 = Movie(
    "movie1", rating=1, watched=False, categories=["Action", "Scifi"]
)
movie2 = Movie(
    "movie2", rating=2, watched=False, categories=["Romance", "Comedy"]
)
movie3 = Movie("movie3", rating=3, watched=True, categories=["Comedy"])
movie4 = Movie("movie4", rating=None, watched=False, categories=[])
movie5 = Movie("movie5", rating=None, watched=False, categories=["Scifi"])

watch_list = WatchList()
watch_list.add_movie(movie1)
watch_list.add_movie(movie2)
watch_list.add_movie(movie3)
watch_list.add_movie(movie4)
watch_list.add_movie(movie5)

assert watch_list.get_next_unwatched().title == "movie1"
assert watch_list.get_next_unwatched().title == "movie2"
assert watch_list.get_next_unwatched().title == "movie4"

watch_list.print_movies()
watch_list.print_movies_2()

distribution = rating_distribution(
    [movie1, movie2, movie3, movie4, movie5], print_output=True
)
assert distribution[0] == 2
assert distribution[1] == 1
assert distribution[2] == 1
assert distribution[3] == 1
assert distribution[4] == 0
assert distribution[5] == 0

try:
    movie_inv = Movie("movie_err", rating=6, watched=False)
except Exception as e:
    assert str(e) == "Invalid rating"


def print_categories(categories: List[tuple[str, float]]):
    print(f"{'Category':<20} {'Average Rating':<10}")
    for category, avg_rating in categories:
        print(f"{category:<20} {avg_rating:<10.2f}")


fav_categories = watch_list.get_favorite_categories()

print_categories(fav_categories)

assert fav_categories[0] == ("Comedy", 2.5)
assert fav_categories[1] == ("Romance", 2.00)
assert fav_categories[2] == ("Action", 1.0)
assert fav_categories[3] == ("Scifi", 1.0)

watch_list.add_movie(
    Movie("movie6", rating=5, watched=True, categories=["Action"])
)
fav_categories = watch_list.get_favorite_categories()
print_categories(fav_categories)

assert fav_categories[0] == ("Action", 3.0)
assert fav_categories[1] == ("Comedy", 2.5)
assert fav_categories[2] == ("Romance", 2)
