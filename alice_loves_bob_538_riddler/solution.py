def test(k, inc):
	posA = 0.0
	posB = 0.0

	a = inc * k

	time = 0.0
	aliceDec = False

	while(True):

		if aliceDec:
			posA -= a
		else:
			posA += a

		posB += inc

		if posA >= 10:
			posA -= posA - 10
			aliceDec = True

		if aliceDec:
			if posA > posB:
				time += inc
			else:
				return time + posB - posA


def main():
	inc = 0.001
	incK = 0.0001
	k = 2.4
	
	bestTime = 0
	bestK = 1.0

	while(k < 2.5):
		time = test(k, inc)

		if time > bestTime:
			bestTime = time
			bestK = k

		k += incK

	print("Best K = " + str(bestK))

if __name__ == "__main__":
	main()



