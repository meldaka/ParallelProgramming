my_list = [8, 9, 765]
my_tuple = (7, 9, 11, 876)
my_set = {0, 11, 455}
my_dict = {"name":"Elon", "Surname":"Musk", "Brand":"Tesla", 222:777}

def remove_duplicates(my_list):
    return list(set(my_list))

def list_counts(my_list: list) -> dict:
    dict_ = dict.fromkeys(my_list, 0)
    for item in my_list:
        dict_[item] += 1
    return dict_

def reverse_dict(my_dict: dict) -> dict:
    return {value: key for key, value in my_dict.items()}
