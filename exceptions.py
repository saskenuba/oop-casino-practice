class InvalidBet(Exception):
    def __init__(self, expression):
        "Player has left the table because his next bet would be more than this budget."
        self.expression = expression


class PlayerError(Exception):
    def __init__(self, expression):
        "docstring"
        self.expression = expression


class InvalidBin(Exception):
    def __init__(self, expression):
        "Used if a invalid bin is selected somehow"
        self.expression = expression
