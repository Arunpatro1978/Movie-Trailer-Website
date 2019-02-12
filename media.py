"""
Define the Movie class
"""


# Movie class object to store movie related information
class Movie():
    """
    Initialize an instance of the Movie class
    :param movie_title: string
    :param movie_artwork: string
    :param movie_trailer_url: string
    :param directed_by: string
    :param starring: string
    : release_date: string
    """
    def __init__(
        self,
        movie_title,
        movie_artwork,
        movie_trailer_url,
        directed_by,
        starring,
        release_date
    ):
        self.title = movie_title
        self.poster_image_url = movie_artwork
        self.trailer_youtube_url = movie_trailer_url
        self.directed_by = directed_by
        self.starring = starring
        self.release_date = release_date
