from abc import ABC
from CreateRoute import CreateRoute
from m_SPF import m_SPF


class Galo(ABC):
    def __init__(self, vel=12.0) -> None:
        self._vel = vel

    def set_vel(self, vel) -> None:
        self._vel = vel


def prueba(agent, vel):
    agent.set_vel(vel)


galo = Galo()
prueba(galo, 7)
print(galo._vel)
[vmap, a] = m_SPF()
route = CreateRoute(vmap, (0, 0), (20, 10))
route2 = route
print(route, len(route))
print(route2, len(route2))
