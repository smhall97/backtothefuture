"""
This script was written @hWils (Holly Wilson)
This RL algorithm determines whether the mouse behaviour can be modelled using reinforcement learning.
In this specific case q-learning has been implemented and the conditions are treated as discrete. 
Having run the model, it computes the similarity between the RL model's choices and the mouse's actual choices
"""

import numpy as np

states = [0,1,2,3,4,5] #0=no stimuli, #1=equal but not zero #2=left only #3=right only #4=left higher #5=right higher
action = [0,1,2] #0=left 1=no-go 2=right
reward =[-1,1]
#gamma = 0.9 # discounting
q_values = np.zeros(len(states)*len(action))
q_values = q_values.reshape(6,3)
print(q_values)
alpha = 0.1
epsilon = 0.95 # how often it does greedy choice
mouse_action = dat['response'] +1 # to make it 0,1,2 rather than -1,0,1
mouse_reward = np.array(dat['feedback_type'])
#mouse_action = fake_mouse_data
models_actions = []


state = [0.2,0.8]

condition = np.zeros(340)
for trial in range(340):
  right = dat['contrast_right'][trial]
  left = dat['contrast_left'][trial]
  if right > left and left > 0: #both present but right higher contrast
    condition[trial] = 5
  elif left > right and right >0: # both present but left is higher
    condition[trial] = 4
  elif left == 0 and right ==0: # no stimuli are present
      condition[trial] = 0
  elif right >0 and left==0: # right is present and left is not
      condition[trial] = 3
  elif left > 0 and right ==0: # left is present and right is not
      condition[trial] = 2
  elif left == right:
    condition[trial] =1



def q_learn_update(state,action,reward):
  #print(state, action)
  old_q = q_values[state][action]
  prediction_error = reward - old_q   #+ gamma*(np.max(q_values[new_state])) 
  new_q = old_q + (alpha * prediction_error)
  q_values[state][action] = new_q

# still need model to predict an action - so can compare later the similaities
def choose_action(state):
  rando = np.random.uniform(0,1)
  if rando > epsilon: #greedy policy
    action = np.argmax(q_values[int(state)])

  else:  #random policy
    action = np.random.randint(0,3)
  models_actions.append(action)
  return action

def compare_mouse_model():
  #print(len(condition == np.array(models_actions)))
  
  same = np.sum(mouse_action == models_actions)  # comparison
  return same

def run_model(ts):
  for i in range(ts):
    mouse_state = condition[i]
    choose_action(mouse_state) # saved in function
    q_learn_update(int(mouse_state),int(mouse_action[i]), int(mouse_reward[i]))

"""
#to run without vague states
toKeep = condition < 4
condition = condition[toKeep]
mouse_action = mouse_action[toKeep]
mouse_reward =mouse_reward[toKeep]
"""

run_model(len(condition))
#models_actions = np.zeros(340)



# here we compute the similarity between the RL and the beheavioural data
similarity = compare_mouse_model()


