class Stats():
    def __init__(self):
        self.run_game = True
        self.reset_stats()

    def reset_stats(self):
        "Определяет кол-во жизней"
        self.guns_left = 1
        self.score = 0