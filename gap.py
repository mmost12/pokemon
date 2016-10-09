import random
from type_chart import type_adv
from evo.models import Pokemon

# Global variables
pop_size       = 100
stop_evolution = 1000
k_tournament   = 10
population     = []

def recombination(chrom1, chrom2):
	return chrom1[:3] + chrom2[3:]

def mutation(chrom):
	for p in range(len(chrom)):
		rand = random.randint(1,100)
		if(rand <= 5):
			rand_pokemon = random.randint(1,800)
			chrom[p]     = Pokemon.objects.get(no=rand_pokemon)
	return chrom

def evaluate(chrom_list):
	chrom_wins = [0] * len(chrom_list)

	for i in range(len(chrom_list)):
		for j in range(i):
			chrom_wins[fight(chrom_list, i, j)] += 1

	pairs = [(chrom_wins[i], i) for i in range(len(chrom_wins))]

	return chrom_list[sorted(pairs)[::-1][0][1]]

def fight(chrom_list, i, j):
	A_team = chrom_list[i]
	B_team = chrom_list[j]
	a = 0
	b = 0

	first = a if A_team[a].speed > B_team[b].speed else b
	a_hp = A_team[a].hp
	b_hp = B_team[b].hp

	while a < 6 and b < 6:
		if first == a:
			b_hp -= attack(A_team[a], B_team[b])
			if b_hp <= 0:
				b+=1
				if b >= 6:
					break
				b_hp = B_team[b].hp
				first = a if A_team[a].speed > B_team[b].speed else b
			else:
				a_hp = attack(B_team[b], A_team[a])
		else:
			a_hp -= attack(B_team[b], A_team[a])
			if a_hp <= 0:
				a+=1
				if a >= 6:
					break
				a_hp = A_team[a].hp
				first = a if A_team[a].speed > B_team[b].speed else b
			else:
				b_hp = attack(A_team[a], B_team[b])

	return i if a > b else j

def attack(attack, defend):
	atk_ratio = attack.attack / defend.defense
	sp_ratio = attack.spatk / defend.spdef

	ratio = atk_ratio if atk_ratio > sp_ratio else sp_ratio

	type1_modifier = 1
	type2_modifier = 1

	if((attack.type1, defend.type1) in type_adv):
		type1_modifier *= type_adv[(attack.type1, defend.type1)]
	if((attack.type1, defend.type2) in type_adv):
		type1_modifier *= type_adv[(attack.type1, defend.type2)]

	if((attack.type2, defend.type1) in type_adv):
		type2_modifier *= type_adv[(attack.type2, defend.type1)]
	if((attack.type2, defend.type2) in type_adv):
		type2_modifier *= type_adv[(attack.type2, defend.type2)]

	type_modifier = type1_modifier if type1_modifier > type2_modifier else type2_modifier

	return 35.2 * ratio * type_modifier



# Sample Database row
#   	Name			Type 1	Type 2	Total		HP		Attack	Defense	Sp. Attack	Sp. Def	Speed	Generation	Legendary
# 1	Bulbasaur	Grass		Poison	318		45		49			49			65				65			45		1				FALSE

# no =      models.IntegerField()
# name =    models.CharField(max_length=200)
# type1 =   models.CharField(max_length=200)
# type2 =   models.CharField(max_length=200)
# total =   models.IntegerField()
# hp =      models.IntegerField()
# attack =  models.IntegerField()
# defense = models.IntegerField()
# spatk =   models.IntegerField()
# spdef =   models.IntegerField()
# speed =   models.IntegerField()

# -------------
#     Main 
# -------------
random.seed()

# Initilize population
for x in range(pop_size):
	chrom = []

	for team_select in range(6):
		rand_pokemon = random.randint(1,800)
		chrom.append(Pokemon.objects.get(no=rand_pokemon))

	population.append(chrom)

print("Population Initilized, beginning evolution...\n")
for generation in range(stop_evolution):
	if generation != 0 and generation % 10 == 0:
		print("Gen:",generation)
	new_population = []
	for chrom in population:

		# Select k chroms to have a tournament
		chrom_list_1 = []
		chrom_list_2 = []
		for k in range(k_tournament):
			rand_pokemon = random.randint(0,pop_size-1)
			chrom_list_1.append(population[rand_pokemon])

			rand_pokemon = random.randint(0,pop_size-1)
			chrom_list_2.append(population[rand_pokemon])

		# Recombination & Mutation
		child = mutation(recombination(evaluate(chrom_list_1),evaluate(chrom_list_2)))
		new_population.append(child)

	population = new_population

print("Best team found after", stop_evolution, "generations")
for pokemon in population[0]:
	print(pokemon.name)
