"""
Code written by Holly Wilson
Logistic regression implemented using the [scikitlearn framework](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
Aim: decode reward information (feedback) and responese (prediction) information within the neural signals
"""

'''
Find optimal decoding window
Adapted from sort_areas_decoding_areas

From function: return -(accuracy) for target area given start/end windows
Minimise function
'''
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import scipy.optimize

from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set()

def get_accuracy(targetneurons,windowVals,label):

    trial_count=[]

    windowPre = windowVals[0] * 100
    windowPost = windowVals[1] * 100
    windowSize = windowPre + windowPost

    if label == 'feedback_type':
      timeMeasure = 'feedback_time'
    elif label =='response':
      timeMeasure = 'response_time'
    endLimit = 2.5 - ((windowPost/100)+0.5)


    accuracyList = [] # Accumulates accuracies for all brain areas
    # Loop over target neurons
    for neuron in targetneurons:

        # All responses list
        areaStack = np.zeros([1, int(windowSize)])
        labelStack = np.array([0])

        # Loop through all recordings
        for dat in alldat:

            # Get target neurons for this recording
            targetInds = getNeurons(dat, neuron)

            # Get rewarded trials for target neurons
            targetSpikes = dat['spks'][targetInds, :, :]

    
            # Limit by response time: need suitable buffer at end
            if label == 'feedback_type': 
              usableInds = dat[timeMeasure] < endLimit# 1.90
            elif label == 'response':
              usableInds = dat[timeMeasure]  < endLimit #dat['feedback_time']
            #  print("usableInds ", usableInds)
            usableInds = usableInds.squeeze()
            

            targetSpikes = targetSpikes[:, usableInds, :]
            indextimes = dat[timeMeasure][usableInds] # HW: changed from timemeasure to label, and feedbacktimes to generic indextimes
            trial_count.append(np.shape(targetSpikes)[1])

            labels = dat[label][usableInds] # Labels for usable trials

            # Get window around reward for each trial  ############################ changed here
            windowInds = [(int((respTime)*100)+50) for respTime in indextimes]
            # HW: added
            indexWindows = np.zeros((len(targetInds), targetSpikes.shape[1], int(windowPre+windowPost))) # changed from feedback window to index window
            for i in range(targetSpikes.shape[1]):
                indices = np.arange(windowInds[i]-windowPre, windowInds[i]+windowPost).astype('int')
                struct = targetSpikes[:, i, indices]

                try: # To account for indices where the indices aren't working (missing recordings in a particualr mouse)
                    indexWindows[:, i, :] = struct
                except:
                    indexWindows[:, i, :] = struct[:, :-1]
)

            # Reshape structures
                # [neurons x trials x time] -> [trials x time]
            currentStack = reshapeToTrials(indexWindows)
            labelvec = np.tile(labels, targetSpikes.shape[0])



            areaStack = np.concatenate((areaStack,currentStack), axis=0)
            labelStack = np.concatenate((labelStack, labelvec), axis=0)

        # Drop zeros from beginning of responsimize.es
        areaStack = areaStack[1:, :] # All of the trials for a specific brain area in the respective loop (trial x time)
        labelStack = labelStack[1:] # Vector len(number of trials) - each element = feedback given (i.e. label)

        # Do decoding (logistic regression) for brain area
        log_reg = LogisticRegression(penalty="none", max_iter=1000)
        # Confirm dimensions are correct
        log_reg.fit(areaStack, labelStack)
        #average accuracy
        accuracies_for_respective_area = np.mean(cross_val_score(log_reg,areaStack, labelStack, cv=5, scoring = 'accuracy'))

        # Add to accuracy list 
        accuracyList.append(accuracies_for_respective_area)
    
    # Return negative accuracy
    accuracy = accuracyList[-1]

    return accuracy
