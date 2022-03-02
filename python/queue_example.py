from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


# CSV writer setup goes here

queue = Queue()


def consume():
    while True:
        if not queue.empty():
            i = queue.get()
            
            # Row comes out of queue; CSV writing goes here
            
            print(i)
            if i == 4999:
                return


consumer = Thread(target=consume)
consumer.setDaemon(True)
consumer.start()


def produce(i):
    # Data processing goes here; row goes into queue
    queue.put(i)


with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(5000):
        executor.submit(produce, i)

consumer.join()

