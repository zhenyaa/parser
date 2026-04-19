from selenium import webdriver
from multiprocessing import Process, Queue

from praser import Parser


PAGES = [
    'https://www.wunderground.com/history/daily/ng/lagos/DNMM',

]

class UserProcess:
    def __init__(self):
        self.q = Queue()

    def run(self):
        processes = []

        for page in PAGES:
            parser = Parser(page, self.q)
            p = Process(target=parser.run)
            p.start()
            processes.append(p)

        while True:
            item = self.q.get()
            print("NEW:", item)


if __name__ == "__main__":
    UserProcess().run()