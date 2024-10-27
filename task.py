from building import building
from player import buildings

"""

TYPES OF TASK:

Type 0:
Description: Buy a loaf of bread from the bakery.
Building: Breadnik (2)

Type 1:
Description: Buy vegetables from the grocery shop.
Building: Grocerov (1)

Type 2:
Description: Buy household items from the grocery shop.
Building: Grocerov (1)

Type 3:
Description: Discuss the socio-political state of the world with Professor Ivanov.
Building: University (7)

Type 4:
Description: Check in with Comrade Kuznetsov.
Building: Stary Senat (8)

Type 5:
Description: Stay updated on the latest news from the Kremlin! Buy a transistor radio.
Building: Techno Store (6)

Type 6:
Description: You need to get moving! Buy a Lada.
Building: Lada DeaLership (5)

Type 7:
Description: It's that time of the week! Pay your bills.
Building: Gosbank (3)

Type 8:
Description: It's that time of the week! Pay your bills.
Building: Gosbank (3)

Type 9:
Description: Time to get on the property ladder. Take out a mortgage.
Building: Gosbank (3)

"""
# list of prices associated with task type IDs
# if task does not require a purchase, this price is 0
tasks_cost_list = [8, 10, 6, 0, 0, 80, 380, 20, 16, 0]
tasks_building_list = [2, 1, 1, 7, 8, 6, 5, 3, 3, 3]
tasks_description_list = ["Buy a loaf of bread from the bakery.",
                          "Buy vegetables from the grocery shop.",
                          "Buy household items from the grocery shop."
                          "Discuss the socio-political state of the world with Professor Ivanov."
                          "Check in with Comrade Kuznetsov.",
                          "Stay updated on the latest news from the Kremlin! Buy a transistor radio.",
                          "You need to get moving! Buy a Lada.",
                          "It's that time of the week! Pay your bills.",
                          "It's that time of the week! Pay your bills.",
                          "Time to get on the property ladder. Take out a mortgage."]

class task:
    def __init__(self, type_of_task):
        self.description = tasks_description_list[type_of_task]
        self.building = tasks_building_list[type_of_task]
        self.completed = False
        self.type = type
        self.cost = tasks_cost_list[type_of_task]

