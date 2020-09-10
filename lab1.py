import copy
import random


def get_amounts_of_each_coin(_kinds_amount: int) -> list:
	_amounts_of_each_coin = list()
	for number_of_coin in range(_kinds_amount):
		_amounts_of_each_coin.append(input_int(f'Введите кол-во {number_of_coin+1}-ой монеты: '))
	return _amounts_of_each_coin


def input_int(text: str) -> int:
	while True:
		out_int = input(text)
		if out_int.isdigit():
			return int(out_int)


def get_probability(checking_times: int) -> float:
	kinds_amount = input_int('Ведите количество видов монет в кармане: ')
	getting_amount = input_int('Введите сколько каждой монеты вы должны достать из кармана: ')
	total_number_of_coins = kinds_amount * getting_amount
	amounts_of_each_coin = get_amounts_of_each_coin(kinds_amount)

	all_coins = []

	for kind_of_coin in range(kinds_amount):
		for coin_number in range(amounts_of_each_coin[kind_of_coin]):
			all_coins.append({'kind_of_coin': kind_of_coin})

	successful_attempts = 0
	for time in range(checking_times):

		temporary_coins_model = copy.deepcopy(all_coins)
		getting_kind_coins = [0 for kind_of_coin in range(kinds_amount)]

		for number_of_coin in range(total_number_of_coins):
			# When there are no coins left
			try:
				coin = random.choice(temporary_coins_model)
			except IndexError:
				break

			getting_kind_coins[coin['kind_of_coin']] += 1

			if getting_kind_coins[coin['kind_of_coin']] > getting_amount:
				break

			temporary_coins_model.remove(coin)

		else:
			successful_attempts += 1

	return successful_attempts/checking_times



if __name__ == '__main__':
	probability = get_probability(1000000)
	print(f'Вероятность: {probability}')





