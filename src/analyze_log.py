import csv


def most_ordered_per_person(data, person):
    most_order_dict = {}
    order_counter = 0
    most_ordered = 'pizza'

    for order in data:
        if order[0] == person:
            if order[1] in most_order_dict:
                most_order_dict[order[1]] += 1
            else:
                most_order_dict[order[1]] = 1

        if most_order_dict[order[1]] > order_counter:
            most_ordered = order[1]

    # print(most_ordered)
    return most_ordered


def never_ordered_per_person(data, person):
    menu = set()
    person_orders = set()

    for order in data:
        menu.add(order[1])

    for order in data:
        if order[0] == person:
            person_orders.add(order[1])

    return menu.difference(person_orders)


def hungry_days_per_person(data, person):
    weekdays = set()
    full_belly_days = set()

    for order in data:
        weekdays.add(order[2])

    for order in data:
        if order[0] == person:
            full_belly_days.add(order[2])

    return weekdays.difference(full_belly_days)


def csv_reader(path_to_file):
    with open(path_to_file, "r") as file:
        result = list(csv.reader(file))
    return result


def csv_writer(path_to_file, data):
    with open(path_to_file, "w") as file:
        file.write(data)
    pass


def analyze_log(path_to_file):
    if (path_to_file.endswith(".csv")) is False:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        csv_file = csv_reader(path_to_file)

        most_ordered_result = most_ordered_per_person(csv_file, "maria")
        ordered_number_result = most_ordered_per_person(csv_file, "arnaldo")
        never_ordered_result = never_ordered_per_person(csv_file, "joao")
        hungry_days_result = hungry_days_per_person(csv_file, "joao")

        csv_writer(
            "./data/mkt_campaign.txt",
            f"{most_ordered_result}\n"
            f"{ordered_number_result}\n"
            f"{never_ordered_result}\n"
            f"{hungry_days_result}\n",
        )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
