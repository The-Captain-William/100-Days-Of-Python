from game import Game
from country import CountryCapture

usa = CountryCapture("50_states.csv")

game = Game(country_image="50_states.csv", state_series=usa.state_series, states=usa.states)
