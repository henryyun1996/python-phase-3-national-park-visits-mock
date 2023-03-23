class NationalPark:
    def __init__(self,name):
        if type(name) == str:
            self._name = name
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        print("Can't change name.")

    name = property(get_name, set_name)

    def trips(self):
        from .trip import Trip
        logged_visits = []
        for trip in Trip.all:
            if trip.national_park == self:
                logged_visits.append(trip)
        return logged_visits
    
    def visitors(self):
        from .trip import Trip
        logged_visitors = []
        for trip in Trip.all:
            if trip.national_park == self:
                logged_visitors.append(trip.visitor)
        return list(set(logged_visitors))
    
    def total_visits(self):
        from .trip import Trip
        count = 0
        for trip in Trip.all:
            if trip.national_park == self:
                count += 1
        return count

    def best_visitor(self):
        from .trip import Trip
        count_object = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.national_park not in count_object:
                    count_object[trip.visitor] = 1
                else:
                    count_object[trip.visitor] += 1
        max_key = max(count_object, key = count_object.get)
        return max_key