class Game:

    def play(self):
        print("The game has started!")

    def end_play(self):
        print("The game has ended!")


class Football(Game):

    def play(self):
        print("Football has started")

    def end_play(self):
        print("Football has ended")


class Cricket(Game):

    def play(self):
        print("Cricket has started")

    def end_play(self):
        print("Cricket has ended")

game = Football()
game.play()
game = Cricket()
game.play()
