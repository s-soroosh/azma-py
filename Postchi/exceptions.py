
__author__ = 'Mahdi'

class TimeLimitBetweenTwo(Exception):

    def __init__(self, remaining_time):
        self.remaining_time = remaining_time
