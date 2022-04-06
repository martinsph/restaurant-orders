class TrackOrders:
    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append({
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        most_order_dict = {}
        order_counter = 1
        most_ordered = 'pizza'

        for order in self.orders:
            if order["customer"] == customer:
                if order["order"] in most_order_dict:
                    most_order_dict[order["order"]] += 1
                else:
                    most_order_dict[["order"]] = 1

            if most_order_dict[order["order"]] > order_counter:
                most_ordered = order["order"]

        # print(most_ordered)
        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        menu = set()
        person_orders = set()

        for order in self.orders:
            menu.add(order["order"])

        for order in self.orders:
            if order["customer"] == customer:
                person_orders.add(order["order"])

        return menu.difference(person_orders)

    def get_days_never_visited_per_customer(self, customer):
        weekdays = set()
        full_belly_days = set()

        for order in self.orders:
            weekdays.add(order["order"])

        for order in self.orders:
            if order["customer"] == customer:
                full_belly_days.add(order["order"])

        return weekdays.difference(full_belly_days)

    def get_busiest_day(self):
        weekdays_dict = {}
        counter = 0
        most_visited = 'terça-feira'

        for order in self.orders:
            if order["day"] in weekdays_dict:
                weekdays_dict[order["day"]] += 1
            else:
                weekdays_dict[["day"]] = 1

            if weekdays_dict[order["day"]] > counter:
                most_visited = order["day"]

        # print(most_visited)
        return most_visited

    def get_least_busy_day(self):
        weekdays_dict = {}
        counter = 0
        least_visited = 'terça-feira'

        for order in self.orders:
            if order["day"] in weekdays_dict:
                weekdays_dict[order["day"]] += 1
            else:
                weekdays_dict[["day"]] = 1

            if weekdays_dict[order["day"]] <= counter:
                least_visited = order["day"]

        # print(least_visited)
        return least_visited
