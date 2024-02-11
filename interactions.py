def request_ride(rider_agent, driver_agents):
    for driver_agent in driver_agents:
        if driver_agent.available and driver_agent.location == rider_agent.location:
            driver_agent.available = False
            return driver_agent
    return None

def accept_ride(driver_agent, rider_agent):
    if not driver_agent.available:
        return True
    else:
        return False