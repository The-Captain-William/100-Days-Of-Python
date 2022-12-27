import pandas


class CountryCapture:
    def __init__(self, country_csv):
        self.states = pandas.read_csv(country_csv)
        self.state_series = self.states["state"]
        self.x_coor = self.states["x"]
        self.y_coor = self.states["y"]
        self.states_num = len(self.state_series)
