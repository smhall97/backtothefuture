import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import scipy.optimize

from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set()

"""
Determine optimal window size for reward decoding
"""

# for carrying out window coding for response

#'VISrl' (visual) , 'MG' (thalamus), 'NB' (midbrain) , 'CA2', (hippocampus) 'SPF' (visual cortex? 
      
    
import time

t = time.time() 

master_dict_res={'VISrl' : [], 'MG' : [],'NB' : [],'CA2' : [],'SPF' : []}

targetneurons = ['VISrl', 'MG','NB','CA2','SPF']
for u in targetneurons:
    targetneurons=[u]
    
    
    for j in range(10,90,10): #before
      total_length=j
      vals=[]
      for i in range(0,40,10): # afetr
        pre=j
        post=i
        windowVals=[pre/100,post/100]
        #print(windowVals)
        try:
            ff=get_accuracy(targetneurons,windowVals,label ='response')
            vals.append([windowVals,ff,j+1])
        except:
            vals.append([windowVals,0.0,j+1])
            print("Error!")
        #print(windowVals,"  ",ff)
        
      master_dict_res[u].append(vals)
      print("Brain Area:",u," ",total_length/100,"sec")

"""
Determine optimal window size for response decoding
"""
example_master_dict={'MEA' : [],'CA' : [],'PT' : [],'MOp' : [],'PAG' : []}

targetneurons = ['MEA','CA','PT','MOp','PAG']
for u in targetneurons:
    targetneurons=[u]
    
    
    for j in range(20,220,10):
      total_length=j
      vals=[]
      for i in range(10,total_length,10):
        pre=total_length-i
        post=i
        windowVals=[pre/100,post/100]
        #print(windowVals)
        try:
            ff=get_accuracy(targetneurons,windowVals,label ='feedback_type')
            vals.append([windowVals,ff,total_length])
        except:
            vals.append([windowVals,0.0,total_length])
            print("Error!")
        #print(windowVals,"  ",ff)
        
      example_master_dict[u].append(vals)
      print("Brain Area:",u," ",total_length/100,"sec")



  