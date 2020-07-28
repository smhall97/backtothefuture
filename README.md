# backtothefuture

Team members: 
[Conor Keogh](https://github.com/conorkeogh),
[Holly Wilson](https://github.com/hWils),
[Saptarshi Ghosh](https://github.com/amisapta15),
[Siobhan Hall](https://github.com/SMHall94)

### Overview of task:
Animals update their behavioural strategies based on feedback to their decisions. Decoding strategies have demonstrated neural activity related to decision making. Similarly, feedback-related responses are well-established in EEG. Frameworks such as “predictive coding”, supported by evidence from sensory perception, have been proposed to unify prediction and feedback where an internal “model” of the external world is updated based on error. It remains unclear, however, how this feedback-related activity is integrated with predictive activity.

Demonstrating a relationship between predictive activity and reward activity on the previous trial (or previous n trials with some weighting) would show that the brain “integrates” reward information to inform decision making. This would imply that some internal state is updated, providing electrophysiological support for models of decision making based on internal predictions. More specifically, we expect to find that the magnitude of neural responses vary as a function of correct vs. incorrect trials as a reflection of the error signal. We will consider a combination of regions of interest deemed to be relevant in past literature as well as novel brain regions, to investigate differential encoding of feedback through different functional areas.

**Dataset** (reference paper): [Steinmetz](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6913580/) 

## Aim 
Determine whether feedback integration from a task (performed correctly with a reward, versus incorrectly with an auditory punishment) is evident in the subsequent task

## Hypothesis
Feedback integration from a task is used to update predictions in the subsequent trials (single trial history)

## Objectives
- [Load data](https://github.com/SMHall94/backtothefuture/blob/master/load_data.py) 
- [Data exploration](https://github.com/SMHall94/backtothefuture/blob/master/visual_cortex_visualisation.py): Visualisation of the data
- [Decode feedback and prediction information](https://github.com/SMHall94/backtothefuture/blob/master/logistic_regression.py)
- [Determine optimal window](https://github.com/SMHall94/backtothefuture/blob/master/optimal_window.py) for decoding
- [Granger causality](https://github.com/SMHall94/backtothefuture/blob/master/pairwise_granger_causality.py)

## Methodology and result summary

## Results and discussion

## Conclusion