import pandas as pd
from deap import base, creator, tools, algorithms
import operator
import random
import numpy as np

# Create random Datatest
num_rows = 10
num_columns = 5
# Generate random data
random_data = np.random.rand(num_rows, num_columns)
# Create the dataframe
df = pd.DataFrame(random_data, columns=[f'Column{i}' for i in range(1, num_columns+1)])
df['Result'] = df['Column1']/4 + df['Column3'] - df['Column4']

# Load file dataset
#df = pd.read_csv('xxxxx.csv')
#df = df.loc[:,['Column0', 'Column1', 'Column2', 'Result']]

# Add column call Four (full of fours in the second position of dataframe)
df.insert(1, 'Four', 4) 
# Randomly switch or shuffle the columns
columns = df.columns.tolist()
shuffled_columns = np.random.permutation(columns)
data = df[shuffled_columns]
# Remove column to adjust
data = data.drop('Result', axis=1)

# Generate column names based on dataset columns
column_names = list(data.columns)
print(column_names)

# Keep track of what operators did the fit use
global_operators = []

# Define the fitness function
def evaluate(individual):
    # Select columns based on individual's genes
    selected_columns = [column for column, gene in zip(column_names, individual) if gene]

    # Check if at least one column is selected
    if len(selected_columns) == 0:
        global_operators.append([]) # Had no operators
        return float('inf'),  # Return infinite fitness if no columns are selected
    #print(selected_columns)

    # Perform mixing function on selected columns and keep operators
    operators = []
    result = data[selected_columns[0]]
    for column in selected_columns[1:]:
        operator_func = random.choice(['+', '-', '*', '/'])#, '//', '**', 'np.log'] Randomly select an operator
        operators.append(operator_func)
        #print(operator_func)
        result = eval(f"result {operator_func} data[column]")  # Evaluate the expression dynamically
    #print(result)
    
    # Calculate mean squared error & save operators used
    mse = np.mean((result - df['Result']) ** 2)
    global_operators.append(operators)
    #print(mse)
    #print(global_operators)

    return mse,  # Return MSE as fitness value (tuple with comma)

def main():
    population_size = 25
    num_generations = 10

    # Define the individual and population
    creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
    creator.create('Individual', list, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    toolbox.register('attribute', random.randint, 0, 1)  # Binary genes
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attribute, n=len(data.columns))
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    # Register the necessary DEAP operators
    toolbox.register('evaluate', evaluate)
    toolbox.register('select', tools.selTournament, tournsize=3)
    toolbox.register('mate', tools.cxTwoPoint)
    toolbox.register('mutate', tools.mutFlipBit, indpb=0.05)

    population = toolbox.population(n=population_size)
    hall_of_fame = tools.HallOfFame(maxsize=10)

    # Track the best individual and its operators
    best_individual = None
    best_operators = None
    best_fitness = float('inf')

    for generation in range(num_generations):

        # Mutate the population over generations
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

        # Evaluate the fitness of offspring
        fitnesses = toolbox.map(toolbox.evaluate, offspring)
        #print(offspring)

        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit
        
        # Update the hall_of_fame with the best individuals
        hall_of_fame.update(offspring)  

        current_best_individual = hall_of_fame[0]
        current_best_fitness = current_best_individual.fitness.values[0]

        # Search for best operators in offspring
        for idx, item in enumerate(offspring):
            if item == hall_of_fame[0]:
                current_best_oper = (idx)

        # Update the best individual and its operators if necessary
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_individual = current_best_individual
            best_operators = current_best_oper + (generation*len(offspring))

        print(f"Generation {generation+1}: Best Fitness = {best_fitness}")

    return best_individual, best_operators, best_fitness, hall_of_fame


if __name__ == '__main__':
    best_individual, best_operators, best_fitness, hall_of_fame = main()

    print("Hall of Fame:")
    for idx, individual in enumerate(hall_of_fame):
        columns = [column for column, gene in zip(data.columns, individual) if gene]
        print(f"Individual {idx+1}: Columns={columns}")

    print("Best individual:")
    selected_columns = [column for column, gene in zip(data.columns, best_individual) if gene]
    selected_operators = global_operators[best_operators]
    print("Selected Columns:", selected_columns)
    print("Selected Operators:", selected_operators)
    print("Fitness obtain:", best_fitness)
