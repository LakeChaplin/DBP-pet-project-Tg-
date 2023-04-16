import datetime
import random
from config import get_comment

class MeasuringState:
    def __init__(self):
        self.last_measurement = {}

    def can_measure(self, user_id):
        if user_id not in self.last_measurement:
            return True

        time_since_last_measurement = datetime.datetime.now() - self.last_measurement[user_id]
        return time_since_last_measurement >= datetime.timedelta(days=1)

    def measure_cook_size(self, user_id):
        self.last_measurement[user_id] = datetime.datetime.now()
        cook_size = random.randint(1, 30)
        message = f"{get_comment().format(cook_size)}"  
        return cook_size, message

