#!/usr/bin/env python3

import pandas as pd
import numpy as np
import time

#del df1, df2, df3, df4
numOfRows = 1000
cols = ('A', 'B', 'C', 'D', 'E')

# append
startTime = time.perf_counter()
df1 = pd.DataFrame(columns = cols)
for i in range(0, numOfRows):
    df1 = df1.append( dict( (a, np.random.randint(100)) for a in cols), ignore_index = True)

print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
print(df1.shape)
del df1

# .loc w/o prealloc
startTime = time.perf_counter()
df2 = pd.DataFrame(np.random.randint(100, size = (5,5)), columns = cols)
for i in range(0, numOfRows):
    df2.loc[i]  = np.random.randint(100, size = (1,5))[0]

print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
print(df2.shape)
del df2

# .loc with prealloc
df3 = pd.DataFrame(index = np.arange(0, numOfRows), columns = cols)
startTime = time.perf_counter()
for i in range(0, numOfRows):
    df3.loc[i]  = np.random.randint(100, size = (1,5))[0]

print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
print(df3.shape)
del df3

# dict
startTime = time.perf_counter()
row_list = []
#for i in range (0,5):
#    row_list.append(dict( (a,np.random.randint(100)) for a in cols))
#for i in range(1, numOfRows - 4):
#    dict1 = dict( (a,np.random.randint(100)) for a in cols)
#    row_list.append(dict1)
for i in range(0, numOfRows):
    row_list.append(dict( (a, np.random.randint(100)) for a in cols ))

df4 = pd.DataFrame(row_list, columns = cols)
print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
print(df4.shape)
del df4

# tuple
startTime = time.perf_counter()

df5 = pd.DataFrame(tuple(tuple(np.random.randint(100) for a in cols) for i in range(0, numOfRows)), columns = cols)
print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
print(df5.shape)
del df5
