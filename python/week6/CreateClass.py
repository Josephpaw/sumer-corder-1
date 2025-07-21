class EntertainmentList:
    def __init__(self):
        self.movie_list = []
        self.game_list = []
        self.fave_movie = None
        self.fave_game = None

    def add_movie(self, movie):
        if movie not in self.movie_list:
            self.movie_list.append(movie)
            print(f"Added movie: {movie}")
        else:
            print(f"Movie '{movie}' already in list.")

    def add_game(self, game):
        if game not in self.game_list:
            self.game_list.append(game)
            print(f"Added game: {game}")
        else:
            print(f"Game '{game}' already in list.")

    def set_fave_movie(self, movie):
        if movie in self.movie_list:
            self.fave_movie = movie
            print(f"Favorite movie set to: {movie}")
        else:
            print(f"Movie '{movie}' not found in movie list. Add it first.")

    def set_fave_game(self, game):
        if game in self.game_list:
            self.fave_game = game
            print(f"Favorite game set to: {game}")
        else:
            print(f"Game '{game}' not found in game list. Add it first.")

    def get_movie_list(self):
        return self.movie_list

    def get_game_list(self):
        return self.game_list

    def get_fave_movie(self):
        return self.fave_movie

    def get_fave_game(self):
        return self.fave_game

    def display(self):
        print("Movie List:")
        if self.movie_list:
            for movie in self.movie_list:
                print(f" - {movie}")
        else:
            print(" (No movies added)")

        print("\nGame List:")
        if self.game_list:
            for game in self.game_list:
                print(f" - {game}")
        else:
            print(" (No games added)")

        print(f"\nFave Movie: {self.fave_movie if self.fave_movie else '(None set)'}")
        print(f"Fave Game: {self.fave_game if self.fave_game else '(None set)'}")