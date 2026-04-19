import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Parser:
    def __init__(self, page, queue=None):
        self.page = page
        self.queue = queue

    def run(self):
        driver = webdriver.Chrome()

        seen = set()  # чтобы не дублировать результаты

        while True:
            driver.get(self.page)
            table = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//lib-city-history-summary//table"
                ))
            )

            el = table.find_element(By.XPATH, ".//tbody[1]/tr[1]/td[1]")
            text = el.text
            if text not in seen:
                seen.add(text)
                if self.queue is None:
                    print(text)
                    continue
                self.queue.put({
                    "page": self.page,
                    "title": text
                })
            time.sleep(5)

if __name__ == "__main__":
    page = 'https://www.wunderground.com/history/daily/ng/lagos/DNMM'
    parser = Parser(page)
    parser.run()


