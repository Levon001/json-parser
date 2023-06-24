import copy
import random

def load_json(filename):
    res = ""
    with open(filename, 'r') as file:
        res = file.read()
    if not res:
        return dict()
    res = res.strip()
    while (index := res.find('true')) != -1:
        res = res[:index] + 'True' + res[index+4:]
    return eval(res)



def tryEval(val):
    res = None
    try:
        res = eval(val)
    except Exception:
        res = val
    finally:
        return res
    
def myRepr(self):
    self = tryEval(self)
    if type(self) == str:
        return str('\"' + self + '\"')
    return type(self).__repr__(self)

    
def write_dict_to_file(data_dict,filename):
    clean_file(filename)
    with open(filename, 'w') as f:
        f.write("{\n")
        for key, value in data_dict.items():
            if isinstance(value, dict):
                f.write('\t"' + key + '": {\n')
                for k, v in value.items():
                    if isinstance(v, dict):
                        f.write('\t\t"' + k + '": {\n')
                        for ke, va in v.items():
                            if ke == list(v.keys())[-1]:
                                f.write(f'\t\t\t"{ke}": {myRepr(va)}\n')
                            else:                            
                                f.write(f'\t\t\t"{ke}": {myRepr(va)},\n')
                        if k == list(value.keys())[-1]:
                            f.write('\t\t}\n')
                        else:
                            f.write('\t\t},\n')
                    else:
                        if k == list(value.keys())[-1]:
                            f.write(f'\t\t"{k}": {myRepr(v)}\n')
                        else:   
                            f.write(f'\t\t"{k}": {myRepr(v)},\n') 
                if key == list(data_dict.keys())[-1]:
                    f.write('\t}\n')
                else:    
                    f.write('\t},\n')
            else:
                if key == list(data_dict.keys())[-1]:
                    f.write(f'\t"{key}": {myRepr(value)}\n')
                else:        
                    f.write(f'\t"{key}": {myRepr(value)},\n')
        f.write("}")


def add(key, value, dict_tmp):
    if dict_tmp.get(key):
        return False
    dict_tmp[key] = value
    return True

def updateValue(key, value, dict_tmp):
    if not dict_tmp:
        return False
    if not dict_tmp.get(key):
        return False
    dict_tmp.update({key:value})
    return True

def delete_key(key,dictionary):
    if not dictionary:
        return False
    if not dictionary.get(key):
        return False
    del dictionary[key]
    return True

def clean_file(file_path):
    with open(file_path, 'w') as file:
        file.truncate()

def generate_json_file(count):
    dictionary = {}
    for i in range(count):
        dictionary["key" + str(i+1)] = "val" + str(i+1) 

    dictionary["key" + str(i+1)] = copy.deepcopy(dictionary)    
    return dictionary

def generate_Json_file_containing(num, i=1):
    res = {}
    if i > num:
        return res
    if i < num:
        res["key" + str(i)] = "val" + str(i)
        res.update(generate_Json_file_containing(num, i + 1))

    if i == num:
        last_dict = {}
        for j in range(num):
            last_dict["key" + str(j+1)] = "value" + str(j+1)
        res["key" + str(i)] = last_dict

    return res

def generate_file(count):
    for i in range(count):
        random_number = random.randint(1, 10)
        filename = f"file{i+1}.json"
        write_dict_to_file(generate_Json_file_containing(random_number),filename)
        

