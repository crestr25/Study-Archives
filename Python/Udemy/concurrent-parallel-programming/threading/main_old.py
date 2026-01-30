import time
from workers.wiki_worker import WikiWorker
from workers.yahoo_finance_price_worker import YahooFinancePriceWorker

def main():
    start_time = time.perf_counter()

    wiki_worker = WikiWorker()
    current_workers = []
    for symbol in wiki_worker.get_sp_500_companies():
        yahoo_worker = YahooFinancePriceWorker(symbol)
        current_workers.append(yahoo_worker)

    for worker in current_workers:
        worker.join()


if __name__ == "__main__":
    main()
