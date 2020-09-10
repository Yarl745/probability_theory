from random import randint


def get_probability(checking_times: int) -> float:
	count = 0

	for time in range(checking_times):
		count += 1 if (randint(0, 255) + randint(0, 255)) > 255 else 0

	return count/checking_times


if __name__ == '__main__':
	probability = get_probability(1000)
	print(probability)