import logging
import time

from threading import Lock, Thread


class MyThread(Thread):
    """
    My custom Thread class which will inform on stop...
    """

    def start(self):
        logging.info("%s Starting", self.name)
        super().start()

    def _stop(self):
        super()._stop()
        logging.info("%s Stopped", self.name)


class ThreadLockContextManager:
    def __init__(self, current_thread_name):
        self.thread_name = current_thread_name
        self.lock = Lock()

    def __enter__(self):
        logging.info("%s Lock is accuiring..." % self.thread_name)
        try:
            self.lock.acquire()
            logging.info("%s Locked..." % self.thread_name)
        finally:
            logging.info("%s Still Locked..." % self.thread_name)


    def __exit__(self, *args, **kwargs):
        self.lock.release()
        logging.info("%s Lock is releaseing..." % self.thread_name)
        logging.info("%s Lock is released..." % self.thread_name)
        return False


def write_to_file(thrad_index):
    with ThreadLockContextManager(thrad_index) as locker:
        logging.info("%s Locked!" % thrad_index)
        now = time.time()
        988888888888888888989898989898989898888888888888999999999999999999999 / 43333333338524745563333333334555454545454
        duration = time.time() - now
        print("Computation ended in %s" % duration)
        logging.info("Thread %s starts writing." % thrad_index)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S", filename="log_txt.log")

    for i in range(12):
        t = MyThread(name="Pablo %s" % i, target=write_to_file, args=(i,))
        t.start()
