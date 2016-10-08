from random import randint

# Sample Database row
# Name	Type 1	Type 2	Total	HP	Attack	Defense	Sp. Attack	Sp. Def	Speed	Generation	Legendary

# Global variables
pop_size       = 100
stop_evolution = 1000
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
		rand = randint(1,100)
		if(randint < 5):
			rand_pokemon = randint(0,800)
			chrom[individual] = Pokemon.objects.all().filter(num=rand_pokemon)

def evaluate(chrom):
	for individual in chrom:

   return fitness

# Main 
# Initilize population
for x in range(0,pop_size):
	chrom = []

	for team_select in range(0,5):
		rand = randint(0,800)
		chrom.append(Pokemon.objects.all().filter(num=rand))

	population.append(chrom)

# Initial evaluation
for generation in range(0,stop_evolution):
	new_population = []
	for chrom in range(0,pop_size):
		# Select parents
		# Recombination
		child = recombination(chrom1, chrom2)
		
		# Mutation
		mutation(child)

		# Evaluation
		new_population.append(chrom1)

	for chrom in range
		# Select new population
