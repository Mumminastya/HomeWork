import json

def task_7():
    with open('text_task7.txt', 'r') as file:
        firm_prof = {}
        aver_prof = {}
        total_prof = float(0)
        firm_index = 0
        for line in file:
            firm_mas = line.split()
            firm_name = firm_mas[0]
            profit = int(firm_mas[2]) - int(firm_mas[3])
            if profit > 0:
                total_prof = total_prof + profit
            firm_index = firm_index + 1
            firm_prof.update ({firm_name: profit})
        aver_prof.update ({"avg_profit": total_prof / firm_index})
        #print(aver_prof)
        result = [firm_prof, aver_prof]
        #print(result)
    with open('task7_result.txt', 'w') as file_json:
        json.dump(result, file_json)