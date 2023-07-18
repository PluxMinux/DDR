import csv
import pandas as pd

class Main:
    def __init__(self, csv_path, save_path):
        self.csv_path = csv_path
        self.save_path = save_path  

    def __str__(self):
        return f"{self.csv_path}\n{self.save_path}"
    
    def total_rows(self):
        countingRows = pd.read_csv(self.csv_path, encoding='latin-1', header=None, dtype='unicode')    
        totalRows = len(countingRows)
        return totalRows

    def dups_remover(self):
        nrow = []
        for n in range(self.total_rows()):
            nrow.append(n)
        ncol = []
        for n in range(24):
            ncol.append(n)
        
        df = pd.read_csv(self.csv_path, encoding='latin-1', header=None,skiprows = lambda x: x not in nrow, usecols=ncol, dtype='unicode')
        df.drop_duplicates(subset=10,keep='last', inplace=True)
        
        
        df.to_csv(self.save_path, index=False, header=False)
        
            
        
        return "Done"











