import random

# Define the problem
cities = ['A', 'B', 'C', 'D', 'E']
distances = {
    'AB': 2, 'AC': 3, 'AD': 1, 'AE': 4,
    'BC': 4, 'BD': 2, 'BE': 3,
    'CD': 5, 'CE': 1,
    'DE': 4
}

# Generate initial population
def generate_chromosome():
    return random.sample(cities, len(cities))

population_size = 100
population = [generate_chromosome() for _ in range(population_size)]

# Define the fitness function
def calculate_distance(chromosome):
    distance = 0
    for i in range(len(chromosome) - 1):
        distance += distances[chromosome[i] + chromosome[i+1]]
    distance += distances[chromosome[-1] + chromosome[0]]
    return distance

def fitness(chromosome):
    return 1/calculate_distance(chromosome)

# Implement the genetic algorithm
def selection(population):
    population = sorted(population, key=fitness, reverse=True)
    return population[:int(len(population)/2)]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(cities) - 1)
    offspring1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    offspring2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]
    return offspring1, offspring2

def mutation(chromosome):
    mutation_point1, mutation_point2 = random.sample(range(len(cities)), 2)
    chromosome[mutation_point1], chromosome[mutation_point2] = chromosome[mutation_point2], chromosome[mutation_point1]
    return chromosome

def generate_new_population(population):
    new_population = []
    for i in range(len(population)):
        parent1, parent2 = random.sample(population, 2)
        offspring1, offspring2 = crossover(parent1, parent2)
        offspring1 = mutation(offspring1)
        offspring2 = mutation(offspring2)
        new_population.append(offspring1)
        new_population.append(offspring2)
    return new_population

# Iterate the genetic algorithm
num_generations = 1000
for i in range(num_generations):
    population = selection(population)
    population = generate_new_population(population)

# Print the best solution
best_chromosome = max(population, key=fitness)
print(best_chromosome)
print(calculate_distance(best_chromosome))

