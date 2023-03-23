class Visitor:

    def __init__(self,name):
        if type(name) == str and (1 <= len(name) <= 15):
            self._name = name
        else:
            print("Please use a name that is between 1 and 15 characters.")
    
    def get_name(self):
        return self._name
    def set_name(self,name):
        print("Sorry - can't change")
    name = property(get_name, set_name)

    def trips(self):
        from .trip import Trip
        logged_trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                logged_trips.append(trip)
        return logged_trips
        
    def nationalparks(self):
        from .trip import Trip
        parklist = []
        for trip in Trip.all:
            if trip.visitor == self:
                parklist.append(trip.national_park)
        return list(set(parklist))
    
    def create_trip(self, national_park, start_date, end_date):
        from .trip import Trip
        return Trip(self, national_park, start_date, end_date)