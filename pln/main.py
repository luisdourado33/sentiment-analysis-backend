import pandas as pd

from helpers import getJsonData, plotGraph

table_url = "https://sentimentanalysis-9bdac-default-rtdb.firebaseio.com/pos_tweets.json"
table_items = getJsonData(table_url)

# Training base in real-time.
# Table: "pos_tweets"
training_base = pd.read_json(table_items)