print('hello')
import pprint as pp

class Flight:
    def __init__(self, flight_number, aircraft):
        self.flight_number = flight_number
        self.aircraft = aircraft

        rows, seats = self.aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def get_airline(self):
        return self.flight_number[0:2]

    def get_number(self):
        return self.flight_number[2:]

    def aircraft_model(self):
        return self.aircraft.get_model()

    def _parse_seat(self, seat):

        row_numbers, seat_letters = self.aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]

        # obsuga wyjatku
        try:
            row = int(row_text)
        except ValueError:
            raise  ValueError(f'Invalid row number {row_text}')

        if row not in row_numbers:
            raise ValueError(f'Incorrect row number my friends')

        return row, letter
    def allocate_seat(self, seat='12C', passenger='Pawel G'):
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger
    #TODO homework
    def relocate_seat(self, from_seat, to_seat):

        to_row, to_letter = self._parse_seat(to_seat)

        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Seat {to_seat} already occupied - can not relocate')

        from_row, from_letter = self._parse_seat(from_seat)

        passenger = self._seating[from_row][from_letter]

        self._seating[from_row][from_letter] = None

        self._seating[to_row][to_letter] = passenger


    def num_available_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
          for passenger, seat in self._passenger_seats():
              card_printer(passenger, seat, self.flight_number, self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self.aircraft.seating_plan()

        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f'{row}{letter}')
#klasa abstrakycjna

class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):

    def get_model(self):
        return 'Airbus A319'

    def seating_plan(self):
        return range(1,23), 'ABCDEF'
# TODO
def console_card_printer(passenger, seat, flight_number, aircraft):

    frame = f'+{"-" * (len(passenger) + len(seat) + len(flight_number) + len(aircraft) + 30)}+'

    text = f'| {passenger}, seat:{seat}, flight#:{flight_number}, aircraft:{aircraft} |'

    list_of_lines = [frame, text, frame]

    output = '\n'.join(list_of_lines)

    print(output)

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