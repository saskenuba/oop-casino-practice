import math


class IntegerStatistics:
    """Computes several simple descriptive statistics of Integer values
    in a list."""

    @staticmethod
    def mean(values):
        return sum(values) / len(values)

    @staticmethod
    def stdev(listOfValues):
        mean = IntegerStatistics.mean(listOfValues)
        sominha = 0

        for value in listOfValues:
            diferenca = value - mean
            sominha += diferenca ** 2
        variance = sominha / (len(listOfValues) - 1)
        stdeviation = math.sqrt(variance)

        return stdeviation
