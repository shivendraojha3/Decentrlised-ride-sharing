def book_ride(rider_agent, driver_agents):
    for driver_agent in driver_agents:
        if driver_agent.available and driver_agent.location == rider_agent.location:
            driver_agent.available = False
            return driver_agent
    return None