import time
import threading


class SleepyWorker(threading.Thread):

    def __init__(self, seconds, **kwargs):
        # we can make use of the kwargs to pass extra flags to the Thread class
        super().__init__(**kwargs)
        self._seconds = seconds
        self.start()


    def _sleep_a_little(self):
        time.sleep(self._seconds)

    def run(self):
        """
        This function gets called by the start method of the Thread Class
        """
        self._sleep_a_little()
