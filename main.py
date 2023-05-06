from mdp import MDP

transition_matrix = {
    "0": {
        "east": [(0.3, "0"), (0.7, "hazard")],
        "southeast": [(0.2, "hazard"), (0.8, "4")],
        "south": [(1.0, "3")]
    },
    "hazard": {
        "east": [(1.0, "goal")],
        "south": [(0.4, "goal"), (0.6, "4")]
    },
    "goal": {},
    "3": {
        "east": [(1.0, "3")]
    },
    "4": {
        "west": [(0.5, "3"), (0.5, "4")],
        "east": [(1.0, "5")]
    },
    "5": {
        "west": [(1.0, "4")],
        "north": [(0.2, "5"), (0.8, "goal")]
    }
}

initial_state = "0"

terminal_states = ["goal"]

rewards = {
    "hazard": -5,
    "goal": 10
}

mdp = MDP(initial_state, terminal_states, transition_matrix, rewards)

print("Reward from state hazard: " + 
      str(mdp.get_reward("hazard")))

print("Possible Actions from state hazard: " + 
      str(mdp.get_possible_actions("hazard")))

print("State space: " + 
      str(mdp.get_states()))

print("Action space: " + 
      str(mdp.get_actions()))

print("Transtions from action southeast in state 0: " + 
      str(mdp.get_transitions("0", "southeast")))

print("Moving from 0 with action east gets us to: " + 
      str(mdp.step("0", "east")))