import requests

def print_stats():
	stat_num = 0
	real_pokemon = True

	while real_pokemon:
		pokemon_id = raw_input('Please input Pokemon ID: ')

		try: 
			pokemon_url = 'http://pokeapi.co/api/v2/pokemon/' + pokemon_id
			response = requests.get(pokemon_url)
			pokemon = response.json()

			print "The base stats for " + str(pokemon['name']) + " are: "
			for stat in pokemon['stats']:
				if stat_num < len(pokemon['stats']):
					print pokemon['stats'][stat_num]['stat']['name'] + ": " + \
					str(pokemon['stats'][stat_num]['base_stat'])
					stat_num += 1

			real_pokemon = False

		except KeyError:
			print "Please input correct Pokemon ID."

print_stats()

