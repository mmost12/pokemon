import random
import gap
from evo.models import Pokemon

# def run(pop_size, stop_evolution, k_tournament):
def small():
	return gap.run(2, 1, 2)

def med():
	return gap.run(10, 1, 3)

def big():
	return gap.run(100, 100, 10)

def long():
	return gap.run(100, 500, 10)

def fight(chrom_list, i, j):
	A_team = chrom_list[i]
	B_team = chrom_list[j]
	a = 0
	b = 0
	report = []
	play   = []
	for pokemon in chrom_list[i]:
		play.append(pokemon)
	report.append(play)

	play = []
	for pokemon in chrom_list[j]:
		play.append(pokemon)
	report.append(play)

	first = 'a' if A_team[a].speed > B_team[b].speed else 'b'
	a_hp = A_team[a].hp
	b_hp = B_team[b].hp

	while a < 6 and b < 6:
		if first == 'a':
			taken = gap.attack(A_team[a], B_team[b])
			b_hp -= taken
			play = []
			play.append("Attack")
			play.append(A_team[a].name)
			play.append(B_team[b].name)
			play.append(str(int(taken)))
			report.append(play)
			if b_hp <= 0:
				play = []
				play.append("Defeat")
				play.append(A_team[a].name)
				play.append(B_team[b].name)
				report.append(play)
				b+=1
				if b >= 6:
					break
				b_hp = B_team[b].hp
				first = 'a' if A_team[a].speed > B_team[b].speed else 'b'
			else:
				taken = gap.attack(B_team[b], A_team[a])
				a_hp -= taken
				play = []
				play.append("Attack")
				play.append(B_team[b].name)
				play.append(A_team[a].name)
				play.append(str(int(taken)))
				report.append(play)
		else:
			taken = gap.attack(B_team[b], A_team[a])
			a_hp -= taken
			play = []
			play.append("Attack")
			play.append(B_team[b].name)
			play.append(A_team[a].name)
			play.append(str(int(taken)))
			report.append(play)
			if a_hp <= 0:
				play = []
				play.append("Defeat")
				play.append(B_team[b].name)
				play.append(A_team[a].name)
				report.append(play)
				a+=1
				if a >= 6:
					break
				a_hp = A_team[a].hp
				first = 'a' if A_team[a].speed > B_team[b].speed else 'b'
			else:
				taken = gap.attack(A_team[a], B_team[b])
				b_hp -= taken
				play = []
				play.append("Attack")
				play.append(A_team[a].name)
				play.append(B_team[b].name)
				play.append(str(int(taken)))
				report.append(play)

	return report

def show_fight():
	population = []
	for x in range(2):
		chrom = []

		for team_select in range(6):
			rand_pokemon = random.randint(1,800)
			chrom.append(Pokemon.objects.get(no=rand_pokemon))

		population.append(chrom)
	return fight(population, 0, 1)