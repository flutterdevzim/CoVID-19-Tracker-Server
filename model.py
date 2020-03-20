from cnews import CoronaNews
import loguru

class CoronaTracker(CoronaNews):

    def __init__(self):
        self.log = loguru.logger
