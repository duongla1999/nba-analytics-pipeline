from load_to_postgres import engine, load_data_to_postgres
import pandas as pd

SEASON_START = "2025-10-01"
SEASON_END = "2026-06-30"

JOBS = [
    {"csv_path": "data/games.csv", "table_name": "games", "filter_season": True},
    {"csv_path": "data/players.csv", "table_name": "players", "filter_season": False},
    {"csv_path": "data/teamStatistics.csv", "table_name": "teamStatistics", "filter_season": True},
    {"csv_path": "data/teamHistories.csv", "table_name": "teamHistories", "filter_season": False},
]
def filter_by_season(df: pd.DataFrame) -> pd.DataFrame:
    df["gameDate"] = pd.to_datetime(df["gameDate"])
    return df[
        (df["gameType"] == "Regular Season") &
        (df["gameDate"] >= SEASON_START) &
        (df["gameDate"] <= SEASON_END)
    ]

def run_pipeline():
    results = {}
    for job in JOBS:
        print(f"Loading {job['csv_path']} into raw.{job['table_name']} table...")
        df = pd.read_csv(job["csv_path"])
        print(f"read shape: {df.shape}")

        if job["filter_season"]:
            df = filter_by_season(df)
            print(f"filtered shape: {df.shape}")

        success = load_data_to_postgres(df, job["table_name"], engine, schema="raw", if_exists="replace", index=False)
        results[job["table_name"]] = success

    print("Pipeline completed. Results:")
    for table_name, success in results.items():
        print(f"{table_name}: {'Success' if success else 'Failed'}")

if __name__ == "__main__":
    run_pipeline()
