# Define Encoding Related Parameters
# choose encoding method
METHOD = 'mix' # or limit_base or mix or prob_base

# if encoding method is prob_base
PROB_ITERATION = 2

# if encoding method is value_base
VALUE_ENCODE_LIMIT = [0.1, 0.2]

# Define Cellular Automata Related Parameters
NEIGHBOURS = 5
ITERATION_CA = 3

# Main program Iteration
NUMBER_OF_RULES = 20
NUMBER_OF_GENERATIONS = 100
RULE_ITERATION = 5

# Define number of parents for optimization
PARENTS = 2