import json
import os
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
print(cg.ping())
cardano_price_usd = cg.get_price(
    ids='cardano', vs_currencies='usd,jpy')
print(cardano_price_usd)
data_folder = "data"
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

with open(os.path.join(data_folder, "data.json"), "w") as f:
    json.dump(cardano_price_usd, f)
