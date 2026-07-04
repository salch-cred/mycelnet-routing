# MycelNet Routing

A novel network routing protocol modeled on the foraging behavior and growth patterns of fungal mycelium networks (specifically *Physarum polycephalum*).

Fungal networks dynamically expand towards nutrient sources and prune redundant, low-traffic connections to minimize metabolic cost while maintaining transport efficiency. MycelNet implements this mathematical behavior for adaptive data packet routing.

## Features
- **Dynamic Growth Equations**: Nodes create potential pathways toward destinations.
- **Pruning Functions**: Inactive pathways decay over time to optimize bandwidth.
- **Resilience Simulation**: Instantly re-routes packets when nodes are disconnected.

## Usage
```bash
python examples/simulate_routing.py
```
