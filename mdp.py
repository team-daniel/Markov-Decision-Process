import random

class MDP:
    def __init__(self, initial_state, terminal_states, 
                 transitions = {}, reward = None):
        # Set arguments
        self.initial_state = initial_state
        self.actions = self.set_actions(transitions)
        self.states = self.get_states_from_transitions(transitions)
        self.terminal_states = terminal_states
        self.transitions = transitions
        if self.transitions == {}:
            print("Warning: Transition matrix is empty!")       
        if reward:
            self.reward = reward
        else:
            self.reward = {s : 0 for s in self.states}

    # Set all actions from the transition matrix into the action space
    def set_actions(self, transitions):
        actions = []
        for state in transitions.keys():
            actions.extend(transitions[state])
        return list(set(actions))
    
    # Get all actions from the action space
    def get_actions(self):
        return self.actions
        
    # Retrieve all the states from the transition matrix given
    def get_states_from_transitions(self, transitions):
        if isinstance(transitions, dict):
            first_state = set(transitions.keys())
            second_state = set([t[1] for 
                                actions in transitions.values()
                               for effects in actions.values() 
                               for t in effects])

            return first_state.union(second_state)
        else:
            print("Warning: Could not find states from transitions!")
            return None
        
    # Get all states in the state space
    def get_states(self):
        return self.states

    # Return the reward for this state
    def get_reward(self, state):
        return self.reward[state]
    
    # Get all transitions for this state action pair
    def get_transitions(self, state, action):
        if action is None:
            return [(0.0, state)]
        else: 
            return self.transitions[state][action]
        
    # Get all possible actions from a certain state
    def get_possible_actions(self, state):
        if state in self.terminal_states:
            return [None]
        else:
            return list(self.transitions[state])
        
    # Move from a state with an action
    def step(self, state, action):
        if state in self.states:
            if action in self.get_possible_actions(state):
                transitions = self.get_transitions(state, action)
                if len(transitions) > 1:
                    trans_probs = [t[0] for t in transitions]
                    trans_states = [t[1] for t in transitions]
                    new_state = random.choices(trans_states, trans_probs, k=1)
                    return new_state
                else:
                    return transitions[0][1]
            else:
                print("Warning: Action cannot be taken from this state!")
                return state
        else:
            print("Warning: State not in MDP!")
            return None