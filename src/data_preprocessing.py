import pandas as pd

def load_data(file_path):
    """
    从 CSV 文件加载比赛数据。
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """
    预处理数据：确保数据格式正确。
    """
    # 检查数据是否包含必要的列
    required_columns = ["match_id", "team_A", "team_B", "winner"]
    if not all(column in data.columns for column in required_columns):
        raise ValueError("数据文件缺少必要的列：match_id, team_A, team_B, winner")

    # 确保 winner 列的值是 team_A 或 team_B
    if not all(data["winner"].isin(data["team_A"]) and not all(data["winner"].isin(data["team_B"])):
        raise ValueError("winner 列的值必须是 team_A 或 team_B")

    return data

if __name__ == "__main__":
    # 示例：加载并预处理数据
    file_path = "data/matches.csv"
    data = load_data(file_path)
    data = preprocess_data(data)
    print("数据加载与预处理完成！")
    print(data.head())