import numpy as np

R = np.matrix([[-1, -1, -1, -1, 0, -1],
               [-1, -1, -1, 0, -1, 100],
               [-1, -1, -1, 0, -1, -1],
               [-1, 0, 0, -1, 0, -1],
               [0, -1, -1, 0, -1, 100],
               [-1, 0, -1, -1, 0, 100]])
#print(R)


gamma = 0.8


Q = np.zeros([6, 6])
#print(Q)


#initial_state = 1


def find_available_actions(state):
    current_row = R[state, :] #all columns in state row
    
    available_actions = np.where(current_row >= 0) [1]
    #available_actions = np.where(current_row >= 0)
    
    return available_actions


def find_next_action(available_actions):
    #pick 1 value from avaiable_actions randomly, and assign that to next_action   
    next_action = int(np.random.choice(available_actions, 1))

    return next_action


def update_Q(current_state, next_action, gamma):
    available_actions = find_available_actions(next_action)
    max_index = max(Q[next_action, available_actions])

    Q[current_state, next_action] = R[current_state, next_action] + gamma * max_index


for i in range(1000):
    current_state = np.random.randint(0, 6)
    available_actions = find_available_actions(current_state)
    next_action = find_next_action(available_actions)
    update_Q(current_state, next_action, gamma)


Q = Q / np.max(Q) * 100
Q = np.round(Q)


#available_actions = find_available_actions(initial_state)
#next_action = find_next_action(available_actions)
#update_Q(current_state, next_action, gamma)

#print(find_available_actions(initial_state))
#print(find_next_action(available_actions))


print('=== TRAINED Q MATRIX ===')
print(Q)

