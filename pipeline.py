from src.ingest import load_data
from src.clean import clean_data
from src.transform import add_features
from src.db import setup_database, insert_dataframe
from src.analysis import fetch_data
from src.visualize import plot_temperature
import logging

logging.basicConfig(level=logging.INFO)





logging.info("Starting data pipeline...")
setup_database()
df = load_data("data/ai4i+2020+predictive+maintenance+dataset/ai4i2020.csv")
logging.info("Loading dataset...")
df = clean_data(df)
df = add_features(df)
insert_dataframe(df)
logging.info("Writing to MySQL...")

analytics_df = fetch_data()
plot_temperature(analytics_df)
logging.info("Pipeline completed successfully.")
