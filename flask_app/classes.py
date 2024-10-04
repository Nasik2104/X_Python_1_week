import time

from flask import jsonify
from threading import Thread

washing_state = {'state': "waiting"}


class WashingMachineThread(Thread):
    """
    Class for creating thread with washing machine states.
    """
    def __init__(self):
        super(WashingMachineThread, self).__init__()

    def washing_cycle(self, washing_time=15, rinsing_time=7, spinning_time=7):
        """
        Func for Washing cycle.
        Params:
            washing_time: int
            rinsing_time: int
            spinning_time: int
        """
        global washing_state
        progress = {
            'water flooding': 5,
            'washing': washing_time,
            'rinsing': rinsing_time,
            'spinning': spinning_time,
            'complete': 5
        }

        for state, timing in progress.items():
            washing_state["state"] = state
            while timing:
                washing_state["time"] = timing
                timing -= 1
                time.sleep(1)

        washing_state["state"] = "waiting"

        return jsonify(washing_state)

    def run(self):
        self.washing_cycle()


class Converter:
    def __init__(self):
        super(Converter, self).__init__()

    def convert(self, value, coef):
        result = value * coef
        return round(result, 5)
