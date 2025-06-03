# Task 5: Extending a Class

import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        total_rows = len(self)
        if total_rows == 0:
            print("DataFrame is empty.")
            return
        
        for start_row in range(0, total_rows, 10):
            end_row = min(start_row +10, total_rows)
            chunk = self.iloc[start_row:end_row]
            print(f"\nRows {start_row + 1} to {end_row}:")
            print(chunk)


dfp = DFPlus.from_csv("../csv/products.csv")
dfp.print_with_headers()
