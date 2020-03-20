from cnews import CoronaNews
import loguru

class CoronaTracker(object):

    def __init__(self):
        self.log = loguru.logger
        self.newsapi = CoronaNews()
