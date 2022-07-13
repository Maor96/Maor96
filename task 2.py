import re
from datetime import datetime, timedelta
from task1 import *

# Task a: 
def read_log():
    b_r = []
    with open('Maor_auth.log', 'r') as f:
        for line in f:
            if line != '\n':
                b_r.append(line)
            else:
                pass
    return b_r

# Task b:
def get_user_names(log_list):

    user_names = []

    for line in log_list:
        if '  user=' in line:
            user_names.append(line[line.find('  user=')+7:-2])

    return list(set(user_names))

# Task c:
def get_address(log_list):
    
    ip = []

    for line in log_list:
        x = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if x:
            ip.append(x[0])

    
    return list(set(ip))

# Task d:
def start_end(log_list):
    log_list[0] = log_list[0].split(' ')
    log_list[-1] = log_list[-1].split(' ')

    start = log_list[0][0]+' '+log_list[0][1]+' '+log_list[0][2]
    end = log_list[-1][0]+' '+log_list[-1][1]+' '+log_list[-1][2]

    return start+' - '+end

# Task e:
def duration(str):

    lst = str.split(' ')
    start = lst[2]
    end = lst[6]
    start = datetime.strptime(start, '%H:%M:%S')
    end = datetime.strptime(end, '%H:%M:%S')
    duration = end - start

    return duration

# Task f:
def country_check(country_dict, ip_lst):
    dict1 = {}

    for ip in ip_lst:
        x = ip.split('.')
        x = x[0]+'.'+ x[1]+'.'+x[2]+'.'
        for key, value in country_dict.items():
            for i in value:
                if x in i:
                    dict1[ip] = key
                    break
    return dict1
        

if __name__ == "__main__":
    print("task A: \n",read_log())
    print("task B: \n",get_user_names(read_log()))
    print("task C: \n",get_address(read_log()))
    print("task D: \n",start_end(read_log()))
    print("task E: \n",duration(start_end(read_log())))
    print("task F: \n",country_check(read_ranges(), get_address(read_log())))
