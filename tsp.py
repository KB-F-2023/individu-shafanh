import random

# Define the cities and their coordinates
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 1),
    'D': (5, 0),
    'E': (6, 3),
    'F': (7, 1),
    'G': (10, 0),
    'H': (11, 3),
    'I': (12, 1),
    'J': (15, 0)
}

# Define the genetic algorithm parameters
POPULATION_SIZE = 20
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.1

# Define the fitness function
def get_fitness(route):
    distance = 0
    for i in range(len(route)):
        from_city = cities[route[i]]
        to_city = cities[route[(i + 1) % len(route)]]
        distance += ((from_city[0] - to_city[0]) ** 2 + (from_city[1] - to_city[1]) ** 2) ** 0.5
    return 1 / distance

# Define the create initial population function
def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        route = list(cities.keys())
        random.shuffle(route)
        population.append(route)
    return population

# Define the breed function
def breed(parent1, parent2):
    child = [''] * len(parent1)
    gene1 = random.randint(0, len(parent1) - 1)
    gene2 = random.randint(0, len(parent1) - 1)
    start_gene = min(gene1, gene2)
    end_gene = max(gene1, gene2)
    for i in range(start_gene, end_gene + 1):
        child[i] = parent1[i]
    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(child)):
                if child[j] == '':
                    child[j] = parent2[i]
                    break
    return child

# Define the mutate function
def mutate(route):
    if random.random() < MUTATION_RATE:
        gene1 = random.randint(0, len(route) - 1)
        gene2 = random.randint(0, len(route) - 1)
        route[gene1], route[gene2] = route[gene2], route[gene1]
    return route

# Define the evolve function
def evolve(population):
    # Select the top 2 routes
    sorted_population = sorted(population, key=get_fitness, reverse=True)
    parents = sorted_population[:2]

    # Breed and mutate to create new routes
    offspring = [parents[0], parents[1]]
    while len(offspring) < POPULATION_SIZE:
        child = breed(parents[0], parents[1])
        child = mutate(child)
        offspring.append(child)

    return offspring

# Define the main function
def main():
    # Create the initial population
    population = create_population()

    # Evolve the population for a number of generations
    for i in range(NUM_GENERATIONS):
        population = evolve(population)

    # Calculate the fitness of each individual in the final population
    fitness_scores = []
    for individual in population:
        fitness_scores.append(get_fitness(individual))

    # Sort the population by their fitness
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]

    # Print the best route
    best_route = sorted_population[0]
    print("Best route:", best_route)

if __name__ == '__main__':
    main()
