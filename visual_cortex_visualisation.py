"""
Gets list of visual cortex neurons, 
then plots heatmap of average response for each, average response of all, and average response for each on same axes
"""
dat = dict
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