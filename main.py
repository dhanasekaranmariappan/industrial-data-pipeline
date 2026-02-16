from src.ingest import load_data
from src.clean import clean_data
from src.transform import add_features
from src.db import setup_database, insert_dataframe
from src.analysis import fetch_data
from src.visualize import plot_temperature

setup_database()
df = load_data("data/ai4i+2020+predictive+maintenance+dataset/ai4i2020.csv")
df = clean_data(df)
df = add_features(df)
insert_dataframe(df)

analytics_df = fetch_data()
plot_temperature(analytics_df)

