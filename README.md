# backtothefuture

Team members: 
[Conor Keogh](https://github.com/conorkeogh),
[Holly Wilson](https://github.com/hWils),
[Saptarshi Ghosh](https://github.com/amisapta15),
[Siobhan Hall](https://github.com/SMHall94)

---
### Overview of task:
Animals update their behavioural strategies based on feedback to their decisions. Decoding strategies have demonstrated neural activity related to decision making. Similarly, feedback-related responses are well-established in electrophysiological data. Frameworks such as “predictive coding”, supported by evidence from sensory perception, have been proposed to unify prediction and feedback where an internal “model” of the external world is updated based on error. It remains unclear, however, how this feedback-related activity is integrated with predictive activity.

Demonstrating a relationship between predictive activity and reward activity on the previous trial would show that the brain “integrates” reward information to inform decision making. This would imply that some internal state is updated, providing electrophysiological support for models of decision making based on internal predictions. More specifically, we expect to find that the magnitude of neural responses vary as a function of correct vs. incorrect trials as a reflection of the error signal. We will consider a combination of regions of interest  to investigate differential encoding of feedback through different functional areas.

**Dataset** (reference paper): [Steinmetz](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6913580/) 

---
## Aim 
Determine whether feedback integration from a task (performed correctly with a reward, versus incorrectly with an auditory punishment) is evident in the subsequent task

----
## Hypothesis
Feedback integration from a task is used to update predictions in the subsequent trials (single trial history)

---
## Objectives
The methodology is further expanded within the code available at the following links:
- [Load data](https://github.com/SMHall94/backtothefuture/blob/master/load_data.py) 
- [Data exploration](https://github.com/SMHall94/backtothefuture/blob/master/visual_cortex_visualisation.py): Visualisation of the data
- [Decode feedback and prediction information](https://github.com/SMHall94/backtothefuture/blob/master/logistic_regression.py)
- [Determine optimal window](https://github.com/SMHall94/backtothefuture/blob/master/optimal_window.py) for decoding
- [Granger causality](https://github.com/SMHall94/backtothefuture/blob/master/pairwise_granger_causality.py) to compare reward[t] to response[t+1] where 't' corresponds to a relative trial 

---
## Results
#### Top ten areas for decoding reward and response respectively (ranked by percentage accuracy)
_Reward:_ 'MEA' (cortical subplate), 'CA' (hippocampus), 'PT' (thalamus), 'MOp' (motor cortex), 'PAG' (midbrain), 'RT' (thalamus), 'COA' (motor cortex), 'BMA' (cortical subplate), 'CA2' (hippocampus), 'LSr' (basal ganglia)
![brainrewarddecodable](https://user-images.githubusercontent.com/47060850/88845722-7ab64f80-d1dc-11ea-83af-b27d4d9d5bdf.png)


_Response:_ 'VISrl' (visual) , 'MG' (thalamus), 'NB' (midbrain) , 'CA2', (hippocampus) 'SPF' (thalamus), 'PIR' (motor cortex), 'CA' (hippocampus), 'EPd'(cortical subplate), 'POL'(thalamus), ' TT' (motor cortex)
![brainresponsedecodable](https://user-images.githubusercontent.com/47060850/88845966-d2ed5180-d1dc-11ea-9cec-b02ac2c86e45.png)



#### Best time windows for decoding reward and response within the respective brain areas
_Reward:_ 0.0 to 1.1 (timelocked to reward at time 0.0)

_Response:_ -0.8 to 0.0 (timelocked to the response at 0.0)

#### Granger causality
The following links directly to the the 'CA' brain areas within the hippocampus - chosen as it is the area with the highest decoding accuracy for both response and reward.


---
## (Tentative) conclusion
Our results show there may be an association between reward and response in single trial history


