# Define Encoding Related Parameters
# choose encoding method
# possible value : cart_position_velocity, pole_angle_velocity, cart_pole, limit_base or mix or prob_base
METHOD = 'pole_angle_velocity'

# if encoding method is prob_base
PROB_ITERATION = 2

# if encoding method is value_base
VALUE_ENCODE_LIMIT = [0.1, 0.2]
REPEAT = 1

# Define parameter related to bins encoding
BINS = 10
POLE_ANGLE = 0.13
POLE_VELOCITY = 0.75
CART_POSITION = 1.25
CART_VELOCITY = 1.25

# Define Cellular Automata Related Parameters
NEIGHBOURS = 3
ITERATION_CA = 5

# Main program Iteration
NUMBER_OF_RULES = 10
NUMBER_OF_GENERATIONS = 10
RULE_ITERATION = 5

# Define number of parents for optimization
PARENTS = 4

# Define mutation rate
MUTATION_RATE = 0.05

# define model
MODEL = 'NX' # possible values: CA or NX
