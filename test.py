import gap

# def run(pop_size, stop_evolution, k_tournament):
def small():
	return gap.run(2, 1, 2)

def med():
	return gap.run(10, 1, 3)

def big():
	return gap.run(100, 100, 10)

def long():
	return gap.run(100, 500, 10)