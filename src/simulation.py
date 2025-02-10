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
            stopping_criterion=self.stopping_criterion,
            resource_management_algorithm=self.algorithm,
        )

        simulator.initialize(input_file="./datasets/sample1.json")

        for user in esp.User.all():
            logger.info(user.coordinates)
        for server in esp.EdgeServer.all():
            logger.warning(server.coordinates)
        simulator.run_model()

        for user in esp.User.all():
            logger.info(user.coordinates)
        for server in esp.EdgeServer.all():
            logger.warning(server.coordinates)
        for service in esp.Service.all():
            logger.error(service.agent.coordinates)

    def stopping_criterion(self, model):
        remaining_services_awaiting_placement_in_an_edge_server: list[esp.Service] = [
            service for service in esp.Service.all() if not service.server
        ]
        return (
            model.schedule.steps == 100
            or not remaining_services_awaiting_placement_in_an_edge_server  # noqa
        )

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
