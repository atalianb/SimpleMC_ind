
#Given a file with data and error bars, create its covariance matrix

import pandas as pd
import numpy  as np

file = '../data/data_used_by_Tula/U11748.dat'

df   = pd.read_csv(file, sep ='\s+', names = ['Rkpc', 'V', 'Err'], skiprows=[0,1,2,3,4])
sigma = np.array(df['Err'].tolist())**2
cov = np.zeros((18, 18), float)
np.fill_diagonal(cov, sigma)

with open('U11748-cov.txt', 'wb') as f:
    #f.write('# 11 11 \n')
    np.savetxt(f, cov, fmt='%.2f')
