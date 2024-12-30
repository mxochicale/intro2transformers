import os
from loguru import logger
import torch
import gc

def test_gpu():
    """
    Test gpu availability
    pytest -vs tests/test_resources.py::test_gpu

    """
    os.system("nvidia-smi")

    logger.info(gc.collect())

    if torch.cuda.is_available():
        logger.info("GPU available: " + torch.cuda.get_device_name(0))
        logger.info("GPU count: " + str(torch.cuda.device_count()))
    else:
        logger.info(torch.cuda.is_available())
        logger.info("GPU not available 😔")

