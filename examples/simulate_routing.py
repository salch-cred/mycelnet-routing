from src.mycelnet import MyceliumRouter
import numpy as np

print("Running MycelNet Routing Simulation...")
router = MyceliumRouter(num_nodes=6)

print("Initial Network Conductivity Matrix:\n", np.round(router.conductivity, 2))

# Route some data packets
current_node = 0
target_node = 5
path = [current_node]

for _ in range(10):
    current_node = router.route_traffic(current_node, target_node, flux=2.0)
    path.append(current_node)
    if current_node == target_node:
        break

print("Routed path:", path)
router.decay_connections()
print("Post-decay/pruned Conductivity Matrix:\n", np.round(router.conductivity, 2))
