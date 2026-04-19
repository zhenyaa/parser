import os
from pprint import pprint

from py_clob_client import ClobClient, BookParams, ApiCreds
from selenium import webdriver
from multiprocessing import Process, Queue

from praser import Parser
from dotenv import load_dotenv
load_dotenv()
POLY_TOKEN = os.getenv("POLY_TOKEN")
PAGES = [
    'https://www.wunderground.com/history/daily/ng/lagos/DNMM',

]
HOST = "https://clob.polymarket.com"
CHAIN_ID = 137
PRIVATE_KEY = os.getenv("POLY_TOKEN")
FUNDER = "<your-funder-address>"
client = ClobClient(
    HOST,  # The CLOB API endpoint
    key=PRIVATE_KEY,  # Your wallet's private key
    chain_id=CHAIN_ID,  # Polygon chain ID (137)
    signature_type=1,  # 1 for email/Magic wallet signatures

)

next_page = "MA=="
key_word = 'temperature'
result = []

for i in range(1, 200):

    a: dict = client.get_orders(next_cursor=next_page)
    print(a)
    next_page = a['next_cursor']
    print(a)
    # for i in a['data']:
    #     if key_word in i['question']:
    #         result.append(i)
#
# pprint(result)
# print(len(result))

# for i in a["data"][:20]:
#     pprint(i)
# token_id = "537"
# mid = client.get_midpoint(token_id)
# price = client.get_price(token_id, side="BUY")
# book = client.get_order_book(token_id)
# books = client.get_order_books([BookParams(token_id=token_id)])
# print(mid, price)
# class UserProcess:
#     def __init__(self):
#         self.q = Queue()
#
#     def run(self):
#         processes = []
#
#         for page in PAGES:
#             parser = Parser(page, self.q)
#             p = Process(target=parser.run)
#             p.start()
#             processes.append(p)
#
#         while True:
#             item = self.q.get()
#             print("NEW:", item)


if __name__ == "__main__":
    print("program finish")
    # UserProcess().run()