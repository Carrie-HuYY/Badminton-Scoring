from data_preprocessing import load_data, preprocess_data
from glicko_model import initialize_ratings, update_ratings_from_matches
from visualizer import plot_ratings, plot_rd_trend

def main():
    # 数据获取与预处理
    file_path = "data/matches.csv"
    data = load_data(file_path)
    data = preprocess_data(data)

    # 初始化评分
    teams = list(set(data["team_A"]).union(set(data["team_B"])))
    ratings = initialize_ratings(teams)

    # 更新评分
    update_ratings_from_matches(ratings, data)

    # 可视化
    plot_ratings(ratings, save_path="ratings_trend.png")
    plot_rd_trend(ratings, save_path="rd_trend.png")

if __name__ == "__main__":
    main()