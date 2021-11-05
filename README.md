# ACIT4610_CartPole_Control
Instruction to run the program
- main.py is the main file --> entry point of the program
- All the configuration parameters are define in config.py file
- Change parameters in config file before run the main.py file


Parameter to change in config.py file
- Which model you want to run (MODEL)
- Which encoding method you want to use (METHOD)
- Define number of rules you want to have (NUMBER_OF_RULES)
- Define number of generation you want to have (NUMBER_OF_GENERATIONS)
- How many time you want to want to test each rule (RULE_ITERATION)
- How many times you want to allow the model to change the cell before taking action (ITERATION_CA)
- How many neighbors you want to have in 1DCA and 2DCA (NEIGHBOURS)
- Note: In case of 2DCA, neighbors 3 means 3x3 neighbors
- Change the mutation rate of evolutionary algorithm (MUTATION_RATE)
- Change optimization type(RM/RCM) (MUTATION_TYPE)
- Note: network model has only RM optimization, We didn't get time to implement crossover


Features
- train_model saved the three rules that gives highest fitness value based on mininum, average and maximum fitness value
- test_model control the cartpole environment based on based rules
