from abc import ABC


class Pick(ABC):
    def _init_(self, ID: int):
        self._missionID = ID  # Mission ID
        self._pickID = ID  # Pick ID
        self._pos: tuple  # Picks position
        self._waittime: float = 0.0  # Picks wait time
        self._intersections: int = 0  # Picks intersections
        self._picktime: float = 0.0  # Tiempo total de hacer el pick
        self._actualwaittime: float = (
            0.0  # Tiempo de espera hasta que se le asigne un humano
        )
        self._humantime: float = 0.0  # Tiempo de pick del humano (cte 15s)
        self._dist: int = 0
        self._humanassigned = -1

    def set_missionID(self, missionID: int):
        self._missionID = missionID

    def get_missionID(self):
        return self._missionID

    def set_pickID(self, pickID: int):
        self._pickID = pickID

    def get_pickID(self):
        return self._pickID

    def set_intersections(self, intersections: int):
        self._intersections = intersections

    def get_intersections(self):
        return self._intersections

    def set_pos(self, pos: tuple):
        self._pos = pos

    def get_pos(self):
        return self._pos

    def get_waittime(self):
        return self._waittime

    def set_waittime(self, waittime: float):
        self._waittime = waittime

    def get_picktime(self):
        return self._picktime

    def set_picktime(self, picktime: float):
        self._picktime = picktime

    def get_actualwaittime(self):
        return self._actualwaittime

    def set_actualwaittime(self, actualwaittime: float):
        self._actualwaittime = actualwaittime

    def get_humantime(self):
        return self._humantime

    def set_humantime(self, humantime: float):
        self._humantime = humantime

    def get_dist(self):
        return self._dist

    def set_dist(self, dist: int):
        self._dist = dist

    def get_human_assigned(self):
        return self._human_assigned

    def set_human_assigned(self, human_assigned: int):
        self._human_assigned = human_assigned
