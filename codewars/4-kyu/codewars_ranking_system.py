class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def rank_index(self, rank):
        return self.ranks.index(rank)

    def inc_progress(self, act_rank):
        print(self.progress)
        if act_rank not in self.ranks:
            raise Exception("Invalid rank")

        user_rank_index = self.rank_index(self.rank)
        activity_rank_index = self.rank_index(act_rank)

        d = activity_rank_index - user_rank_index

        if d == 0:
            self.progress += 3
        elif d == -1:
            self.progress += 1
        elif d > 0:
            self.progress += 10 * d * d

        self.update_rank()
        print(self.progress)

    def update_rank(self):
        while self.progress >= 100 and self.rank != 8:
            self.progress -= 100
            user_rank_index = self.rank_index(self.rank)
            self.rank = self.ranks[user_rank_index + 1]

        if self.rank == 8:
            self.progress = 0

