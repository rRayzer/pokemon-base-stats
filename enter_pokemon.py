import requests

def enter_team():
	real_pokemon = True
	team = []
	pokedex = []

	for num in range(1, 5):	
		response = requests.get('http://pokeapi.co/api/v2/pokemon/' + str(num))	
		pokemon = response.json()	
		pokedex.append(pokemon['name'])

	while real_pokemon:
		pokemon_name = raw_input("Enter Pokemon ('x' to exit): ")

		if pokemon_name in pokedex:
			team.append(pokemon_name)
		elif pokemon_name == 'x':
			print "Your team is: " + '\n' + str(team)
			real_pokemon = False
		elif pokemon_name != pokedex:
			print "Please input correct Pokemon name."


enter_team()

"""
Generation I: range(1, 152)
Generation II: range(152, 252)
Generation III: range(252, 387)
Generation IV: range(387, 494)
Generation V:  range(494, 650)
Generation VI : range(650, 722)

"""




