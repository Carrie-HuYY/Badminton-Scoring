import math

class GlickoRating:
    """
    Glicko 评分系统实现。
    """

    def __init__(self, rating=1500, rd=350, volatility=0.06):
        self.rating = rating
        self.rd = rd
        self.volatility = volatility

    def update_rating(self, opponent, result):
        """
        根据比赛结果更新评分和 RD。
        :param opponent: 对手的 GlickoRating 对象
        :param result: 比赛结果（1 为胜，0 为负）
        """
        q = math.log(10) / 400
        g_rd = 1 / math.sqrt(1 + 3 * q ** 2 * opponent.rd ** 2 / math.pi ** 2)
        expected_score = 1 / (1 + 10 ** (-g_rd * (self.rating - opponent.rating) / 400))
        d_squared = 1 / (q ** 2 * g_rd ** 2 * expected_score * (1 - expected_score))
        self.rating += q / (1 / self.rd ** 2 + 1 / d_squared) * g_rd * (result - expected_score)
        self.rd = math.sqrt((1 / self.rd ** 2 + 1 / d_squared) ** -1)

def initialize_ratings(teams):
    """
    初始化队伍的 Glicko 评分。
    :param teams: 队伍名称列表
    :return: 包含队伍评分的字典
    """
    return {team: GlickoRating() for team in teams}

def update_ratings_from_matches(ratings, matches):
    """
    根据比赛数据更新队伍评分。
    :param ratings: 包含队伍评分的字典
    :param matches: 比赛数据（DataFrame）
    """
    for _, row in matches.iterrows():
        team_A = row["team_A"]
        team_B = row["team_B"]
        winner = row["winner"]

        if winner == team_A:
            ratings[team_A].update_rating(ratings[team_B], result=1)
            ratings[team_B].update_rating(ratings[team_A], result=0)
        else:
            ratings[team_A].update_rating(ratings[team_B], result=0)
            ratings[team_B].update_rating(ratings[team_A], result=1)

if __name__ == "__main__":
    # 示例：初始化评分并更新
    teams = ["A", "B", "C"]
    ratings = initialize_ratings(teams)
    print("初始评分：", {team: ratings[team].rating for team in teams})