import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data[field]


def liner_search(sequence, number):
    index = 0
    positions = []
    while index < len(sequence):
        if sequence[index] == number:
            positions.append(index)
        index = index + 1
    count = len(positions)
    return {"positions": positions, "count": count}


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    search = liner_search(sequential_data, 5)
    print(search)

if __name__ == '__main__':
    main()