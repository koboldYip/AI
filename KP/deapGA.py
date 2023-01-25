import random

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

IND_INIT_SIZE = 5
MAX_ITEM = 50
MAX_WEIGHT = 50
NBR_ITEMS = 20

items = {0: (17, {"IW1C", "IW2C", "IAT1C"}, "main", "K1C"),
         1: (17, {"IW1C", "IW2C", "IAT1C"}, "secondary", "K1C"),
         2: (17, {"IW3C", "IW4C", "IAT2C"}, "main", "K2C"),
         3: (17, {"IW3C", "IW4C", "IAT2C"}, "secondary", "K2C"),
         4: (13, {"IW1C", "W1C-TV2"}, "main", "W1C"),
         5: (13, {"IW2C", "W2C-TV2"}, "main", "W2C"),
         6: (13, {"IW3C", "W3C-TV2"}, "main", "W3C"),
         7: (13, {"IW4C", "W4C-TV2"}, "main", "W4C"),
         8: (11, {"IW1W2C", "IW1C", "W1C-TV1"}, "secondary", "W1C"),
         9: (11, {"IW1W2C", "IW1C", "W1C-TV2"}, "secondary", "W1C"),
         10: (11, {"IW1W2C", "IW2C", "W2C-TV1"}, "secondary", "W2C"),
         11: (11, {"IW1W2C", "IW2C", "W2C-TV2"}, "secondary", "W2C"),
         12: (11, {"IW3W4C", "IW3C", "W3C-TV1"}, "secondary", "W3C"),
         13: (11, {"IW3W4C", "IW3C", "W3C-TV2"}, "secondary", "W3C"),
         14: (11, {"IW3W4C", "IW4C", "W4C-TV1"}, "secondary", "W4C"),
         15: (11, {"IW3W4C", "IW4C", "W4C-TV2"}, "secondary", "W4C"),
         16: (12, {"IAT1C", "IAT1K", "IAT1E"}, "main", "AT1"),
         17: (12, {"IAT1C", "IAT1K", "IAT1E"}, "main", "AT1"),
         18: (9, {"IAT1C", "IAT1E", "K1C-TV1", "TV1E"}, "secondary", "AT1"),
         19: (9, {"IAT1K", "TV1K"}, "secondary", "AT1"),
         20: (12, {"IAT2C", "IAT2K", "IAT2E"}, "main", "AT2"),
         21: (12, {"IAT2C", "IAT2K", "IAT2E"}, "main", "AT2"),
         22: (9, {"IAT2C", "IAT2E", "K1C-TV2"}, "secondary", "AT2"),
         23: (9, {"IAT2K", "TV2K"}, "secondary", "AT2"),
         24: (14, {"IQC4E", "IW8E", "IAT1E", "IW6E", "IQC1E"}, "main", "K1E"),
         25: (14, {"IQC2E", "IW4E", "IAT2E", "IW3E", "IQC3E"}, "main", "K2E"),
         26: (14, {"IQC1E", "IW2E", "IAT3E", "IW1E", "IQC3E"}, "main", "K3E"),
         27: (14, {"IQC4E", "IW7E", "IAT4E", "IW5E", "IQC2E"}, "main", "K4E"),
         28: (9, {"IQC1E", "TV1E", "TV3E"}, "main", "QC1E"),
         29: (9, {"IQC2E", "TV4E", "TV2E"}, "main", "QC2E"),
         30: (9, {"IQC3E", "TV3E", "TV2E"}, "main", "QC3E"),
         31: (9, {"IQC4E", "TV1E", "TV4E"}, "main", "QC4E"),
         32: (16, {"IW1E", "TV3E"}, "main", "W1E"),
         33: (16, {"IW2E", "TV3E"}, "main", "W2E"),
         34: (16, {"IW3E", "TV2E"}, "main", "W3E"),
         35: (16, {"IW4E", "TV2E"}, "main", "W4E"),
         36: (16, {"IW5E", "TV4E"}, "main", "W5E"),
         37: (16, {"IW6E", "TV1E"}, "main", "W6E"),
         38: (16, {"IW7E", "TV4E"}, "main", "W7E"),
         39: (16, {"IW8E", "TV1E"}, "main", "W8E"),
         40: (11, {"IW1E", "TV3E"}, "main", "W1E"),
         41: (13, {"IW2E", "TV3E"}, "main", "W2E"),
         42: (13, {"IW3E", "TV2E"}, "main", "W3E"),
         43: (11, {"IW4E", "TV2E"}, "main", "W4E"),
         44: (11, {"IW5E", "TV4E"}, "main", "W5E"),
         45: (11, {"IW6E", "TV1E"}, "main", "W6E"),
         46: (11, {"IW7E", "TV4E"}, "main", "W7E"),
         47: (11, {"IW8E", "TV1E"}, "main", "W8E"),
         48: (12, {"IAT3E", "IAT3G", "IAT3K"}, "main", "AT3"),
         49: (12, {"IAT3E", "IAT3G", "IAT3K"}, "main", "AT3"),
         50: (12, {"IAT4E", "IAT4G", "IAT4K"}, "main", "AT4"),
         51: (12, {"IAT4E", "IAT4G", "IAT4K"}, "main", "AT4"),
         52: (9, {"IAT3E", "IAT3G", "TV3E", "TV1G"}, "secondary", "AT3"),
         53: (9, {"IAT3K", "TV3K"}, "secondary", "AT3"),
         54: (9, {"IAT4E", "IAT4G", "TV4E", "TV2G"}, "secondary", "AT4"),
         55: (9, {"IAT4K", "TV4K"}, "secondary", "AT4"),
         56: (14, {"IAT3G", "IW1G", "IW3G", "IW5G", "IQC1G"}, "main", "K1G"),
         57: (14, {"IAT4G", "IW2G", "IW4G", "IW5G", "IQC1G"}, "main", "K2G"),
         58: (9, {"IQC1G", "TV1G", "TV2G"}, "main", "QC1G"),
         59: (16, {"IW1G", "TV1G"}, "main", "W1G"),
         60: (16, {"IW2G", "TV2G"}, "main", "W2G"),
         61: (16, {"IW3G", "TV1G"}, "main", "W3G"),
         62: (16, {"IW4G", "TV2G"}, "main", "W4G"),
         63: (16, {"IW5G", "TV1G"}, "main", "W5G"),
         64: (16, {"IW6G", "TV2G"}, "main", "W6G"),
         65: (16, {"IW1G", "TV1G"}, "secondary", "W1G"),
         66: (16, {"IW2G", "TV2G"}, "secondary", "W2G"),
         67: (16, {"IW3G", "TV1G"}, "secondary", "W3G"),
         68: (16, {"IW4G", "TV2G"}, "secondary", "W4G"),
         69: (16, {"IW5G", "TV1G"}, "secondary", "W5G"),
         70: (16, {"IW6G", "TV2G"}, "secondary", "W6G"),
         71: (6, {"ITN1", "TV1K"}, "main", "TN1"),
         72: (6, {"ITN2", "TV2K"}, "main", "TN2"),
         73: (6, {"ITN3", "TV1K"}, "main", "TN3"),
         74: (6, {"ITN4", "TV2K"}, "main", "TN4"),
         75: (9, {"IQC1K", "TV1K", "TV2K"}, "main", "QC1K"),
         76: (9, {"IQC4K", "TV3K", "TV4K"}, "main", "QC4K"),
         77: (7, {"IW412K", "TV4K"}, "main", "W412K"),
         78: (7, {"IW410K", "TV4K"}, "main", "W410K"),
         79: (7, {"IW409K", "TV4K"}, "main", "W409K"),
         80: (7, {"IW408K", "TV4K"}, "main", "W408K"),
         81: (7, {"IW407K", "TV4K"}, "main", "W407K"),
         82: (7, {"IW405K", "TV4K"}, "main", "W405K"),
         83: (7, {"IW404K", "TV4K"}, "main", "W404K"),
         84: (7, {"IW303K", "TV3K"}, "main", "W303K"),
         85: (7, {"IW304K", "TV3K"}, "main", "W304K"),
         86: (7, {"IW305K", "TV3K"}, "main", "W305K"),
         87: (7, {"IW306K", "TV3K"}, "main", "W306K"),
         88: (7, {"IW307K", "TV3K"}, "main", "W307K"),
         89: (7, {"IW309K", "TV3K"}, "main", "W309K"),
         90: (7, {"IW310K", "TV3K"}, "main", "W310K"),
         91: (7, {"IW312K", "TV3K"}, "main", "W312K"),
         92: (9, {"IAT1K", "TV1K"}, "secondary", "AT1"),
         93: (9, {"IAT2K", "TV2K"}, "secondary", "AT2"),
         94: (9, {"IAT3K", "TV3K"}, "secondary", "AT3"),
         95: (9, {"IAT4K", "TV4K"}, "secondary", "AT4")
         }

items1 = items.copy()

creator.create("Fitness", base.Fitness, weights=(1.0, 1.0, 0.00000001, 0.00000001))
creator.create("Individual", set, fitness=creator.Fitness)

toolbox = base.Toolbox()

toolbox.register("attr_item", random.choice, list(items1.keys()))

toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_item, IND_INIT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evalKnapsack(individual):
    eqpfl = False
    capacity = 0
    equipment = []
    streams = set()
    for item in individual:
        if item in items1:
            capacity += int(items1[item][0])
            if items1[item][3] in equipment:
                eqpfl = True
                break
            else:
                equipment.append(items1[item][3])
            streams.update(items1[item][1])
    if len(streams) > 20 or capacity > 100 or len(individual) > 14 or eqpfl:
        return 0, 0, 0, 0
    return capacity, len(streams), 0, 0


def cxSet(ind1, ind2):
    temp = set(ind1)
    ind1 &= ind2
    ind2 ^= temp
    return ind1, ind2


def mutSet(individual):
    if random.random() < 0.5:
        if len(individual) > 0:
            individual.remove(random.choice(sorted(tuple(individual))))
    else:
        individual.add(random.choice(list(items1.keys())))
    return individual,


toolbox.register("evaluate", evalKnapsack)
toolbox.register("mate", cxSet)
toolbox.register("mutate", mutSet)
toolbox.register("select", tools.selNSGA2)


def main():
    # random.seed(32)
    NGEN = 50
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()

    population, logbook = algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN,
                                                    halloffame=hof)

    return population, logbook, hof


if __name__ == "__main__":
    result = []
    while len(items1) > 0:
        capacity = 0
        streams = set()
        pop, logbook, hof = main()
        for item in hof.items[0]:
            if item in items:
                capacity += int(items[item][0])
                streams.update(items[item][1])
        if capacity > 100 or len(streams) > 20:
            continue
        result.append(hof.items[0])
        for i in hof.items[0]:
            if i in items1:
                del items1[i]
    print(len(result))
    for i in result:
        capacity = 0
        streams = set()
        functions = []
        print(i)
        for item in i:
            if item in items:
                functions.append(items[item][3] + " " + items[item][2])
                capacity += int(items[item][0])
                streams.update(items[item][1])
        print(functions)
        print(capacity)
        print(len(streams))
