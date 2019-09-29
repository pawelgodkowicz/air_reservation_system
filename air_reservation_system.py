import pprint as pp
from flight import Flight

# from planes import AirbusA319, Boeing777
from planes import *
# print('hello')
# from helpers import console_card_printer
from helpers import *

airbus = AirbusA319()
# print(airbus.num_seats())
f = Flight('L023', AirbusA319())
# print(f.aircraft_model())
# print(f.get_airline())
# print(f.get_number())

f.allocate_seat('10A', 'Jaroslaw K')
f.allocate_seat('10B', 'Lech K')
f.allocate_seat('10C', 'Pawel K')
print(f.num_available_seats())
# pp.pprint(f._seating)
f.make_boarding_cards(console_card_printer)