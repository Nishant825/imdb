import requests
import  pandas as pd
import os
import matplotlib.pyplot as plt


def get_crypto_data():
    data = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc")
    res = data.json()[:15]
    return res


def save_chart():
  response = get_crypto_data()
  df = pd.DataFrame(dict(
    symbol = [i["symbol"].upper() for i in response],
    price = [i["current_price"] for i in response],
  ))
  if not os.path.exists("images"):
    os.mkdir("images")
  plt.title('cryptocurrency data')
  plt.bar(df["symbol"], df["price"], color='green')
  plt.xlabel("symbols")
  plt.ylabel("current_price(INR)")
  plt.xticks(rotation=32)
  plt.subplots_adjust(left=0.2, right=0.9, bottom=0.1, top=0.9)
  folder_path = "images"
  file_name = "graph.png"
  file_path = os.path.join(folder_path, file_name)
  plt.savefig(file_path)