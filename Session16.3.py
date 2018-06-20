# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:31:25 2018

@author: avatash.rathore
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


print("""For a random student, 

The probability of failing in 0 subjects, P(X=0) = 0.8

The probability of failing in 1 subjects, P(X=1) = 0.1

The probability of failing in 2 subjects, P(X=2) = 0.07

The probability of failing in 3 subjects, P(X=3) = 0.03""")

Dataset = np.array([0.8,0.1,0.7,0.03])    
Df = pd.DataFrame(Dataset,columns={'X'})
Df.describe()
Mean=Df.mean()
Std= Df.std()
Df['Probablity density distribution'] = stats.norm.pdf(Df['X'],0,1)
Df.head()









