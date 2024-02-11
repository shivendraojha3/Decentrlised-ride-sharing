from uagents import Agent

# Define Rider Agent
class RiderAgent(Agent):
    def __init__(self, id, location):
        super().__init__(id)
        self.location = location
        self.available = True

# Define Driver Agent           
class DriverAgent(Agent):
    def __init__(self, id, location):
        super().__init__(id)
        self.location = location
        self.available = True
