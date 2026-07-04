from fastapi import FastAPI
from pydantic import BaseModel
from src.mycelnet import MyceliumRouter

app = FastAPI(title="MycelNet Routing API")
router = MyceliumRouter(num_nodes=6)

class RoutingRequest(BaseModel):
    source: int
    target: int
    flux: float

@app.post("/route")
def route_traffic(req: RoutingRequest):
    if req.source < 0 or req.source >= 6 or req.target < 0 or req.target >= 6:
        return {"error": "Source and target must be between 0 and 5."}
    next_hop = router.route_traffic(req.source, req.target, req.flux)
    router.decay_connections()
    return {
        "next_hop": int(next_hop),
        "conductivity": router.conductivity.tolist()
    }
