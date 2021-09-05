def put_number(s = ""):
    index = s.find("(")
    if (index == -1):
        return ""
    ss = s[:index]
    return ss

def task_6():
    with open('text_task6.txt', encoding = 'utf-8', mode='r') as file:
        result = {}
        for line in file:
            subj = line.split()
            subj_name = subj[0]
            subj_hours = 0
            for elem in subj:
                s = put_number(elem)
                if (s != ""):
                    subj_hours = subj_hours + int(s)
            result.update({subj_name: subj_hours})
        print(result)