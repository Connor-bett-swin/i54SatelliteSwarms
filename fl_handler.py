"""
Filename: fl_handler.py
Description: Reads algorithm data to perform preprocessing before running federated learning round. 
Author: Elysia Guglielmo
Date: 2024-08-02
Version: 1.0
Python Version: 

Changelog:
- 2024-08-02: Initial creation.

Usage: 

"""
from interfaces.handler import Handler

class FLHandler(Handler):

    # Constructor
    def __init__(self, federated_learning):
        self.federated_learning = federated_learning

    def parse_input(file):
        return super().parse_input()