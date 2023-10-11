from abc import ABC


class Human(ABC):
    def __init__(self, ID: int, vel: float, picktime: float):
        self._ID = ID  # Human ID
        self._vel: float = 1.0  # Human Speed
        self._pos = (0, 0)  # Human position
        self._process: int = 0  # Human Process
        self._dist: float = 0.0  # Human distance (squares)
        self._goal = (0, 0)  # Human goal (position of robot to pick)
        self._picktime: float = 15.0  # Human pick time
        self._actualpicktime: float = 0.0  # Human actual pick time
        self._assignedmission: int = 0  # Human assigned mission
        self._deb_route = list  # Human route
        self._deb_picks = list  # Human picks
        self._deb_numpicks: int = 0  # Human number of picks

    def get_ID(self) -> int:
        return self._ID

    def set_ID(self, ID: int):
        self._ID = ID

    def get_vel(self) -> float:
        return self._vel

    def set_vel(self, vel: float):
        if vel > 0:
            self._vel = vel

    def get_pos(self) -> tuple:
        return self._pos

    def set_pos(self, pos):
        self._pos = pos

    def get_process(self) -> int:
        return self._process

    def set_process(self, process: int):
        if process >= 0 and process <= 3:
            self._process = process

    def get_dist(self) -> float:
        return self._dist

    def set_dist(self, dist: float):
        if dist >= 0:
            self._dist = dist

    def get_goal(self) -> tuple:
        return self._goal

    def set_goal(self, goal):
        self._goal = goal

    def get_picktime(self) -> float:
        return self._picktime

    def set_picktime(self, picktime: float):
        if picktime > 0:
            self._picktime = picktime

    def get_actualpicktime(self) -> float:
        return self._actualpicktime

    def set_actualpicktime(self, actualpicktime: float):
        if actualpicktime > 0:
            self._actualpicktime = actualpicktime

    def get_assignedmission(self) -> int:
        return self._assignedmission

    def set_assignedmission(self, assignedmission: int):
        self._assignedmission = assignedmission

    def get_deb_route(self):
        return self._deb_route

    def set_deb_route(self, deb_route):
        self._deb_route = deb_route

    def get_deb_picks(self):
        return self._deb_picks

    def set_deb_picks(self, deb_picks):
        self._deb_picks = deb_picks

    def get_deb_numpicks(self) -> int:
        return self._deb_numpicks

    def set_deb_numpicks(self, deb_numpicks: int):
        if deb_numpicks >= 0:
            self._deb_numpicks = deb_numpicks
