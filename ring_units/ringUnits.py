
def unitsOfRing(n):
	units = 0

	for u in range(n):
		for v in range(n):
			if (u * v) % n == 1:
				units += 1
				break

	return units

def main():
	mappings = []

	for i in range(2, 50):
		units = unitsOfRing(i)

		mappings.append( (i, units) ) 

	mappings.sort(key=lambda x: x[1]/x[0])

	for n, units in mappings:
		print(f"n = {n:>2} units = {units:>2} percentage = {units/n * 100:.1f}")

if __name__ == '__main__':
	main()
