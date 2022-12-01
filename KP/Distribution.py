from KP.Function import Function
from KP.Terminal import Terminal


def process(terminals, functions):
    functions_list = [i for i in functions if isinstance(i, Function)]
    terminals_list = [i for i in terminals if isinstance(i, Terminal)]
    for i in range(len(functions_list)):
        now_function = functions_list.pop(0)
        for j in range(len(terminals_list)):
            if (sum(terminals_list[j].functions_capacity) + now_function.capacity <= terminals_list[
                j].capacity) and now_function.equipment not in [i.equipment for i in terminals_list[j].functions if
                                                                isinstance(i, Function)]:
                if len(now_function.streams - terminals_list[j].functions_streams) > 0:
                    if len(terminals_list[j].functions_streams) + \
                            len(now_function.streams - terminals_list[j].functions_streams) < terminals_list[j].streams:
                        terminals_list[j].functions.append(now_function)
                        terminals_list[j].functions_capacity.append(now_function.capacity)
                        terminals_list[j].functions_streams.update(
                            now_function.streams - terminals_list[j].functions_streams)
                        break
                    else:
                        continue
                else:
                    terminals_list[j].functions.append(now_function)
                    terminals_list[j].functions_capacity.append(now_function.capacity)
                    break


def process_pack(terminals, functions):
    functions_list = [i for i in functions if isinstance(i, Function)]
    terminals_list = [i for i in terminals if isinstance(i, Terminal)]
    calculations = dict()
    while len(functions_list) > 0:
        for i in range(len(functions_list)):
            for j in range(len(terminals_list)):
                if sum(terminals_list[j].functions_capacity) + functions_list[i].capacity <= \
                        terminals_list[j].capacity and len(terminals_list[j].functions_streams) + len(
                    functions_list[i].streams - terminals_list[j].functions_streams) <= \
                        terminals_list[j].streams:
                    calculations[str(j) + "_" + str(i)] = functions_list[i].capacity + len(
                        functions_list[i].streams - terminals_list[j].functions_streams) + 100 * (
                                                              [k.equipment for k in terminals_list[j].functions if
                                                               isinstance(k, Function)].count(
                                                                  functions_list[i].equipment))
        para = sorted(calculations.items(), key=lambda group: (group[1], group[0]))[0]
        calculations.clear()
        now_function = functions_list.pop(int(para[0].split("_")[1]))
        now_terminal = terminals_list[int(para[0].split("_")[0])]
        now_terminal.functions.append(now_function)
        now_terminal.functions_capacity.append(now_function.capacity)
        now_terminal.functions_streams.update(now_function.streams - now_terminal.functions_streams)
