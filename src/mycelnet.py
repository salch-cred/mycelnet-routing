import numpy as np

class MyceliumRouter:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Conductivity of connections (tubes)
        self.conductivity = np.random.uniform(0.1, 1.0, (num_nodes, num_nodes))
        # Ensure symmetric properties
        self.conductivity = (self.conductivity + self.conductivity.T) / 2.0
        np.fill_diagonal(self.conductivity, 0.0)

    def route_traffic(self, source, target, flux):
        # Calculate routing probabilities based on conductivity (metabolic flow rate)
        row = self.conductivity[source]
        probs = row / np.sum(row)
        next_hop = np.random.choice(self.num_nodes, p=probs)
        # Increase conductivity of utilized path (reinforcement)
        self.conductivity[source, next_hop] += flux * 0.1
        self.conductivity[next_hop, source] = self.conductivity[source, next_hop]
        return next_hop

    def decay_connections(self, decay_rate=0.02):
        # Pruning inactive connections
        self.conductivity = np.clip(self.conductivity - decay_rate, 0.01, 10.0)
        np.fill_diagonal(self.conductivity, 0.0)
