"""
Import library for generating HTML pages
Import library for Movie class
"""
import fresh_tomatoes    # module to render movies
import media			# module with classes for movies
"""
Initialize some favorite movies to be rendered, and put them in a list
Few instances of Movie class created
"""

brightburn = media.Movie(
    "Brightburn",
    "https://www.movieinsider.com/images/p/600/500713_m1544538453.jpg",
    "https://www.youtube.com/watch?v=6Ui6m_eEEOI",
    "David Yarovesky",
    "Elizabeth Banks, David Denman, Jackson A. Dunn, Matt Jones",
    "May 24, 2019 (United States)"
    )
polar = media.Movie(
    "Polar",
    "https://upload.wikimedia.org/wikipedia/en/0/07/" +
    "Polar%2C_Came_from_the_Cold.png",
    "https://www.youtube.com/watch?v=A9Pu2tRtzX4",
    "Jonas Akerlund",
    "Mads Mikkelsen ,Vanessa Hudgens,Katheryn Winnick,Matt Lucas",
    "January 25, 2019 (United States)"
    )
captain_marvel = media.Movie(
    "Captain Marvel",
    "https://upload.wikimedia.org/wikipedia/en/8/85/Captain_Marvel_poster.jpg",
    "https://www.youtube.com/watch?v=jr8f40dDSxI",
    "Anna Boden,Ryan Fleck",
    "Brie Larson,Samuel L. Jackson,Ben Mendelsohn,Djimon Hounsou,Lee Pace",
    "March 8, 2019 (United States)"
    )
close = media.Movie(
    "Close",
    "https://m.media-amazon.com/images/M/MV5BYzI5OTUzZjktMDE4Zi00YjE3LWIz" +
    "NWQtNDjZWQyMDVkY2I1XkEyXkFqcGdeQXVyMTg1MzYyMzQ@._V1_QL50_SY1000_" +
    "SX664_AL_.jpg",
    "https://www.youtube.com/watch?v=0mrottDo_0M",
    "Vicky Jewson",
    "Noomi Rapace, Sophie Nelisse, Eoin Macken, Indira Varma, Mimi Keene",
    "January 18, 2019 (United Kingdom)"
    )
the_secret_life_of_pets2 = media.Movie(
    "The Secret Life of Pets 2",
    "https://upload.wikimedia.org/wikipedia/en/b/b1/The_Secret_Life_of_Pets_" +
    "2_%282019%29_Teaser_Poster.jpg",
    "https://www.youtube.com/watch?v=pKLGUuJftl0",
    "Chris Renaud",
    "Patton Oswalt,Eric Stonestreet,Kevin Hart,Jenny Slate,Ellie Kemper",
    "June 7, 2019 (United States)"
    )
the_prodigy = media.Movie(
    "THE PRODIGY",
    "http://www.impawards.com/2019/posters/prodigy_xlg.jpg",
    "https://www.youtube.com/watch?v=9SGxWmtn9Yg",
    "Nicholas McCarthy",
    "Taylor Schilling,Jackson Robert Scott,Colm Feore",
    "February 8, 2019 (United States)"
    )
happy_death_day_2u = media.Movie(
    "HAPPY DEATH DAY 2U",
    "https://upload.wikimedia.org/wikipedia/en/e/ef/" +
    "Happy_Death_Day_2U_promo_poster.jpg",
    "https://www.youtube.com/watch?v=tiWyTaD-aKA",
    "Christopher Landon",
    "Jessica Rothe,Israel Broussard,Phi Vu,Suraj Sharma,Sarah Yarkin",
    "February 14, 2019 (United States)"
    )

# Create a list of all movies to use in the web page
movies = [
    brightburn,
    polar,
    captain_marvel,
    close,
    the_secret_life_of_pets2,
    the_prodigy,
    happy_death_day_2u
    ]

# Let the list of movies render on a webpage and open it in the web browser
fresh_tomatoes.open_movies_page(movies)
