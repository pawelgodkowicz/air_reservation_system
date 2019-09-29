from aircraft import Aircraft


class Boeing777(Aircraft):

    def get_model(self):
        return 'Boeing 777'

    def seating_plan(self):
        return range(1,23), 'ABCDEGHJK'