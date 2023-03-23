from .visitor import Visitor
from .national_park import NationalPark

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        if type(start_date) == str:
            self.start_date = start_date
        if type(end_date) == str:
            self.end_date = end_date
        Trip.all.append(self)

        def get_visitor(self):
            return self._visitor
        def set_visitor(self, visitor_input):
            if visitor_input == Visitor:
                self._visitor = visitor_input
            else:
                print("Not a valid visitor name.")
        visitor = property(get_visitor, set_visitor)
            
        def get_national_park(self):
            return self._national_park
        def set_national_park(self, national_park_input):
            if national_park_input == NationalPark:
                self._national_park = national_park_input
            else:
                print("Not a valid National Park.")
        national_park = property(get_national_park, set_national_park)

