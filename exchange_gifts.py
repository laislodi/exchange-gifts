import random

def read_file() -> list:
    list_of_people = []
    with open("input.csv", "r") as file:
        _ = file.readline()
        for line in file:
            name, email = line.replace("\n", "").split(",")
            person = (name, email)
            list_of_people.append(person)
    return list_of_people


def exchange_gifts(list_of_people: list) -> dict:
    matches = {}
    random.shuffle(list_of_people)
    for index in range(0, len(list_of_people)):
        if index + 1 == len(list_of_people):
            matches[list_of_people[index]] = list_of_people[0]
        else:
            matches[list_of_people[index]] = list_of_people[index + 1]
    return matches


def print_result(matches: dict) -> None:
    for key, value in matches.items():
        print(f"{key[0]} ({key[1]}) -> {value[0]} ({value[1]})")


emails = read_file()
matches = exchange_gifts(list_of_people=emails)
print_result(matches=matches)
