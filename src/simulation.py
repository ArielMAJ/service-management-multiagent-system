from random import seed
from typing import Callable

import edge_sim_py as esp
import numpy as np
from loguru import logger


class Simulation:

    def __init__(self, algorithm: Callable[[dict], None]):
        self.algorithm = algorithm

    def run(self):
        logger.info(f">>>>>> [{self.algo_name}] <<<<<<")
        seed_value = 428956419
        seed(seed_value)
        np.random.seed(seed_value)
        simulator = esp.Simulator(
            tick_duration=1,
            tick_unit="seconds",
            stopping_criterion=lambda model: model.schedule.steps == 10,
            resource_management_algorithm=self.algorithm,
        )

        simulator.initialize(
            input_file="https://raw.githubusercontent.com/EdgeSimPy/edgesimpy-tutorials/master/datasets/sample_dataset1.json"  # noqa
        )

        simulator.run_model()

    @property
    def algo_name(self):
        return self._algo_name

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._algorithm = value
        self._algo_name = value.__name__
