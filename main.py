import funct

if __name__ == "__main__":
    while True:
        print("Choose one of this variants")
        print("1. Add key")
        print("2. Update value of key")
        print("3. Delete key")
        print("4. Exit")

        number_variant = input()
        
        if number_variant == "1":
            funct.add_key_value("test.json")        

        if number_variant == "2":
            funct.update_value("test.json")

        if number_variant == "3":
            funct.delete_value("test.json")

        if number_variant == "4":
            break


