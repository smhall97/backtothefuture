# Code written by Conor Keogh
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from scipy.optimize import minimize
from statsmodels.tsa.stattools import grangercausalitytests

from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set()

"""
Determine best lag for Granger causality analysis
Code will produce a plot for analysis
"""

all_lags = []
for lag in range(1,28): # Here using 28 lags
    # Initialise test statistic list
    teststatistic=[] 
    for trial in range(len(results)):
        currenttrial = results[trial][lag][0]['lrtest'][1] # See above for data structure
        teststatistic.append(currenttrial)
    
    all_lags.append(np.mean(teststatistic))

bestlag = np.argmin(all_lags)

for trial in range(len(results)):
        currenttrial = results[trial][bestlag][0]['lrtest'][1] # See above for data structure
        teststatistic.append(currenttrial)

sns.set_context("talk")
with sns.axes_style("dark"):
    fig, ax = plt.subplots(2, 1, figsize=(6, 6))
    ax[0].plot(all_lags)
    ax[0].plot([0, 28], [0.05, 0.05], 'k--', label='0.05')
    ax[0].set_xlabel('Number of lags')
    ax[0].set_ylabel('p', fontstyle='italic')
    ax[0].legend(loc='upper right')
    ax[0].set_xlim([0, 26])
    ax[0].set_title('p value vs. lags')

    ax[1].hist(teststatistic, bins=30, range=[0,0.1])
    ax[1].set_title('p value distribution, lag = {}'.format(bestlag))
    ax[1].set_xlabel('p', fontstyle='italic')
    ax[1].set_ylabel('Count')

    fig.tight_layout()

"""
Determine best lag according to a test statistic
"""
bestlag = np.argmin(all_lags)

for trial in range(len(results)):
        currenttrial = results[trial][bestlag][0]['lrtest'][1] # See above for data structure
        teststatistic.append(currenttrial)

plt.hist(teststatistic, bins=30, range=[0,0.001])

'''
Granger causality analysis is performed for every trial
For each set of trials: run from 0 to N-1
    At each: predict predictionWindow[n+1] using feedbackWindow[n]
    Append results to massive list
'''
# Define window size
windowValsReward = [0.1, 0.8]
windowValsPrediction = [0.8, 0.1]

def get_accuracy(windowValsReward, windowValsPrediction):
    stimulusOnset = 50
    targetneurons = ['CA']
    timeMeasureReward = 'feedback_time'
    timeMeasurePrediction = 'response_time'

    windowPreReward = windowValsReward[0] * 100
    windowPostReward = windowValsReward[1] * 100
    windowSizeReward = windowPreReward + windowPostReward
   # endLimit = 2.5 - (windowPostReward/100) 

    windowPrePrediction = windowValsPrediction[0] * 100
    windowPostPrediction = windowValsPrediction[1] * 100
    windowSizePrediction = windowPrePrediction + windowPostPrediction

    # accuracyList = np.zeros(len(targetneurons))
    statsList = [] # Accumulates accuracies for all brain areas
    # Loop over target neurons
    for neuron in targetneurons:

        # Loop through all recordings
        for dat in alldat:

            # Get target neurons for this recording
            targetInds = getNeurons(dat, neuron)

            # Get rewarded trials for target neurons
            targetSpikes = dat['spks'][targetInds, :, :]
          
            endLimit =  targetSpikes.shape[2] - (windowPostReward) 


            usableInds = (dat[timeMeasureReward]*100)+stimulusOnset < endLimit #  and  (dat[timeMeasureReward]+stimulusOnset)*#only take certain trials
            usableInds = usableInds.squeeze()

            targetSpikes = targetSpikes[:, usableInds, :] # make sure neural activity matches now that some trials are removed
            feedbacktimes = dat[timeMeasureReward][usableInds]

            actionTimes = dat[timeMeasurePrediction][usableInds]

            # remove data where the timing for reward is earlier than, or equal to the response timing, do this from the timing arrays and spike data
            feedbacktimesNew = []
            actionTimesNew = []
            Inds = []
            if len(actionTimes) > len(feedbacktimes):
              rng = len(feedbacktimes)
            
            else:
              rng = len(actionTimes)
            for i in range(rng):
             
              if feedbacktimes[i] > actionTimes[i]:
                feedbacktimesNew.append(feedbacktimes[i])
                actionTimesNew.append(actionTimes[i])
                Inds.append(True)
              elif feedbacktimes[i]== actionTimes[i]:
              
                Inds.append(False)
              else:
   
                Inds.append(False)
            targetSpikes = targetSpikes[:, Inds, :] # make sure neural activity matches now that some trials are removed

            # Get window around reward for each trial
            windowIndsReward = [(int((respTime*100)+stimulusOnset)) for respTime in feedbacktimesNew]
            windowIndsPrediction = [(int(respTime*100)+stimulusOnset) for respTime in actionTimesNew]

            feedbackWindowsReward = np.zeros((len(targetInds), targetSpikes.shape[1], int(windowSizeReward)))
            feedbackWindowsPrediction = np.zeros((len(targetInds), targetSpikes.shape[1], int(windowSizePrediction)))
            for i in range(targetSpikes.shape[1]-1):


                rewardIndices = np.arange(windowIndsReward[i]-windowPreReward, windowIndsReward[i]+windowPostReward).astype('int')
                rewardWindow = targetSpikes[:, i, rewardIndices]
              
                predictionIndices = np.arange(windowIndsPrediction[i+1]-windowPrePrediction, windowIndsPrediction[i+1]+windowPostPrediction).astype('int')
               # print(predictionIndices)
                predictionWindow = targetSpikes[:, i+1, predictionIndices]

                # Average across neurons
                if len(predictionWindow) > 2 and len(rewardWindow) > 2:
                  predictionWindowMean = np.mean(predictionWindow, axis=0)
           
                  rewardWindowMean = np.mean(rewardWindow, axis=0)

                  dataStructure = np.array([predictionWindowMean.T, rewardWindowMean.T]).T

                  trialResults = grangercausalitytests(dataStructure, 28)

                  statsList.append(trialResults)
                else:

                  print(" ")

    # Return results list
    return statsList

results = get_accuracy(windowValsReward, windowValsPrediction)