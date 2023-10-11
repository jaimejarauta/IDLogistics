from abc import ABC


class Mission(ABC):
    def __init__(self, ID: int):
        self._ID = ID  # ID of the mission
        self._picks: list  # Pick position
        self._process: int = 0  # Process in which the mission is in
        # 0: unassigned, 1: assigned, 2: in process, 3: finished
        self._picksdone: list
        self._robotassigned: int = -1  # Robot assigned to mission
        self._humanassigned: int = 0  # Human assigned to the mission
        self._numpicks: int = 0  # Number of picks of the mission
        self._route: list  # Route of the mission
        self._tstart: float = 0.0  # Start time of the mission
        self._twait: float = 0.0  # Time to wait for the mission
        self._intersec: int = 0  # Intersection at which the mission is located
        self._deb_route: list  # Mission debug route
        self._false: int = 0

    def get_ID(self) -> int:
        return self._ID

    def set_ID(self, ID: int):
        self._ID = ID

    def get_picks(self):
        return self._picks

    def set_picks(self, picks):
        self._picks = picks

    def get_picksdone(self):
        return self._picksdone

    def set_picksdone(self, picksdone):
        self._picksdone = picksdone

    def get_process(self) -> int:
        return self._process

    def set_process(self, process: int):
        self._process = process

    def get_robotassigned(self) -> int:
        return self._robotassigned

    def set_robotassigned(self, robotassigned):
        self._robotassigned = robotassigned

    def get_humanassigned(self) -> int:
        return self._humanassigned

    def set_humanassigned(self, humanassigned: int):
        self._humanassigned = humanassigned

    def get_numpicks(self) -> int:
        return self._numpicks

    def set_numpicks(self, numpicks: int):
        if numpicks > 0:
            self._numpicks = numpicks

    def get_route(self) -> list:
        return self._route

    def set_route(self, route):
        self._route = route

    def get_tstart(self) -> float:
        return self._tstart

    def set_tstart(self, tstart: float):
        if tstart > 0:
            self._tstart = tstart

    def get_twait(self) -> float:
        return self._twait

    def set_twait(self, twait: float):
        if twait > 0:
            self._twait = twait

    def get_intersec(self) -> int:
        return self._intersec

    def set_intersec(self, intersec: int):
        self._intersec = intersec

    def get_deb_route(self) -> list:
        return self._deb_route

    def set_deb_route(self, deb_route: list):
        self._deb_route = deb_route

    def set_false(self, false: int):
        self._false = false

    def get_false(self):
        return self._false
