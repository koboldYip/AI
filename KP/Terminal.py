class Terminal:

    def __init__(self, capacity, streams):
        self.capacity = capacity
        self.streams = streams
        self.functions_streams = set()
        self.functions_capacity = []
        self.functions = []
