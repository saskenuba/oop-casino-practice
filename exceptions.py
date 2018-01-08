class InvalidBet(Exception):
    def __init__(self, expression):
        "docstring"
        self.expression = expression
