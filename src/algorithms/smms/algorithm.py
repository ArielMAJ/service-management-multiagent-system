from loguru import logger

from src.schemas.algorith_parameters import AlgorithmInputParameters


def service_management_multiagent_system_runner(parameters: AlgorithmInputParameters):
    """ """
    parameters = AlgorithmInputParameters.model_validate(parameters)
    logger.info(f"[SMMS] [STEP {parameters.current_step}]")
