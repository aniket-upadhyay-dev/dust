from __future__ import annotations
from typing import Any
import numpy as np
from numpy.typing import NDArray



class Column:
    def __init__(self, data: np.ndarray) -> None:
        self.data = data  # self is the column object and self.data is the array itself
        # column.data = [10,20,30]
    def __rshift__(self, operation: Any) -> float:
        return operation.__rrshift__(self.data)  

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"Column({self.data})"

    def __eq__(self, condition: Any) -> np.ndarray: #type: ignore
        return np.equal(self.data,condition)
    
    def __gt__(self, condition: Any) -> np.ndarray:
        return np.greater(self.data, condition)
    
    def __lt__(self, condition: Any) -> np.ndarray:
        return np.less(self.data, condition)

    def __le__(self, condition: Any) -> np.ndarray:
        return np.less_equal(self.data, condition)
    
    def __ge__(self, condition: Any) -> np.ndarray:
        return np.greater_equal(self.data, condition)

    def __ne__(self, condition: Any) -> np.ndarray:  #type: ignore
        return np.not_equal(self.data, condition)


class Sum:
    def __rrshift__(self, data):
        return np.nansum(data)

class Avg:
    def __rrshift__(self, data):
        return np.nanmean(data)

class Min:
    def __rrshift__(self, data):
        return np.nanmin(data)

class Max:
    def __rrshift__(self, data):
        return np.nanmax(data)

class Count:
    def __rrshift__(self, data):
        return np.count_nonzero(data)

class Filter:
    def __init__(self, df: DDF, condition: np.ndarray) -> None:
        self.df = df
        self.condition = condition

    def __getitem__(self, key: str) -> Column:
        return Column(self.df[key].data[self.condition])
    
class DDF:
    def __init__(self, filename):
        raw = np.genfromtxt(filename, delimiter=',',dtype=str)
        header = np.char.strip(raw[0])
        data = np.char.strip(raw[1:])
        self.columns = {}
        for i, col_name in enumerate(header):
            # convert '' to 'nan' here 
            col = np.where(data[:,i] == '', 'nan', data[:,i])
            
            try:
                float_data = col.astype(float)
                self.columns[col_name] = float_data
            except ValueError:
                self.columns[col_name] = col

    def __getitem__(self, key):
        return Column(self.columns[key])
