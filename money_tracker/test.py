import pandas as pd
import numpy as np
from dataclasses import dataclass as dc
import enum

class item_category(enum.Enum):
    grocery = 0
    alcohol = 1
    weed    = 2
    monthly = 3
    

index = ["Income", "Spending"]