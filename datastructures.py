my_list = ["toyota", "bmw", "subaru", "range", "nissan"]
my_list.append("G-wagon")
print(my_list)
print(my_list[0])
my_list[1] = "Mercedes"       # mutable
print(my_list[1], "is manufactured in Germany.")


list_2 = ["17", "19", "21", "23"]
list_2.insert(1, "16")
list_2.extend(my_list)
print(list_2)

# tuple datastructure
my_tuple = ("Banana", "Oranges", "Mangoes", "Apples", "Grapes")
print(my_tuple)
print(f"i like eating {my_tuple[3]}")

# set datastructure
my_set = {"Kenya", "Uganda", "Tanzania", "Ethiopia"}
print(my_set)


# dictionary datastructure
my_dictionary = {"Name": "Alvin", "Age": 18, "Gender": "Male"}
print(my_dictionary)
print(my_dictionary["Name"])
print(my_dictionary["Age"])
print(my_dictionary["Gender"])
