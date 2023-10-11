from abc import ABC


class Robot(ABC):
    def __init__(self, ID: int):
        self._ID = ID  # Robot ID
        self._vel: float = 0.9  # Robot speed
        self._pos: tuple  # Robot position
        self._route: list  # Robot route
        self._goal: list  # Robot goal
        self._process: int = 0  # Robot process
        self._dist: float = 0.0  # Robot distance (squares)
        self._assignedmission: int = 0  # Robot assigned mission
        self._downloadtime: float = 0.0

    def get_ID(self):
        return self._ID

    def get_vel(self):
        return self._vel

    def get_pos(self):
        return self._pos

    def get_route(self):
        return self._route

    def get_process(self):
        return self._process

    def get_dist(self):
        return self._dist

    def set_pos(self, pos: tuple):
        self._pos = pos

    def set_route(self, route: list):
        self._route = route

    def get_goal(self):
        return self._goal

    def set_goal(self, goal: list):
        self._goal = goal

    def set_process(self, process: int):
        self._process = process

    def set_dist(self, dist: float):
        self._dist = dist

    def set_assignedmission(self, assignedmission: int):
        self._assignedmission = assignedmission

    def get_assignedmission(self):
        return self._assignedmission

    def set_downloadtime(self, downloadtime: float):
        self._downloadtime = downloadtime

    def get_downloadtime(self):
        return self._downloadtime
