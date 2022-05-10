from arrays import Array
from arrayqueue import ArrayQueue
from people import TicketAgent, Passenger
import random


class TicketCounterSimulation:  # Create a simulation object.

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):  # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        # Simulation components.
        self._passengerQ = ArrayQueue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)
        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.

    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.

    def _handleArrival(self, time):
        """
        Handles arrival of passenger. Randomly creates new passenger
        and adds it to the queue. The chance is determined by betweenTime
        """
        if random.random() < self._arriveProb:
            self._passengerQ.add(Passenger(self._numPassengers, time))
            self._numPassengers += 1


    def _handleBeginService(self, time):
        """
        Handles the start of service for the passenger. Finds
        free agent and starts the procedure of arrival
        """
        while not self._passengerQ.isEmpty():
            found_agent = False
            for agent in self._theAgents:
                if agent.isFree():
                    passenger = self._passengerQ.pop()
                    self._totalWaitTime += time - passenger.timeArrived()
                    agent.startService(passenger, time + self._serviceTime)
                    found_agent = True
                if found_agent:
                    break
            if not found_agent:
                break

    def _handleEndService(self, time):
        """
        Ends the service of the passenger. Frees the agent to be able
        work with other passengers
        """
        for agent in self._theAgents:
            if agent.isFinished(time):
                agent.stopService()

    def printResults(self):
        """
        Prints results for the whole simulation
        """
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)


if __name__ == '__main__':
    random.seed(4500)
    sim = TicketCounterSimulation(3, 10000, 2, 4)
    sim.run()
    sim.printResults()