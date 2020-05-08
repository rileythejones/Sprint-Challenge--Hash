#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    cache = {}
    
    for ticket in tickets:
        cache[ticket.source] = ticket.destination 
    

    route = []
    y = "NONE"
    for x in range(len(cache)):
        y = cache[y]
        route.append(y)
    return route
