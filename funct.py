import json_parser

def show_keys(dictionary):
    return dictionary.keys()

def key_dict(dictionary):
    key_list = []
    for key in dictionary:
        if (isinstance(dictionary.get(key), dict)):
            key_list.append(key)

    return key_list

def add_key_value(filename):
    res = json_parser.load_json(filename)
    key_list = res
    print(list(key_dict(key_list)))
    while isinstance(key_list.get(tmp := input("Choose key from this list or input new key: ").strip()), dict):
        key_list = key_list.get(tmp)
        print(list(key_dict(key_list)))
    val = input("Input value for new key: ")
    if not json_parser.add(tmp,val,key_list):
        print("Key excists")
        return
    json_parser.write_dict_to_file(res)

def update_value(filename):
    res = json_parser.load_json(filename)
    tmp_dict = res
    print(list(tmp_dict.keys()))
    while (tmp := tmp_dict.get(key := input("Choose one key from this list whose value you want to change: "))) and isinstance(tmp, dict):
        number = input("If you want to update the value of the selected key, enter 1. If you want to update a value within a nested dictionary, enter 2: ")
        print(list(tmp.keys()))
        if number == "1":
            break
        if number == "2":
            tmp_dict = tmp
    if not tmp:
        print("Wrong key")
        return
    value = input("Input new value: ")
    json_parser.updateValue(key, value, tmp_dict)
    json_parser.write_dict_to_file(res)

def delete_value(filename):
    res = json_parser.load_json(filename)
    tmp_dict = res
    print(list(tmp_dict.keys()))
    while (tmp := tmp_dict.get(key := input("Choose one key from this list which you want to delete: "))) and isinstance(tmp, dict):
        number = input("If you want to delete the value of the selected key, enter 1. If you want to delete a value within a nested dictionary, enter 2: ")
        print(list(tmp.keys()))
        if number == "1":
            json_parser.delete_key(key, tmp_dict)
            json_parser.write_dict_to_file(res)
            return    
        if number == "2":
            tmp_dict = tmp
    if not tmp:
        print("Wrong key")
        return
    json_parser.delete_key(key, tmp_dict)
    json_parser.write_dict_to_file(res)