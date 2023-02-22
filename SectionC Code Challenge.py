
def resistor(net):

    def res(resistors):
        if type(resistors) == list:
            return 1 / sum(1 / res(parallel) for parallel in resistors)
        if type(resistors) == tuple:
            return sum(res(series) for series in resistors)
        return resistors

    return round(res(eval(net)), 1)

    print(resistor("(10, [20, 30])"))
    print(resistor("[([(470, 1000), 330], 470), 680]"))
    print(resistor("[10, 20, [30, (40, 50), 60, (70, 80)], 90]"))
    print(resistor("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"))
    print(resistor("([([(470, 680), 330], 1000), 470], 680)"))



