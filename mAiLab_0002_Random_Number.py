# -*- coding: utf-8 -*-

# HW0002 Random Number
import numpy as np
import time


# Basic
# 1. Generate 5 random numbers and print
print('Generating 5 random numbers=', np.random.random(5))

# 2. Generate N random numbers within -1 to 1 and calculate mean and stddev and
# print. Random numbers shouldn't be printed. N = 10^1, 10^2, 10^3, 10^4, 10^5
# Advanced
# 3. From 2, calculate time when generating N random numbers    

#set N = 10^1, 10^2, 10^3, 10^4, 10^5
N = [10 ** i for i in range(1, 6)]
     
for i in N:
    #t1 record the start time of each loop
    t1=time.time()
    x=2*np.random.random(i)-1
    #calculate the time when generating N random numbers    
    delta_t=time.time()-t1
    #print N, mean and sd and time spent
    print('N=', i, ', Mean=', np.mean(x), ' SD=', np.std(x), 'time= ', delta_t, 's')
    #print('N= {}, Mean= {}, SD= {}, time= {:10f}'.format(i, np.mean(x), np.std(x), delta_t))

#Advanced
# 4. Self-made Random Number Generator
     
     


    


    
