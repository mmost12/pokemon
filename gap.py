from random

# Sample Database row
# Name	Type 1	Type 2	Total	HP	Attack	Defense	Sp. Attack	Sp. Def	Speed	Generation	Legendary

# Global variables
pop_size       = 100
stop_evolution = 1000
k_tournament   = 10
population     = []

def recombination(chrom1, chrom2):
	child = []  
	for individual in range(0,2):
		child = chrom1[individual]
	for individual in range(3,5):
		child = chrom2[individual]
	return child

def mutation(chrom):
	for individual in chrom:
		rand = random.randint(1,100)
		if(rand <= 5):
			rand_pokemon = random.randint(0,800)
			chrom[individual] = Pokemon.objects.all().filter(num=rand_pokemon)
	return chrom

def evaluate(chrom):
	for individual in chrom:

   return fitness

# Main 
random.seed()

# Initilize population
for x in range(0,pop_size):
	chrom = []

	for team_select in range(0,5):
		rand = random.randint(0,800)
		chrom.append(Pokemon.objects.all().filter(num=rand))

	population.append(chrom)

# Initial evaluation
for generation in range(0,stop_evolution):
	new_population = []
	for chrom in population:
		# Select parents
		chrom1 = population[]
		chrom2 = population[]

		# Recombination & Mutation
		child   = mutation(recombination(chrom1,chrom2))
		fitness = evaluate(child)

		fitness_pair = (fitness, child)
		new_population.append(fitness_pair)

	for chrom in new_population:
		heap = []
		for add in range(1,k_tournament):
			rand_pokemon = random.randint(0,pop_size)
			heap.append(new_population[rand_pokemon])
		heap.sort(key=lambda tup: tup[0])

		population[chrom] = heap[-1]