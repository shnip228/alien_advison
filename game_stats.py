import os.path


class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.stats_file_path = os.path.join(self.settings.app_path,
                                            'data/stats/stats.txt')
        if not os.path.exists(self.stats_file_path):
            self.high_score = 0
        else:
            stats_file = open(self.stats_file_path, "r", encoding='utf-8')
            self.high_score = float(stats_file.readline())
            stats_file.close()
        self.reset_status()
        self.game_active = False

    def reset_status(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        stats_file = open(self.stats_file_path, "w", encoding='utf-8')
        print(self.high_score, file=stats_file)
        stats_file.close()
