import time
import threading

class HitCounter():
    __slots__ = ("hits", "hits_lock")

    def __init__(self):
        self.hits = 0
        self.hits_lock = threading.Lock()

    def add_hit(self):
        with self.hits_lock:
            self.hits += 1

    def __len__(self):
        with self.hits_lock:
            return self.hits
