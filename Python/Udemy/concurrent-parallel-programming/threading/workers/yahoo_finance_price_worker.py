import time
import random
import threading
import requests
from lxml import html

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super().__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break

            finance_worker = YahooFinancePriceWorker(symbol=val)
            price = finance_worker.get_price()
            print(price)
            time.sleep(0.5)


class YahooFinancePriceWorker():
    def __init__(self, symbol):
        self._symbol = symbol.lower()
        # base_url = 'https://stockanalysis.com/stocks/'
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = base_url + self._symbol
        self._headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        }

    def get_price(self):
        # sleep a random amount of time to prevent spam
        print(f"Making request to {self._url}...")
        response = requests.get(self._url, headers=self._headers)
        if response.status_code != 200:
            print(f"Could not get {self._symbol} price")
            return
        
        page_contents = html.fromstring(response.text)
        raw_price = page_contents.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span')[0].text
        price = float(raw_price.replace(",", "."))

        return price


class YahooFinancePriceWorkerOld(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super().__init__(**kwargs)
        self._symbol = symbol.lower()
        base_url = 'https://stockanalysis.com/stocks/'
        self._url = base_url + self._symbol
        self._headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15",
        }
        self.start()


    def run(self):
        # sleep a random amount of time to prevent spam
        time.sleep(20 * random.random())
        print(f"Making request to {self._url}...")
        response = requests.get(self._url, headers=self._headers)
        print(response)
        if response.status_code != 200:
            print(f"Could not get {self._symbol} price")
            return
        
        page_contents = html.fromstring(response.text)
        price = float(page_contents.xpath('//*[@id="main"]/div[1]/div[2]/div/div[1]')[0].text)
        print(price)

