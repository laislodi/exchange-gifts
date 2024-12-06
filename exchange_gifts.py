
import random
import yagmail
import os
from dotenv import load_dotenv

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


def send_emails(matches: dict, organizer_name: str, organizer_email: str, organizer_password: str) -> None:
    load_dotenv()
    if organizer_email is None or organizer_email == "":
        organizer_email = os.getenv("EMAIL_ADDRESS")
    if organizer_password is None or organizer_password == "":
        organizer_email = os.getenv("EMAIL_PASSWORD")
    yag = yagmail.SMTP(organizer_email, organizer_password)
    body = """
Hello {you}!

You are receiving this email because you participated in a Gift Exchange!

Ask your friend {organizer} if you want to know more!

Here is the person you got: {name} ({email})
    """
    for giver, receiver in matches.items():
        giver_name = giver[0]
        giver_email = giver[1]
        receiver_name = receiver[0]
        receiver_email = receiver[1]
        yag.send(giver_email, 'Exchange Gifts!', [body.format(you=giver_name, organizer=organizer_name, name=receiver_name, email=receiver_email)])
        # print(f"email sent to {giver_email}. {giver_name} -> {receiver_name}")


# This is one easy way for everyone to see who they got, without ceasing the fun!
# Just don't scroll the window up, ok?
def print_result(matches: dict) -> None:
    givers = list(matches.keys())
    random.shuffle(givers)
    for giver in givers:
        receiver = matches[giver]
        input(f"Call {giver[0]} and after that. {giver[0]} click any key.")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"{giver[0]} ({giver[1]}) -> {receiver[0]} ({receiver[1]})")
        input(f"{giver[0]} click any key to continue...")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Close this windows so nobody can see the list!")


organizer = input("Who is organizing this Gift Exchange? ")
email = input("Type your email (default email in the environment file .env): ")
password = input("Type your password (default password in the environment file .env): ")
print("Make sure you edited the input file...")
emails = read_file()
matches = exchange_gifts(list_of_people=emails)
send_emails(matches=matches, organizer_name=organizer, organizer_email=email, organizer_password=password)
print_result(matches=matches)
