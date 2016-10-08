import random
from evo.models import Pokemon

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
			# chrom[individual] = Pokemon.objects.all().filter(num=rand_pokemon)
			chrom[individual] = Pokemon(no=rand_pokemon)
	return chrom

def evaluate(chrom_list):
	chrom_wins = [0] * len(chrom_list)

	for i in range(chrom_list):
		for j in range(i):
			chrom_wins[fight(chrom_list, i, j)] += 1

	pairs = [(chrom_wins[i], i) for i in range(len(chrom_wins))]

	return chrom_list[sorted(pairs)[::-1][0][1]]

def fight(chrom_list, i, j):
	fitness = 12
	return fitness

# Sample Database row
# Name	Type 1	Type 2	Total	HP	Attack	Defense	Sp. Attack	Sp. Def	Speed	Generation	Legendary

# -------------
#     Main 
# -------------
random.seed()

# Initilize population
for x in range(0,pop_size):
	chrom = []

	for team_select in range(0,5):
		rand_pokemon = random.randint(0,800)
		chrom.append(Pokemon(no=rand_pokemon))

	population.append(chrom)

# Initial evaluation
for generation in range(0,stop_evolution):
	new_population = []
	for chrom in population:

		# Select k chroms to have a tournament
		chrom1 = []
		chrom2 = []
		for k in range(1,k_tournament):
			rand_pokemon = Random.randint(0,800)
			chrom1.append(population[rand_pokemon])

			rand_pokemon = Random.randint(0,800)
			chrom2.append(population[rand_pokemon])

		# Recombination & Mutation
		# child = mutation(recombination(evaluate(chrom1),evaluate(chrom2)))
		child = mutation(recombination(chrom1[0],chrom2[0]))
		new_population.append(child)

	population = new_population