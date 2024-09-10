"""
Filename: algorithm_config.py
Description: Converts Algorithm JSON options to local data types and configures core Algorithm module via setters. 
Initial Creator: Elysia Guglielmo (System Architect)
Author: Yuganya Perumal
Date: 2024-07-11
Version: 1.0
Python Version: 

Changelog:
- 2024-07-11: Initial creation.
- 2024-08-24: Reading JSON Options satellite_names to configure the setters by Yuganya Perumal 

Usage: 

"""
import json
from dataclasses import dataclass

from interfaces.config import Config
from algorithm_core import Algorithm

@dataclass
class AlgorithmOptions:
    key: str
    satellite_names = []

class AlgorithmConfig(Config):

    # Constructor, accepts core module
    def __init__(self, algorithm:Algorithm):
        self.algorithm = algorithm
        self.options = None

    # Traverse JSON options to check for nested objects
    def read_options(self, options):
        self.options = options
        self.set_algorithm()

    def read_options_from_file(file):
         return super().read_options_from_file()


    def set_algorithm(self):
        self.algorithm.set_satellite_names(self.options["satellite_names"])

    def get_satellite_names(self):
        return self.algorithm.get_satellite_names() 
