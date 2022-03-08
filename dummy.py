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
    out_string += s




with open('Milestone1B.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)   
print('-'*30)




json_object = json.dumps(data, indent=3)
print(json_object)
file = open('Milestone1B_log.txt', mode='w')
for key, value in data.items():
    
    c = 0
    #print(key," ",value)
    
    if(value['Execution'] =='Sequential'):
        out_string += str(now + timedelta(0, more))+';'
        out_string += key + ' Entry\n'
        c = 0
        for ke, valu in value['Activities'].items():
            c += 1
        
            
            out_string += str(now + timedelta(0, more))+';'
            out_string += f'''{key}.{ke} Entry\n'''
            #more += int(valu['Inputs']['ExecutionTime'])
            #threads = []

    elif(value['Execution']=='Concurrent'):
         
         threads = []
         out_string += str(now + timedelta(0, more))+';'
         out_string += key + ' Entry\n'

         c = 0
         for ke, valu in value['Activities'].items():
            c += 1
            command = str(now + timedelta(0, more))+';'
            
            t1 = threading.Thread(target=execute, args=(command,))
            t1.start()
            threads.append(t1)
            for k, va in valu['Activities'].items():
                out_string += str(now + timedelta(0, more))+';'
                out_string += f'{key}.{ke}.{k} Entry\n'
                command = f'''{key}.{ke}.{k} Executing {va['Function']} ({va['Inputs']['FunctionInput']}, {va['Inputs']['ExecutionTime']})\n'''
                execute(command)
                
                more += int(va['Inputs']['ExecutionTime'])
                out_string += str(now + timedelta(0, more))+';'
                out_string += f'{key}.{ke}.{k} Exit\n'
                for t in threads:
                    t.join()
            out_string += str(now + timedelta(0, more))+';'
            out_string += f'''{key}.{ke} Exit\n'''
            break


            
            
            

                

        


print(out_string)
file.write(out_string)
file.close()