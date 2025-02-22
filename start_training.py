import os 
import sys

from networks security.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.pipeline import Training_pipeline

def start_training():
    try:
        model_training = Training_pipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    