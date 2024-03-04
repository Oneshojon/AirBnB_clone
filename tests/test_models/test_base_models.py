#!/usr/bin/python3
"""
A test_class to test all classeses and methods
"""

import unittest
from models.base_model import Basemodel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """
    A class to perform unittest on base_model.
    """

    def setUp(self):
        """
        sets up a base_model.
        """
        self.base_model = BaseModel()
        
