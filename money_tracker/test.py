import pandas as pd
import numpy as np
from dataclasses import dataclass as dc
import enum

class item_category(enum.Enum):
    grocery = 0
    alcohol = 1
    weed    = 2
    monthly = 3
    
df = pd.DataFrame([[600,0]], index=[1], columns=["income", "expenses"])

print(df)

df.add(5,1)

print(df)