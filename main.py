import os

from py_clob_client import ClobClient
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
data = client.get_midpoint(84)
print(data)
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
    print("well")
    # UserProcess().run()