from aircraft import Aircraft


class AirbusA319(Aircraft):

    def get_model(self):
        return 'Airbus A319'

    def seating_plan(self):
        return range(1,23), 'ABCDEF'