"""
Written by Conor Keogh (https://github.com/conorkeogh)

This step helps with the visualisation of a brain area.
The code at present is set up to visualise the visual cortex which is useful in this task, on account of the visual 
component of the task.
Order of operations:
1. Create list of visual cortex neurons, 
2. Plots heatmap of average response for each, average response of all, and average response for each on same axes
"""
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np

sns.set()


dat = {} # Load from Steinmetz data: https://github.com/SMHall94/backtothefuture/blob/master/load_data.py

# Get list of visual cortex neurons
visual_cortex_neurons = []
i = 0
for index, neuron in enumerate((dat['brain_area'])):
 # print(neuron)
  if neuron in ["VISa", "VISam", "VISl", "VISp", "VISpm", "VISrl"]:
    visual_cortex_neurons.append(index)
# Get spike data at visual cortex neurons
shortened_spike_array = dat['spks'][visual_cortex_neurons]
# Try plotting functions
meanResponse = np.mean(shortened_spike_array, axis = 1) # Mean over trials -> neurons x time
# Make a big figure
fig, ax = plt.subplots(figsize=(20,10))
# Try heatmat of data (requires "import seaborn as sns" then "sns.set()" - this is just a high level wrapper for Matplotlib)
sns.heatmap(meanResponse) # Plot heatmap
# Plot average response of all neurons
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(np.mean(meanResponse,axis=0)) # Average response of all visual cortex neurons
# Loop through each neuron and plot all on same axis
fig, ax = plt.subplots(figsize=(20,10))
for neuron in meanResponse:
    ax.plot(np.arange(0, 250), neuron)


def getNeurons(dat, areas):
    target_neurons = []
    i = 0
    for index, neuron in enumerate((dat['brain_area'])):
        # print(neuron)
        if neuron in areas:
            target_neurons.append(index)

    return target_neurons

"""
Plot activity of all neurons
"""

visareas = ["VISa", "VISam", "VISl", "VISp", "VISpm", "VISrl"]
visual_cortex_neurons = getNeurons(dat, visareas)

# Get spike data at visual cortex neurons
shortened_spike_array = dat['spks'][visual_cortex_neurons]

# Try plotting functions
meanResponse = np.mean(shortened_spike_array, axis = 1) # Mean over trials -> neurons x time

# Make a big figure
fig, ax = plt.subplots(figsize=(20,10))

# Try heatmat of data (requires "import seaborn as sns" then "sns.set()" - this is just a high level wrapper for Matplotlib)
sns.heatmap(meanResponse) # Plot heatmap

# Plot average response of all neurons
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(np.mean(meanResponse,axis=0)) # Average response of all visual cortex neurons

# Loop through each neuron and plot all on same axis
fig, ax = plt.subplots(figsize=(20,10))
for neuron in meanResponse:
    ax.plot(np.arange(0, 250), neuron)

"""
Reproduce Steinmetz figure 4 - timelock to reward
"""