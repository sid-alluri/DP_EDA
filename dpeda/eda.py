
import json
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

class Owner():
    
    def __init__(self):
        
        self.data = None
        self.jsondata = None
        self.stats = []

        return None


    def get_stats(self, df, Header = 'DP EDA'):

        profile = ProfileReport(df, title=Header, explorative=False, progress_bar = False , minimal=True )
        profile.to_file("data_report.json")
        json_file = open('data_report.json')
        self.jsondata = json.load(json_file)
        for x in self.jsondata['variables'].keys():
            _buf = self.jsondata['variables'][x]
            self.stats.append([_buf['mean'], _buf['std'], _buf['variance']])

        return np.array(self.stats)



