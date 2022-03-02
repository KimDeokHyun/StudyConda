#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np

def outliers_iqr3(dframe, data) : 
    q1, q3 = np.percentile(data, [25, 75])
    print(q1)
    print(q3)
    
    iqr = q3 - q1
    print(iqr)
    
    upper_bound = q3 + (iqr * 1.5)
    print(upper_bound)
    
    lower_bound = q1 - (iqr * 1.5)
    print(lower_bound)
    
    df_temp = dframe[(data > upper_bound) | 
                             (data < lower_bound)]
    
    print(len(df_temp))
    print(df_temp)

