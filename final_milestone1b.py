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


def flow_seq(key,value):
    out_string += str(now + timedelta(0, more))+';'
    out_string += f'''{key}.{ke} Entry\n'''
    for ke,valu in value['Activities']:
        out_string += str(now + timedelta(0, more))+';'
        out_string += f'''{key}.{ke} Entry\n'''
        command = f'''{key}.{ke} Executing {valu['Function']} ({valu['Inputs']['FunctionInput']}, {valu['Inputs']['ExecutionTime']})\n'''
        execute(command)


def flow_con(key,value):
    threads=[]
    out_string += str(now + timedelta(0, more))+';'
    out_string += f'''{key}.{ke} Entry\n'''
    for ke,valu in value['Activities']:
        out_string += str(now + timedelta(0, more))+';'
        out_string += f'''{key}.{ke} Entry\n'''
        command = f'''{key}.{ke} Executing {valu['Function']} ({valu['Inputs']['FunctionInput']}, {valu['Inputs']['ExecutionTime']})\n'''
        execute(command)
        t1 = threading.Thread(target=execute, args=(command,))
        t1.start()
        threads.append(t1)
        for t in threads:
            t.join()






with open('Milestone1B.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)   
print('-'*30)

json_object = json.dumps(data, indent=3)
print(json_object)
file = open('Milestone1B_log.txt', mode='w')
for key, value in data.items():
    if(value['Type']=='Flow' and value['Execution']=='Sequential'):
        flow_seq(key,value)
    
        c=0
        for ke, valu in value['Activities'].items():
            c+=1
            if c == 3:
                flow_seq(ke,valu)
            
            
                for k, va in valu['Activities'].items():
                    
                    flow_seq(k,va)
                # out_string += f'\nMore = {more}\n'
                    
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
        
        
            
            
print(out_string)
file.write(out_string)
file.close()