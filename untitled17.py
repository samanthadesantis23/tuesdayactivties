class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        # Create a string for the genres
        genre_string = ", ".join(self.genres)
        
        # If there are ratings, calculate the average and count
        if self.ratings:
            average_rating = sum(self.ratings) / len(self.ratings)
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{len(self.ratings)} ratings, average {average_rating:.1f} points"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"

    def rate(self, rating: int):
        # Add a rating (must be between 0 and 5)
        if 0 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating! Rating must be between 0 and 5.")

def minimum_grade(rating: float, series_list: list):
    # Return series with average ratings >= the given rating
    return [series for series in series_list if (sum(series.ratings) / len(series.ratings) if series.ratings else 0) >= rating]

def includes_genre(genre: str, series_list: list):
    # Return series that include the given genre
    return [series for series in series_list if genre in series.genres]

# Example usage
if __name__ == "__main__":
    # Create series instances
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(4)
    s1.rate(5)
    s1.rate(5)
    s1.rate(3)
    s1.rate(0)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum rating of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
