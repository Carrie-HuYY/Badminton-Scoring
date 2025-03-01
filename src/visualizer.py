import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 系统
plt.rcParams['axes.unicode_minus'] = False


def plot_ratings(ratings, save_path=None):
    """
    绘制队伍评分趋势图。
    :param ratings: 包含队伍评分的字典
    :param save_path: 图片保存路径（可选）
    """
    teams = list(ratings.keys())
    ratings_values = [ratings[team].rating for team in teams]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=teams, y=ratings_values, palette="viridis")
    plt.title("队伍 Glicko 评分")
    plt.xlabel("队伍")
    plt.ylabel("评分")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_rd_trend(ratings, save_path=None):
    """
    绘制队伍 RD 趋势图。
    :param ratings: 包含队伍评分的字典
    :param save_path: 图片保存路径（可选）
    """
    teams = list(ratings.keys())
    rd_values = [ratings[team].rd for team in teams]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=teams, y=rd_values, marker="o")
    plt.title("队伍 RD 趋势")
    plt.xlabel("队伍")
    plt.ylabel("RD")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_win_loss_heatmap(matches, save_path=None):
    """
    绘制队伍胜负关系热力图。
    :param matches: 比赛数据，格式为 DataFrame，包含 team_A, team_B, winner 列
    :param save_path: 图片保存路径（可选）
    """
    # 获取所有队伍
    teams = sorted(list(set(matches["team_A"]).union(set(matches["team_B"]))))

    # 初始化胜负矩阵
    win_loss_matrix = np.zeros((len(teams), len(teams)))

    # 填充胜负矩阵
    for _, row in matches.iterrows():
        winner = row["winner"]
    loser = row["team_A"] if row["team_B"] == winner else row["team_B"]
    i = teams.index(winner)
    j = teams.index(loser)
    win_loss_matrix[i, j] += 1

    # 绘制热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(win_loss_matrix, annot=True, fmt=".0f", xticklabels=teams, yticklabels=teams, cmap="YlOrRd")
    plt.title("队伍胜负关系热力图")
    plt.xlabel("输的队伍")
    plt.ylabel("赢的队伍")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":


    matches = pd.DataFrame({
        "match_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "team_A": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
        "team_B": ["B", "C", "A", "C", "A", "B", "B", "C", "A", "C"],
        "winner": ["A", "B", "C", "A", "A", "B", "A", "B", "C", "A"],
    })

    # 绘制评分趋势图
    #plot_ratings(ratings, save_path="ratings_trend.png")

    # 绘制 RD 趋势图
    #plot_rd_trend(ratings, save_path="rd_trend.png")

    # 绘制胜负关系热力图
    plot_win_loss_heatmap(matches, save_path="win_loss_heatmap.png")