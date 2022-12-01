class Function:

    def __init__(self, capacity, streams, appointment, equipment):
        self.capacity = capacity
        self.streams = set(streams)
        self.appointment = appointment
        self.equipment = equipment
