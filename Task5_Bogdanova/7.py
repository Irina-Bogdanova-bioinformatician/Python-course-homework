import json

with open("text_7.txt", "r") as firms:
    firms.seek(0)
    lines_list = firms.readlines()
    profit_dict = {}
    average_profit = 0
    number = 0
    loss_dict = {}
    for i in lines_list:
        a = i.split(" ")
        a.pop(1)
        b = int(a[1])
        c = int(a[2])
        profit = b - c
        if profit >= 0:
            profit_dict[a[0]] = profit
            average_profit += profit
            number += 1
        else:
            loss_dict[a[0]] = profit
    average_dict = {"average_profit": (average_profit / number)}
    final_list = [profit_dict, average_dict, loss_dict]
    print(final_list)
    with open("firms_analytics.json", "w") as final_effort:
        json.dump(final_list, final_effort)
