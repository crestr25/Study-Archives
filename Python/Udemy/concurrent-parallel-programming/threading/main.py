import time
from multiprocessing import Queue

from workers.wiki_worker import WikiWorker
from workers.yahoo_finance_price_worker import YahooFinancePriceScheduler
from dotenv import load_dotenv

load_dotenv()

def main():
    start_time = time.perf_counter()

    # Create a symbol queue, queues are thread safe
    # They are blocking (.get()) which means the program waits until a value is returned
    symbol_queue = Queue()
    worker_threads = []
    num_workers = 4

    wiki_worker = WikiWorker()
    # Defined before so it can start consuming
    for _ in range(num_workers):
        finance_scheduler = YahooFinancePriceScheduler(symbol_queue)
        worker_threads.append(finance_scheduler)

    for symbol in wiki_worker.get_sp_500_companies():
        # Store the symbol
        symbol_queue.put(symbol)
    
    for worker in worker_threads:
        symbol_queue.put("DONE")
     
    for worker in worker_threads:
        worker.join()

    print(f'Extracting Time took: {time.perf_counter() - start_time}')


if __name__ == "__main__":
    main()
