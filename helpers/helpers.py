def console_card_printer(passenger, seat, flight_number, aircraft):

    frame = f'+{"-" * (len(passenger) + len(seat) + len(flight_number) + len(aircraft) + 30)}+'

    text = f'| {passenger}, seat:{seat}, flight#:{flight_number}, aircraft:{aircraft} |'

    list_of_lines = [frame, text, frame]

    output = '\n'.join(list_of_lines)

    print(output)

