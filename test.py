import json_parser

def test():
    json_parser.generate_file(2)
    file_path = "test.json"
    localdata = json_parser.load_json(file_path)
    print(localdata)
    json_parser.add("key1", "value1", localdata)
    print(localdata)

    json_parser.updateValue("name", "NEW_VALUE", localdata["school"])
    print(localdata)

    if localdata["key1"] != "value1" or localdata["school"]["name"] != "NEW_VALUE":
        return False
    json_parser.delete_key("age", localdata["student"])
    print(localdata)
    if localdata.get("age"):
        return False 
    return True

print(test())