# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:44:34 2020

@author: ADMIN
"""

import glassdoor_scraper as gs
import pandas as pd

path="C:/Users/ADMIN/Documents/sai/data_science/chromedriver"
df = gs.get_jobs('data scientist', 15, path, 20, False)