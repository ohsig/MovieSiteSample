import media
import fresh_tomatoes

the_godfather = media.Movie("The Godfather",
                        "Never let anyone outside the family know what you're thinking.",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")
avatar = media.Movie("Tron",
                     "In the future video game battles will be a matter of life or death.",
                     "https://upload.wikimedia.org/wikipedia/en/1/17/Tron_poster.jpg",
                     "https://www.youtube.com/watch?v=3efV2wqEjEY")
empire_strikes_back = media.Movie("Star Wars: The Empire Strikes Back",
                                  "You know the Empire?....well, they strike back.",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=xESiohGGP7g")
wall_e = media.Movie("Wall-E",
                     "A cautionary tale that you should clean your room.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                     "https://www.youtube.com/watch?v=ZisWjdjs-gM")
blues_brothers = media.Movie("The Blues Brothers",
                             "It's 106 miles to Chicago, we got a full tank of gas, half a pack of cigarettes, it's dark and we're wearing sunglasses.",
                             "https://upload.wikimedia.org/wikipedia/en/a/ae/Bluesbrothersmovieposter.jpg",
                             "https://www.youtube.com/watch?v=A-xtJYIwfYo")
dark_knight = media.Movie("The Dark Knight",
                          "The Joker wreaks havoc and chaos on the people of Gotham. Batman responds.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [the_godfather,avatar,empire_strikes_back,wall_e,blues_brothers,dark_knight]
fresh_tomatoes.open_movies_page(movies)
