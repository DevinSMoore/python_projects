from cmath import exp
import pandas as pd
import numpy as np
from dataclasses import dataclass as dc
import enum

class item_category(enum.Enum):
    grocery = 0
    alcohol = 1
    weed    = 2
    monthly = 3

column_names = ["income", "expenses"]
#index_names 
df = pd.DataFrame([[600,0]], columns=column_names)
#df.reset_index(inplace=True)
print('Before concat:\n', df, '\n')

income = input("Please enter your income: ")
expenses = input("Please enter your expenses: ")

i_df = pd.DataFrame([[income, expenses]], columns=column_names)



print("Index of df: ", df.index, "\nIndex of i_df: ", i_df.index)


df = pd.concat([df, i_df], ignore_index=True, axis=0)

print('After concat:\n', df, '\n')