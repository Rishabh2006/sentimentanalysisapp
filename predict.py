# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:22:44 2021

@author: risha
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Predict1(BaseModel):
    Review : str
    