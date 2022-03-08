import os
import yaml
import json
import threading
from datetime import datetime, timedelta

out_string = ''

more = 0
now = datetime.now()

def execute(s):
    global out_string
    global more
    out_string += str(datetime.now() + timedelta(0, more))+';'
    out_string += s





with open('Milestone1A.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)   
print('-'*30)

json_object = json.dumps(data, indent=3)
print(json_object)
file = open('Milestone1A_log.txt', mode='w')
for key, value in data.items():
    out_string += str(now + timedelta(0, more))+';'
    out_string += key + ' Entry\n'
    c = 0
    for ke, valu in value['Activities'].items():
        c += 1
        if c == 3:
            out_string += str(now + timedelta(0, more))+';'
            out_string += f'''{key}.{ke} Entry\n'''
            threads = []
            for k, va in valu['Activities'].items():
                out_string += str(now + timedelta(0, more))+';'
                out_string += f'{key}.{ke}.{k} Entry\n'
                
                command = f'''{key}.{ke}.{k} Executing {va['Function']} ({va['Inputs']['FunctionInput']}, {va['Inputs']['ExecutionTime']})\n'''
                execute(command)
                more += int(va['Inputs']['ExecutionTime'])
                out_string += str(now + timedelta(0, more))+';'
                out_string += f'{key}.{ke}.{k} Exit\n'
            out_string += str(now + timedelta(0, more))+';'
            out_string += f'''{key}.{ke} Exit\n'''
            break
        out_string += str(now + timedelta(0, more))+';'
        out_string += f'{key}.{ke} Entry\n'
        
        command = f'''{key}.{ke} Executing {valu['Function']} ({valu['Inputs']['FunctionInput']}, {valu['Inputs']['ExecutionTime']})\n'''
        execute(command)
        more += int(valu['Inputs']['ExecutionTime'])
        out_string += str(now + timedelta(0, more))+';'
        out_string += f'{key}.{ke} Exit\n'
    out_string += str(now + timedelta(0, more))+';'
    out_string += key + ' Exit\n'

file.write(out_string)
file.close()