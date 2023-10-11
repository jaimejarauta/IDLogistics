# Full code in one file (not checked if working)

# For use of simulator, use the individual files

from abc import ABC

import numpy as np
from matplotlib import pyplot
from matplotlib import colors

import random
import copy


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import random
import pickle

import GUI_functions

from pathlib import Path
import pandas as pd


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


def m_SPF():
    map_SPF = np.ones((57, 165), dtype=int)

    for i in range(map_SPF.shape[1]):
        if (i % 2) == 0:
            map_SPF[:, i] = 0

    map_SPF[0, :] = 0  # Empty row 0
    map_SPF[11:13, :] = 0  # Empty thick row
    map_SPF[30:32, :] = 0  # Empty thick row
    map_SPF[:, 160:165] = 0  # Empty end thick column
    map_SPF[53:57, 0:38] = 0  # Empty lower left zone
    map_SPF[48:57, 38:42] = 0  # map_SPF[48:57, 38:42] = 0 # Lower left empty
    map_SPF[43:47, 42:57] = 0  # map_SPF[43:47, 42:57] = 0 # map_SPF[47:57] = 0
    map_SPF[47:57, 43:55] = 1  # "Outside" occupied slot
    map_SPF[48:57, 56:63] = 0  # map_SPF[48:50] = 0 # map_SPF[48:50] = 0
    map_SPF[48:50, 63:156] = 0  # Rows separating the pickup zone empty
    map_SPF[48:57, 156:164] = 0  # map_SPF[50:57, 56:63] = 0
    map_SPF[50:57, 63:156] = 1  # Pickup zone occupied
    map_SPF[51, 7:10] = 0  # Gap above a staircase
    # Gaps interleaved:
    map_SPF[16:20, 32:37] = 0  # Gap a.
    map_SPF[16:20, 58:63] = 0  # Gap b
    map_SPF[16:20, 88:93] = 0  # Gap e
    map_SPF[16:20, 114:119] = 0  # G-gap
    map_SPF[16:20, 146:151] = 0  # Gap i
    map_SPF[37:41, 32:37] = 0  # Gap d
    map_SPF[37:41, 58:63] = 0  # Gap c
    map_SPF[37:41, 88:93] = 0  # Gap f
    map_SPF[37:41, 114:119] = 0  # Gap h
    map_SPF[37:41, 146:151] = 0  # Gap j
    # Stairs:
    map_SPF[7:11, 10:12] = 1
    map_SPF[7:11, 38:40] = 1
    map_SPF[7:11, 74:76] = 1
    map_SPF[7:11, 90:92] = 1
    map_SPF[7:11, 118:120] = 1
    map_SPF[7:11, 154:156] = 1
    map_SPF[52:56, 7:10] = 1
    map_SPF[41:45, 38:40] = 1
    map_SPF[42:46, 118] = 1
    # Blue squares right:
    map_SPF[2:4, 162:165] = 1.0
    map_SPF[22:24, 162:165] = 1
    map_SPF[38:40, 162:165] = 1
    map_SPF[53:55, 162:165] = 1
    # Blue squares below:
    map_SPF[50:52, 40:43] = 1
    map_SPF[50:52, 56:59] = 1
    # Green columns:
    map_SPF[16:18, 6:9] = 1
    map_SPF[16:18, 33:36] = 1
    map_SPF[16:18, 60:63] = 1
    map_SPF[16:18, 89:92] = 1
    map_SPF[16:18, 116:119] = 1
    map_SPF[16:18, 149:152] = 1
    map_SPF[38:40, 6:9] = 1
    map_SPF[38:40, 33:36] = 1
    map_SPF[38:40, 60:63] = 1
    map_SPF[38:40, 89:92] = 1
    map_SPF[38:40, 116:119] = 1
    map_SPF[38:40, 149:152] = 1

    map_list = map_SPF.tolist()

    # colormap = colors.ListedColormap(["white", "grey"])
    # pyplot.imshow(map_list, cmap=colormap)
    # pyplot.show()

    map_array = map_SPF

    return map_array, map_list


def m_SES():
    map_Ses = np.zeros((91, 137), dtype=int)
    index = 2
    while index < map_Ses.shape[1] - 5:
        map_Ses[:, index] = 1
        index += 3

    map_Ses[0:3, :] = 0
    map_Ses[18:20, :] = 0
    map_Ses[35:37, :] = 0
    map_Ses[52:54, :] = 0
    map_Ses[69:71, :] = 0
    map_Ses[86:, :] = 0

    map_Ses[0, 28] = 1
    map_Ses[10, 28] = 1
    map_Ses[20, 28] = 1
    map_Ses[29, 28] = 1
    map_Ses[39, 28] = 1
    map_Ses[48, 28] = 1
    map_Ses[58, 28] = 1
    map_Ses[68, 28] = 1
    map_Ses[78, 28] = 1
    map_Ses[87, 28] = 1

    map_Ses[0, 57] = 1
    map_Ses[10, 57] = 1
    map_Ses[20, 57] = 1
    map_Ses[29, 57] = 1
    map_Ses[39, 57] = 1
    map_Ses[48, 57] = 1
    map_Ses[58, 57] = 1
    map_Ses[68, 57] = 1
    map_Ses[78, 57] = 1
    map_Ses[87, 57] = 1

    map_Ses[0, 85] = 1
    map_Ses[10, 85] = 1
    map_Ses[20, 85] = 1
    map_Ses[29, 85] = 1
    map_Ses[39, 85] = 1
    map_Ses[48, 85] = 1
    map_Ses[58, 85] = 1
    map_Ses[68, 85] = 1
    map_Ses[78, 85] = 1
    map_Ses[87, 85] = 1

    map_Ses[0, 114] = 1
    map_Ses[10, 114] = 1
    map_Ses[20, 114] = 1
    map_Ses[29, 114] = 1
    map_Ses[39, 114] = 1
    map_Ses[48, 114] = 1
    map_Ses[58, 114] = 1
    map_Ses[68, 114] = 1
    map_Ses[78, 114] = 1
    map_Ses[87, 114] = 1

    map_Ses[0, -1] = 1
    map_Ses[10, -1] = 1
    map_Ses[20, -1] = 1
    map_Ses[29, -1] = 1
    map_Ses[39, -1] = 1
    map_Ses[48, -1] = 1
    map_Ses[58, -1] = 1
    map_Ses[68, -1] = 1
    map_Ses[78, -1] = 1
    map_Ses[87, -1] = 1

    map_Ses[50, 41] = 0
    map_Ses[50, 44] = 0
    map_Ses[51, 44] = 0
    map_Ses[55, 41] = 0
    map_Ses[55, 44] = 0
    map_Ses[54, 44] = 0

    map_Ses[51, 42] = 1
    map_Ses[51, 43] = 1
    map_Ses[52, 41] = 1
    map_Ses[53, 41] = 1
    map_Ses[52, 42] = 1
    map_Ses[53, 42] = 1
    map_Ses[52, 43] = 1
    map_Ses[53, 43] = 1
    map_Ses[54, 42] = 1
    map_Ses[54, 43] = 1

    map_list = map_Ses.tolist()

    # colormap = colors.ListedColormap(["white", "grey"])
    # pyplot.imshow(map_list, cmap=colormap)
    # pyplot.show()

    map_array = map_Ses

    return map_array, map_list


def m_CTF():
    map_CTF = np.ones((64, 121))

    for i in range(map_CTF.shape[1]):
        if (i % 2) == 0:
            map_CTF[:, i] = 0

    map_CTF[:3, :] = 0
    map_CTF[-5:, :] = 0
    map_CTF[-3:, :11] = 1
    map_CTF[25:27, :] = 0
    map_CTF[41:43, :] = 0
    map_CTF[-15:, 29:41] = 0
    map_CTF[11:14, 24] = 1
    map_CTF[45:48, 24] = 1
    map_CTF[11:14, 60] = 1
    map_CTF[11:14, 76] = 1
    map_CTF[9:12, 75] = 0
    map_CTF[14, 75] = 0
    map_CTF[11:13, 77] = 0
    map_CTF[-9:-6, 52] = 1
    map_CTF[-9:-6, 74] = 1
    map_CTF[-6, 70:77] = 0
    map_CTF[11:14, 104] = 1
    map_CTF[45:48, 104] = 1
    map_CTF[9:12, 103] = 0
    map_CTF[14, 103] = 0
    map_CTF[11:13, 105] = 0
    map_CTF[-12:-10, 73] = 0
    map_CTF[46:49, 103] = 0
    map_CTF[43:45, 105] = 0

    map_list = map_CTF.tolist()

    # colormap = colors.ListedColormap(["white", "grey"])
    # pyplot.imshow(map_list, cmap=colormap)
    # pyplot.show()

    map_array = map_CTF

    return map_array, map_list


def OrderPicks(picks, pos):
    ordered_picks = []
    j = 0

    while len(picks) > 0:
        d_min = 100000
        if len(ordered_picks) == 0:
            for i in range(len(picks)):
                d = (
                    (picks[i].get_pos()[0] - pos[0]) ** 2
                    + (picks[i].get_pos()[1] - pos[1]) ** 2
                ) ** 0.5
                # Calculate the distance between the current pick and all remaining picks to see which one is the closest one.
                if d < d_min:
                    d_min = d
                    pos_min_index = i
            ordered_picks.append(picks[pos_min_index])
            picks.pop(pos_min_index)
        else:
            d_min = 100000
            for i in range(len(picks)):
                d = (
                    (picks[i].get_pos()[0] - ordered_picks[j].get_pos()[0]) ** 2
                    + (picks[i].get_pos()[1] - ordered_picks[j].get_pos()[1]) ** 2
                ) ** 0.5
                # Calculate the distance between the current pick and all remaining picks to see which one is the closest one.
                if d < d_min:
                    d_min = d
                    pos_min_index = i
            j = j + 1

            ordered_picks.append(
                picks[pos_min_index]
            )  # Add the pick closest to the route
            picks.pop(pos_min_index)  # Remove the closest pick from the pick vector
    return ordered_picks


def MoveRobot(robot, robot_list, goal, vmap, vmap_empty, mission):
    a = 0
    cont_intersec_iterations = 0

    new_positions_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    positions_to_check = [
        [[2, 0], [1, 1], [1, -1]],
        [[-2, 0], [-1, 1], [-1, -1]],
        [[0, 2], [1, 1], [-1, 1]],
        [[0, -2], [-1, -1], [1, -1]],
    ]

    """print("Calculando Movimiento del Robot ", robot.get_ID(), ":")
    print("Posicion: ", robot.get_pos())"""

    while a == 0:
        """print("Numero de iteracion: ", cont_intersec_iterations + 1)"""
        vmap_route = copy.deepcopy(vmap_empty)
        check_intersection = 0
        check_pos_exist = 1
        check_map_pos_exist = 1
        check_route_exist = 1
        if len(robot.get_route()) >= 1:
            # If the robot has 2 or more positions in its route, you check both of them

            r00 = robot.get_route()[0][0]
            r01 = robot.get_route()[0][1]

            # En primer lugar se comprueban todas las posibles intersecciones que pueda tener un robot
            # Se calcula la dirección a la que avanza el robot principal (Permite calcular menos puntos)
            for x in range(len(new_positions_list)):
                if (r00 - robot.get_pos()[0] == new_positions_list[x][0]) and (
                    r01 - robot.get_pos()[1] == new_positions_list[x][1]
                ):
                    # Comprobamos si en la posición hacia la que avanza el robot principal hay un robot crítico
                    if vmap[r00][r01] == 2:
                        # Buscamos que robot es
                        for z in robot_list:
                            check_robot_stopped = 0
                            # Comprobamos que el robot tiene ruta
                            try:
                                z.get_route()[0][0]
                                if z.get_route() == z.get_pos():
                                    check_robot_stopped = 1
                            except:
                                check_route_exist = 0
                            # Comprobamos que el robot tiene posicion
                            try:
                                z.get_pos()[0]
                            except:
                                check_pos_exist = 0

                            if check_route_exist == 1 and check_robot_stopped == 0:
                                # Si el robot critico se encuentra el la ruta del principal
                                if (z.get_pos()[0] == r00) and (z.get_pos()[1] == r01):
                                    # Y va hacia la posición del principal
                                    if (z.get_route()[0][0] == robot.get_pos()[0]) and (
                                        z.get_route()[0][1] == robot.get_pos()[1]
                                    ):
                                        # Si no hubiera cambios los robots se atravesarían
                                        # Cambio de la ruta del robot principal
                                        vmap_route[
                                            r00,
                                            r01,
                                        ] = 1
                                        """print(
                                            "Interseccion tipo 1 con robot ", z.get_ID()
                                        )
                                        print(
                                            "Siguiente Posicion robot principal: \nAntigua:",
                                            robot.get_route()[0],
                                        )"""

                                        if (
                                            CreateRoute(
                                                vmap_route, robot.get_pos(), goal
                                            )
                                            != False
                                        ):
                                            robot.set_route(
                                                CreateRoute(
                                                    vmap_route, robot.get_pos(), goal
                                                )[1:]
                                            )
                                        else:
                                            mission.set_false(mission.get_false() + 1)
                                            robot.set_pos(pos=robot.get_route()[0])
                                            route = robot.get_route()
                                            route.pop(0)
                                            robot.set_route(route)
                                            robot.set_dist(dist=robot.get_dist() + 1)
                                        """print("Nueva: ", robot.get_route()[0])
                                        print(
                                            "Posicion robot critico: \nPosicion Actual: ",
                                            z.get_pos(),
                                            "Siguiente Posicion: ",
                                            z.get_route()[0],
                                        )"""

                                        colormap = colors.ListedColormap(
                                            ["white", "grey", "black"]
                                        )
                                        """pyplot.imshow(
                                            vmap_route.tolist(), cmap=colormap
                                        )
                                        pyplot.show()"""
                                        vmap_route = copy.deepcopy(vmap_empty)
                                        mission.set_intersec(mission.get_intersec() + 1)
                                        check_intersection = 1

                            elif check_pos_exist == 1:
                                # Si el robot crítico está parado en la ruta del principal
                                if (z.get_pos()[0] == r00) and (z.get_pos()[1] == r01):
                                    # Cambio ruta del principal
                                    vmap_route[
                                        r00,
                                        r01,
                                    ] = 1
                                    """print("Interseccion tipo 2 con robot ", z.get_ID())"""
                                    """print(
                                        "Siguiente Posicion robot principal: \nAntigua:",
                                        robot.get_route()[0],
                                    )"""
                                    if (
                                        CreateRoute(vmap_route, robot.get_pos(), goal)
                                        != False
                                    ):
                                        robot.set_route(
                                            CreateRoute(
                                                vmap_route, robot.get_pos(), goal
                                            )[1:]
                                        )
                                    else:
                                        mission.set_false(mission.get_false() + 1)
                                        robot.set_pos(pos=robot.get_route()[0])
                                        route = robot.get_route()
                                        route.pop(0)
                                        robot.set_route(route)
                                        robot.set_dist(dist=robot.get_dist() + 1)
                                    """print("Nueva: ", robot.get_route()[0])"""
                                    """print(
                                        "Posicion robot critico: \nPosicion Actual: ",
                                        z.get_pos(),
                                    )"""
                                    """colormap = colors.ListedColormap(
                                        ["white", "grey", "black"]
                                    )
                                    pyplot.imshow(vmap_route.tolist(), cmap=colormap)
                                    pyplot.show()"""
                                    vmap_route = copy.deepcopy(vmap_empty)
                                    mission.set_intersec(mission.get_intersec() + 1)
                                    check_intersection = 1
                            check_route_exist = 1
                            check_pos_exist = 1
                    # Se comprueban que no haya un robot critico cuya ruta sea la misma que el principal
                    for y in range(len(positions_to_check[x])):
                        # Comprobación de que la posicion del mapa existe
                        try:
                            vmap[robot.get_pos()[0] + positions_to_check[x][y][0]][
                                robot.get_pos()[1] + positions_to_check[x][y][1]
                            ]
                        except:
                            check_map_pos_exist = 0
                        if check_map_pos_exist == 1:
                            # Si en la posicion critica hay un robot
                            if (
                                vmap[robot.get_pos()[0] + positions_to_check[x][y][0]][
                                    robot.get_pos()[1] + positions_to_check[x][y][1]
                                ]
                                == 2
                            ):
                                for z in robot_list:
                                    try:
                                        z.get_route()[0][0]
                                    except:
                                        check_route_exist = 0
                                    if check_route_exist == 1:
                                        # Se busca que robot es
                                        if (
                                            z.get_pos()[0]
                                            == robot.get_pos()[0]
                                            + positions_to_check[x][y][0]
                                        ) and (
                                            z.get_pos()[1]
                                            == robot.get_pos()[1]
                                            + positions_to_check[x][y][1]
                                        ):
                                            # Y que las rutas coincidan
                                            if (
                                                len(z.get_route()) != 0
                                                and len(robot.get_route()) != 0
                                            ):
                                                if (
                                                    z.get_route()[0][0]
                                                    == robot.get_route()[0][0]
                                                ) and (
                                                    z.get_route()[0][1]
                                                    == robot.get_route()[0][1]
                                                ):
                                                    # Cambio de ruta del robot principal
                                                    vmap_route[
                                                        z.get_route()[0][0],
                                                        z.get_route()[0][1],
                                                    ] = 1
                                                    """print(
                                                        "Interseccion tipo ",
                                                        y + 3,
                                                        "con robot ",
                                                        z.get_ID(),
                                                    )"""
                                                    """print(
                                                        "Siguiente Posicion robot principal: \nAntigua:",
                                                        robot.get_route()[0],
                                                    )"""
                                                    if (
                                                        CreateRoute(
                                                            vmap_route,
                                                            robot.get_pos(),
                                                            goal,
                                                        )
                                                        != False
                                                    ):
                                                        robot.set_route(
                                                            CreateRoute(
                                                                vmap_route,
                                                                robot.get_pos(),
                                                                goal,
                                                            )[1:]
                                                        )
                                                    else:
                                                        mission.set_false(
                                                            mission.get_false() + 1
                                                        )
                                                        robot.set_pos(
                                                            pos=robot.get_route()[0]
                                                        )
                                                        route = robot.get_route()
                                                        route.pop(0)
                                                        robot.set_route(route)
                                                        robot.set_dist(
                                                            dist=robot.get_dist() + 1
                                                        )
                                                    """print("Nueva: ", robot.get_route()[0])"""
                                                    """print(
                                                        "Posicion robot critico: \nPosicion Actual: ",
                                                        z.get_pos(),
                                                        "Siguiente Posicion: ",
                                                        z.get_route()[0],
                                                    )"""
                                                    mission.set_intersec(
                                                        mission.get_intersec() + 1
                                                    )
                                                    vmap_route = copy.deepcopy(
                                                        vmap_empty
                                                    )
                                                    check_intersection = 1

                                    check_route_exist = 1
                        check_map_pos_exist = 1

            # Si se ha recorrido el while mas de 500 veces, se considera que no existe ruta posible
            if cont_intersec_iterations > 10:
                # Se para el robot para la siguiente iteracion
                new_route = robot.get_route()
                new_route.insert(0, robot.get_pos())
                robot.set_route(new_route)
                check_intersection = 0

            if check_intersection == 0:
                robot.set_pos(pos=robot.get_route()[0])
                route = robot.get_route()
                route.pop(0)
                robot.set_route(route)
                robot.set_dist(dist=robot.get_dist() + 1)
                a = 1
            else:
                cont_intersec_iterations = cont_intersec_iterations + 1

            """if vmap[r00][r01] == 1 or vmap[r10][r11] == 1:

                vmap2 = copy.deepcopy(vmap)
                vmap2[r00][r01] = 1
                vmap2[r10][r11] = 1

                robot.set_route(CreateRoute(vmap2, robot.get_pos(), goal))

                pick.set_intersections(pick.get_intersections() + 1)"""

        if len(robot.get_route()) == 0:
            a = 2  # The robot arrived at the pick or it does not have a route (should not happen)
    """print("\n")"""
    return a


# import datarobot_CSV


def Movement(mission, missions, robot, robots, human, xmap):
    if xmap == 0:  # If the map is Cortefiel
        [vmap, map_list] = m_CTF()
    elif xmap == 1:  # If the map is Springfield
        [vmap, map_list] = m_SPF()
    elif xmap == 2:
        [vmap, map_list] = m_SES()
    process = mission.get_process()

    vmap_2 = copy.deepcopy(vmap)

    for x in range(len(missions)):
        vmap_2[
            robots[missions[x].get_robotassigned()].get_pos()[0],
            robots[missions[x].get_robotassigned()].get_pos()[1],
        ] = 2
    vmap_robots = copy.deepcopy(vmap_2)

    if mission.get_process() == 0:  # If the process is 0 (never supposed to happen)
        a = 0

    if (
        mission.get_process() == 1
    ):  # If the process is 1 (robot moving to pick position)
        mission.get_picks()[0].set_picktime(mission.get_picks()[0].get_picktime() + 1.4)
        if (
            robot.get_pos() == mission.get_picks()[0].get_pos()
        ):  # If robot is at pick location
            mission.set_process(process=2)  # Set mission process to 2
            robot.set_process(2)

        elif (
            robot.get_pos() != mission.get_picks()[0].get_pos()
        ):  # If robot is not at pick location
            MoveRobot(
                robot,
                robots,
                mission.get_picks()[0].get_pos(),
                vmap_robots,
                vmap,
                mission,
            )  # Move robot to next route position

    if (
        mission.get_process() == 2
    ):  # If the process is 2 (waiting to have human assigned)
        # Get robots class process
        selected_human = -1  # Set selected human to -1
        available_humans = 0  # Number of humans available to pick
        d = 100000
        for i in range(0, len(human)):
            if human[i].get_process() == 0:  # If human is available
                if d > (
                    (mission.get_picks()[0].get_pos()[0] - human[i].get_pos()[0]) ** 2
                    + (mission.get_picks()[0].get_pos()[1] - human[i].get_pos()[1]) ** 2
                ) ** (1 / 2):
                    available_humans = available_humans + 1  # Add 1 to available humans
                    selected_human = i  # Set selected human to i
                    d = (
                        (mission.get_picks()[0].get_pos()[0] - human[i].get_pos()[0])
                        ** 2
                        + (mission.get_picks()[0].get_pos()[1] - human[i].get_pos()[1])
                        ** 2
                    ) ** (1 / 2)

        if available_humans == 0:  # If no humans are available
            mission.get_picks()[0].set_actualwaittime(
                actualwaittime=mission.get_picks()[0].get_actualwaittime() + 1.4
            )
            return 0

        elif available_humans > 0:  # If humans are available
            mission.set_humanassigned(
                humanassigned=selected_human
            )  # Set human assigned to selected mission
            human[mission.get_humanassigned()].set_process(
                process=1  # Set human process to 1 (going to pick position)
            )  # Set human process to 1
            human[mission.get_humanassigned()].set_goal(
                goal=mission.get_picks()[0].get_pos()  # Set human goal to pick position
            )  # Set human goal to pick location
            human[
                mission.get_humanassigned()
            ].set_deb_route(  # Create route for human to get to pick position
                deb_route=CreateRoute(
                    vmap,
                    human[mission.get_humanassigned()].get_pos(),
                    human[mission.get_humanassigned()].get_goal(),
                )  # Set human route to route from human position to pick location
            )
            if len(human[mission.get_humanassigned()].get_deb_route()) != 0:
                human[mission.get_humanassigned()].set_dist(
                    len(human[mission.get_humanassigned()].get_deb_route())
                )  # Set human distance to length of route

            mission.get_picks()[0].set_waittime(
                waittime=human[mission.get_humanassigned()].get_dist() * 1
            )  # Add 1 to human wait time

            human[mission.get_humanassigned()].set_assignedmission(
                assignedmission=mission.get_ID()
            )  # Set human assigned mission to mission id

            mission.get_picks()[0].set_waittime(
                human[mission.get_humanassigned()].get_dist()
                / human[mission.get_humanassigned()].get_vel()
            )  # Set pick wait time to distance / velocity

            # Es decir, pick-waittime es el tiempo en el que tarda el humano en llegar a la posición de pick

            mission.set_process(
                process=3
            )  # Set mission process to 3 (waiting for human to get to pick)
            robot.set_process(3)
            mission.get_picks()[0].set_picktime(
                mission.get_picks()[0].get_picktime() + 1.4
            )
    if mission.get_process() == 3:
        human[mission.get_humanassigned()].set_pos(
            human[mission.get_humanassigned()].get_deb_route()[0]
        )
        route = human[mission.get_humanassigned()].get_deb_route()
        route.pop(0)
        human[mission.get_humanassigned()].set_deb_route(route)
        if (
            mission.get_picks()[0].get_pos()
            == human[mission.get_humanassigned()].get_pos()
        ):  # If pick wait time is less than human wait time
            mission.set_process(
                process=4
            )  # Set mission process to 4 (human doing picking)
            human[mission.get_humanassigned()].set_process(
                process=2
            )  # Set human process to 2
            # Picks-picktime es el tiempo que tarda el humano en hacer el pick (hasta 15 segundos)
            mission.get_picks()[0].set_picktime(
                mission.get_picks()[0].get_picktime() + 1.4
            )

    if mission.get_process() == 4:  # If mission process is 4 (human doing pick)
        if (
            mission.get_picks()[0].get_humantime()
            < human[mission.get_humanassigned()].get_picktime()
        ):  # If pick time is less than human actual pick time
            mission.get_picks()[0].set_humantime(
                mission.get_picks()[0].get_humantime() + 1.4
            )  # Add 1.4 to pick time
            mission.get_picks()[0].set_picktime(
                picktime=mission.get_picks()[0].get_picktime() + 1.4
            )

            # Human actualpicktime es el valor (siempre constante) que tarda el humano en hacer el pick (15 segundos normalmente)

        elif (
            mission.get_picks()[0].get_humantime()
            >= human[mission.get_humanassigned()].get_picktime()
        ):  # If pick time is greater than human pick time
            human[mission.get_humanassigned()].set_pos(
                pos=mission.get_picks()[0].get_pos()
            )
            human[mission.get_humanassigned()].set_process(
                process=0
            )  # Set human process to 0
            human[mission.get_humanassigned()].set_deb_numpicks(
                deb_numpicks=human[mission.get_humanassigned()].get_deb_numpicks() + 1
            )  # Add 1 to human number of picks
            human[mission.get_humanassigned()].set_deb_route(
                deb_route=[]
            )  # Set human route to empty list
            human[mission.get_humanassigned()].set_dist(
                dist=0
            )  # Set human distance to 0
            human[mission.get_humanassigned()].set_assignedmission(
                assignedmission=-1
            )  # Set human assigned mission to -1
            human[mission.get_humanassigned()].set_goal(
                goal=()
            )  # Set human goal to empty list
            human[mission.get_humanassigned()].set_actualpicktime(
                actualpicktime=0
            )  # Set human actual pick time to 0

            mission.set_numpicks(
                numpicks=mission.get_numpicks() + 1
            )  # Add 1 to mission number of picks
            picks = mission.get_picks()
            picksdone = mission.get_picksdone()
            picks[0].set_human_assigned(mission.get_humanassigned())
            picksdone.append(picks.pop(0))
            mission.set_picks(picks)  # Remove first pick from mission picks list
            mission.set_picksdone(picksdone)

            if len(mission.get_picks()) == 0:  # If mission picks list is empty
                mission.set_process(process=5)  # Set mission process to 5
                robot.set_downloadtime(0)
                robot.set_process(1)
                if xmap == 1:  # If SPF
                    zonadescarga = random.randint(64, 153)
                    robot.set_goal(goal=(49, zonadescarga))
                    mission.set_picks(robot.get_goal())
                    robot.set_route(
                        route=CreateRoute(vmap, robot.get_pos(), robot.get_goal())
                    )

                    mission.set_deb_route(
                        deb_route=mission.get_deb_route().append(robot.get_route())
                    )

                if xmap == 0:  # If CTF
                    zonadescarga = random.randint(40, 115)
                    robot.set_goal(goal=(63, zonadescarga))
                    mission.set_picks(robot.get_goal())
                    robot.set_route(
                        route=CreateRoute(vmap, robot.get_pos(), robot.get_goal())
                    )

                    # mission.set_deb_route(
                    #    deb_route=mission.get_deb_route().append(robot.get_route())
                    # )
                if xmap == 2:
                    zonadescarga = random.randint(0, 80)
                    robot.set_goal(goal=(90, zonadescarga))
                    mission.set_picks(robot.get_goal())
                    robot.set_route(
                        route=CreateRoute(vmap, robot.get_pos(), robot.get_goal())
                    )

                    # mission.set_deb_route(
                    #    deb_route=mission.get_deb_route().append(robot.get_route())
                    # )
                robot.set_process(1)  # Set robot process to 1

                # mission.get_picks()[0].set_waittime(
                #   waittime=0
                # )  # Set pick wait time to 0"""

            else:  # If mission picks list is not empty
                mission.set_process(process=1)  # Set mission process to 1
                robot.set_process(1)
                robot.set_goal(goal=mission.get_picks()[0].get_pos())

                robot.set_route(
                    route=CreateRoute(vmap, robot.get_pos(), robot.get_goal())
                )
                """mission.get_picks()[0].set_dist(len(robot.get_route()))"""

                # mission.set_deb_route(
                # deb_route=mission.get_deb_route().append(robot.get_route())
                mission.get_picks()[0].set_picktime(
                    mission.get_picks()[0].get_picktime() + 1.4
                )
    if mission.get_process() == 5:
        if robot.get_downloadtime() < len(robot.get_route()) / 0.9:
            robot.set_downloadtime(robot.get_downloadtime() + 1.4)
        else:
            mission.set_process(6)

    if mission.get_process() == 6:
        data_CSV(mission)
        # Llamar a csv

        # datarobot_CSV(robot)
        robot.set_goal(goal=())
        robot.set_route(route=())
        robot.set_process(process=0)
        robot.set_assignedmission(assignedmission=0)
        robot.set_pos(pos=CreatePos(vmap, map_list, 0, 0))

        mission.set_process(process=7)

    if process == 7:
        return

    return


#############################
#     Initial Interface
#############################


def ini_GUI():
    initial_window = tk.Tk()
    initial_window.title("ID Logistics - Warehouse Simulation")

    data_intro_frame = tk.LabelFrame(
        initial_window, text="ID Logistics - Warehouse Simulation", padx=20, pady=20
    )
    data_intro_frame.grid(row=10, column=10, padx=10, pady=10, columnspan=3)

    def new_simulation():
        global selection
        selection = 1
        initial_window.destroy()

    # New Simulation Button
    new_sim_button = tk.Button(
        data_intro_frame, text="New Simulation", fg="blue", command=new_simulation
    )
    new_sim_button.grid(row=1, column=0, pady=10, columnspan=1)

    # FUNCIONAMIENTO CONTINUO DE LA INTERFAZ
    initial_window.mainloop()

    return selection


#############################
# Data introduction interface
#############################


def data_intro_GUI():
    data_introduction_window = tk.Tk()
    data_introduction_window.title(
        "ID Logistics - Warehouse Simulation - Data Introduction"
    )

    data_intro_frame = tk.LabelFrame(
        data_introduction_window, text="Data Introduction", padx=20, pady=20
    )
    data_intro_frame.grid(row=10, column=10, padx=10, pady=10, columnspan=3)

    def save_data():
        global selection_map
        global Num_Robots
        global Num_Humans
        global High_Demand_Days
        global Low_Demand_Days
        global Num_Picks_min
        global Num_Picks_max
        global T_Wave
        global Num_Mission_min
        global Num_Mission_max
        global selection

        selection_map = click_map.get()
        Num_Robots = entry_num_robots.get()
        Num_Humans = entry_num_humans.get()
        High_Demand_Days = entry_High_Demand.get()
        Low_Demand_Days = entry_Low_Demand.get()
        Num_Picks_min = entry_Picks_min.get()
        Num_Picks_max = entry_Picks_max.get()
        T_Wave = entry_T_Waves.get()
        Num_Mission_min = entry_Mission_min.get()
        Num_Mission_max = entry_Mission_max.get()
        selection = 1

        data_introduction_window.destroy()

    def exit_simulation():
        global selection

        selection = 0

        data_introduction_window.destroy()

    # Title

    Label_map_title = tk.Label(data_intro_frame, text="DATA INTRODUCTION")
    Label_map_title.grid(row=0, column=0, padx=10, pady=10, columnspan=6)

    # Map Selection

    menu_options_map = [
        "Seseña",
        "Tarancón SPF",
        "Tarancón CTF",
    ]

    Label_map_title = tk.Label(data_intro_frame, text="Map Selection")
    Label_map_title.grid(row=1, column=0, padx=10, pady=10)

    click_map = tk.StringVar()
    click_map.set(menu_options_map[0])
    menu_map = tk.OptionMenu(data_intro_frame, click_map, *menu_options_map)
    menu_map.grid(row=2, column=0)

    # Number of robots selection

    Label_agent_title = tk.Label(data_intro_frame, text="Agents")
    Label_agent_title.grid(row=1, column=1, padx=10, pady=10)

    Label_Robot = tk.Label(data_intro_frame, text="Number of robots")
    Label_Robot.grid(row=2, column=1, padx=10)
    entry_num_robots = tk.Entry(data_intro_frame, width=15)
    entry_num_robots.grid(row=2, column=2)

    # Number of humans selection

    Label_Humans = tk.Label(data_intro_frame, text="Number of humans")
    Label_Humans.grid(row=3, column=1, padx=10)
    entry_num_humans = tk.Entry(data_intro_frame, width=15)
    entry_num_humans.grid(row=3, column=2)

    # Demand Selection

    Label_demand_title = tk.Label(data_intro_frame, text="Demand")
    Label_demand_title.grid(row=1, column=3, padx=10, pady=10)

    Label_High_Demand = tk.Label(data_intro_frame, text="High demand days: ")
    Label_High_Demand.grid(row=2, column=3, padx=10, pady=10)
    entry_High_Demand = tk.Entry(data_intro_frame, width=15)
    entry_High_Demand.grid(row=2, column=4)

    Label_Low_Demand = tk.Label(data_intro_frame, text="Low demand days: ")
    Label_Low_Demand.grid(row=3, column=3, padx=10)
    entry_Low_Demand = tk.Entry(data_intro_frame, width=15)
    entry_Low_Demand.grid(row=3, column=4)

    # Order Selection

    Label_order_title = tk.Label(data_intro_frame, text="Picks")
    Label_order_title.grid(row=4, column=0, padx=10, pady=10)

    Label_Picks = tk.Label(data_intro_frame, text="Picks per Mission: ")
    Label_Picks.grid(row=5, column=0, pady=10)
    entry_Picks_min = tk.Entry(data_intro_frame, width=15)
    entry_Picks_min.grid(row=5, column=1)
    entry_Picks_max = tk.Entry(data_intro_frame, width=15)
    entry_Picks_max.grid(row=5, column=2)

    # Number of waves selection

    Label_waves_title = tk.Label(data_intro_frame, text="Waves")
    Label_waves_title.grid(row=4, column=3, padx=10, pady=10)

    Label_T_Waves = tk.Label(data_intro_frame, text="Time between waves (h): ")
    Label_T_Waves.grid(row=5, column=3, padx=20)
    entry_T_Waves = tk.Entry(data_intro_frame, width=15)
    entry_T_Waves.grid(row=5, column=4)

    Label_Mission = tk.Label(data_intro_frame, text="Missions per Wave: ")
    Label_Mission.grid(row=6, column=3)
    entry_Mission_min = tk.Entry(data_intro_frame, width=15)
    entry_Mission_min.grid(row=6, column=4, padx=0)
    entry_Mission_max = tk.Entry(data_intro_frame, width=15)
    entry_Mission_max.grid(row=6, column=5, padx=20)

    # Save Data
    save_map_button = tk.Button(
        data_intro_frame, text="Start Simulation", fg="blue", command=save_data
    )
    save_map_button.grid(row=8, column=0, pady=30, columnspan=4)

    # Exit
    exit_button = tk.Button(
        data_intro_frame, text="Exit Simulation", fg="red", command=exit_simulation
    )
    exit_button.grid(row=8, column=3, pady=30, columnspan=1)

    # FUNCIONAMIENTO CONTINUO DE LA INTERFAZ
    data_introduction_window.mainloop()

    if selection:
        initial_parameters = {
            "Selection_map": selection_map,
            "Num_Robots": Num_Robots,
            "Num_Humans": Num_Humans,
            "High_Demand_Days": High_Demand_Days,
            "Low_Demand_Days": Low_Demand_Days,
            "Num_Picks_min": Num_Picks_min,
            "Num_Picks_max": Num_Picks_max,
            "T_Wave": T_Wave,
            "Num_Mission_min": Num_Mission_min,
            "Num_Mission_max": Num_Mission_max,
            "Selection": selection,
        }
    else:
        initial_parameters = {"Selection": selection}

    return initial_parameters


#############################
# Data introduction interface
#############################

data_introduction_window = tk.Tk()
data_introduction_window.title(
    "ID Logistics - Warehouse Simulation - Data Introduction"
)

data_intro_frame = tk.LabelFrame(
    data_introduction_window, text="Data Introduction", padx=20, pady=20
)
data_intro_frame.grid(row=10, column=10, padx=10, pady=10, columnspan=3)


def save_data():
    global selection_map
    global Num_Robots
    global Num_Humans
    global High_Demand_Days
    global Low_Demand_Days
    global Num_order_mission_min
    global Num_order_mission_max
    global Num_article_order_min
    global Num_article_order_max
    global T_Wave
    global Num_Mission_Wave_min
    global Num_Mission_Wave_max

    selection_map = click_map.get()
    Num_Robots = entry_num_robots.get()
    Num_Humans = entry_num_humans.get()
    High_Demand_Days = entry_High_Demand.get()
    Low_Demand_Days = entry_Low_Demand.get()
    Num_order_mission_min = entry_Order_Mission_min.get()
    Num_order_mission_max = entry_Order_Mission_max.get()
    Num_article_order_min = entry_Articles_Orders_min.get()
    Num_article_order_max = entry_Articles_Orders_max.get()
    T_Wave = entry_T_Waves.get()
    Num_Mission_Wave_min = entry_Mission_Wave_min.get()
    Num_Mission_Wave_max = entry_Mission_Wave_max.get()

    data_introduction_window.destroy()


# Title

Label_map_title = tk.Label(data_intro_frame, text="DATA INTRODUCTION")
Label_map_title.grid(row=0, column=0, padx=10, pady=10, columnspan=6)

# Map Selection

menu_options_map = [
    "Seseña",
    "Tarancón SPF",
    "Tarancón CTF",
]

Label_map_title = tk.Label(data_intro_frame, text="Map Selection")
Label_map_title.grid(row=1, column=0, padx=10, pady=10)

click_map = tk.StringVar()
click_map.set(menu_options_map[0])
menu_map = tk.OptionMenu(data_intro_frame, click_map, *menu_options_map)
menu_map.grid(row=2, column=0)

# Number of robots selection

Label_agent_title = tk.Label(data_intro_frame, text="Agents")
Label_agent_title.grid(row=1, column=1, padx=10, pady=10)

Label_Robot = tk.Label(data_intro_frame, text="Number of robots")
Label_Robot.grid(row=2, column=1, padx=10)
entry_num_robots = tk.Entry(data_intro_frame, width=15)
entry_num_robots.grid(row=2, column=2)

# Number of humans selection

Label_Humans = tk.Label(data_intro_frame, text="Number of humans")
Label_Humans.grid(row=3, column=1, padx=10)
entry_num_humans = tk.Entry(data_intro_frame, width=15)
entry_num_humans.grid(row=3, column=2)

# Demand Selection

Label_demand_title = tk.Label(data_intro_frame, text="Demand")
Label_demand_title.grid(row=1, column=3, padx=10, pady=10)

Label_High_Demand = tk.Label(data_intro_frame, text="High demand days: ")
Label_High_Demand.grid(row=2, column=3, padx=10, pady=10)
entry_High_Demand = tk.Entry(data_intro_frame, width=15)
entry_High_Demand.grid(row=2, column=4)


Label_Low_Demand = tk.Label(data_intro_frame, text="Low demand days: ")
Label_Low_Demand.grid(row=3, column=3, padx=10)
entry_Low_Demand = tk.Entry(data_intro_frame, width=15)
entry_Low_Demand.grid(row=3, column=4)

# Order Selection

Label_order_title = tk.Label(data_intro_frame, text="Orders")
Label_order_title.grid(row=4, column=0, padx=10, pady=10)

Label_Order_Mission = tk.Label(data_intro_frame, text="Orders per mission: ")
Label_Order_Mission.grid(row=5, column=0, pady=10)
entry_Order_Mission_min = tk.Entry(data_intro_frame, width=15)
entry_Order_Mission_min.grid(row=5, column=1)
entry_Order_Mission_max = tk.Entry(data_intro_frame, width=15)
entry_Order_Mission_max.grid(row=5, column=2)

Label_Articles_Orders = tk.Label(data_intro_frame, text="Articles per order: ")
Label_Articles_Orders.grid(row=6, column=0)
entry_Articles_Orders_min = tk.Entry(data_intro_frame, width=15)
entry_Articles_Orders_min.grid(row=6, column=1)
entry_Articles_Orders_max = tk.Entry(data_intro_frame, width=15)
entry_Articles_Orders_max.grid(row=6, column=2)

# Number of waves selection

Label_waves_title = tk.Label(data_intro_frame, text="Waves")
Label_waves_title.grid(row=4, column=3, padx=10, pady=10)

Label_T_Waves = tk.Label(data_intro_frame, text="Time between waves (h): ")
Label_T_Waves.grid(row=5, column=3, padx=20)
entry_T_Waves = tk.Entry(data_intro_frame, width=15)
entry_T_Waves.grid(row=5, column=4)

Label_Mission_Wave = tk.Label(data_intro_frame, text="Mission per wave: ")
Label_Mission_Wave.grid(row=6, column=3)
entry_Mission_Wave_min = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_min.grid(row=6, column=4, padx=0)
entry_Mission_Wave_max = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_max.grid(row=6, column=5, padx=20)

# Save Data
save_map_button = tk.Button(
    data_intro_frame, text="Start Simulation", fg="blue", command=save_data
)
save_map_button.grid(row=8, column=0, pady=30, columnspan=6)

# FUNCIONAMIENTO CONTINUO DE LA INTERFAZ
data_introduction_window.mainloop()


######################
# Simulating Interface
######################

'''
# msg_box_frm_sub_content = tk.Frame(self.msg_box_frm_content, bg='yellow', bd=2, width=1000)

simulating_window = tk.Tk()
simulating_window.title("ID Logistics - Warehouse Simulation - Simulating")

simulating_frame = tk.LabelFrame(simulating_window, text="Simulating", padx=20, pady=20)
simulating_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Title

Simulating_title = tk.Label(simulating_frame, text="Simulating")
Simulating_title.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Running Time

Label_day_title = tk.Label(simulating_frame, text="Day")
Label_day_title.grid(row=1, column=1, padx=10, pady=10)
Label_hour_title = tk.Label(simulating_frame, text="Hour")
Label_hour_title.grid(row=1, column=2, padx=10, pady=10)
Label_minute_title = tk.Label(simulating_frame, text="Minute")
Label_minute_title.grid(row=1, column=3, padx=10, pady=10)
Label_time_title = tk.Label(simulating_frame, text="Running Time: ")
Label_time_title.grid(row=2, column=0, padx=10, pady=10)

day_sub_frm = tk.Frame(simulating_frame, width=15, relief=tk.GROOVE)
day_sub_frm.grid(row=2, column=1, padx=10, pady=10)
Label_day_value = tk.Label(day_sub_frm, text="00", bg="grey")
Label_day_value.grid(row=0, column=0, padx=10, pady=10)

"""
Label_T_Waves = tk.Label(data_intro_frame, text="Time between waves (h): ")
Label_T_Waves.grid(row=5, column=3)
entry_T_Waves = tk.Entry(data_intro_frame, width=15)
entry_T_Waves.grid(row=5, column=4)

Label_Mission_Wave = tk.Label(data_intro_frame, text="Mission per wave: ")
Label_Mission_Wave.grid(row=6, column=3)
entry_Mission_Wave_min = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_min.grid(row=6, column=4, padx=30)
entry_Mission_Wave_max = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_max.grid(row=6, column=5)
"""

simulating_window.mainloop()

'''


# Main

# Declaration of variables included in interface

# We declare map depending on the one introduced in the interface
# The variable array of the map has been created before.


if __name__ == "__main__":
    state = 0
    a = 0
    while a != 1:
        if state == 0:
            selection = GUI_functions.ini_GUI()
            if selection == 1:
                state = 1
            if selection == 2:
                state = 3
            if selection == 0:
                break
        if state == 1:
            initial_param = GUI_functions.data_intro_GUI()
            if initial_param["Selection"]:
                state = 2
                a = 1

            else:
                state = 0
            """
            execution_window = GUI_DataIntro.tk.Tk()
            execution_param = GUI_DataIntro.ExecutionParam()
            GUI_DataIntro.execution_GUI(execution_window, execution_param)
            execution_param.set_time(10, 10, 10)
            execution_window.mainloop()
            """


if initial_param["Selection_map"] == "Seseña":
    xmap = 2
elif initial_param["Selection_map"] == "Tarancón SPF":
    xmap = 0
else:
    xmap = 1
# 0: CTF, 1: SPF, 2: SES

if xmap == 0:
    vmap, map_list = m_CTF()  # Load the CTF map

elif xmap == 1:
    vmap, map_list = m_SPF()  # Load the SPF map

elif xmap == 2:
    vmap, map_list = m_SES()

# vmap = map variable

# Declaration of variables entered in interface

Num_Robots = int(initial_param["Num_Robots"])  # Number of robots
Num_Human = int(initial_param["Num_Humans"])  # Number of humans
random.seed(69)
High_demand_days = float(initial_param["High_Demand_Days"])
Low_demand_days = float(initial_param["Low_Demand_Days"])
Sim_days = High_demand_days + Low_demand_days

Sim_s = Sim_days * 60 * 60 * 24
High_demand_s = High_demand_days * 60 * 60 * 24
Low_demand_s = Low_demand_days * 60 * 60 * 24

Wave_time = float(initial_param["T_Wave"]) * 60 * 60  # Time between each wave

Missions_Wave = [
    int(initial_param["Num_Mission_min"]),
    int(initial_param["Num_Mission_max"]),
]  # Missions per wave

Picks_Mission = [
    int(initial_param["Num_Picks_min"]),
    int(initial_param["Num_Picks_max"]),
]  # Range of picks per tote


Missions_left = 0  # Remaining missions that have not been assigned

Num_Missions = 0  # Number of total missions

xt = 1


# Initialization of time variables

t = 0.0  # Total simulation time
tday = 0.0  # Time of day (0s to 86400s)
# Day zone (0 = day, 1 = evening, 2 = night) (0s-28800s, 28800s-57600s, 57600s-86400s)
zday = 0
twave = 0.0  # Wave time (0s to timeola s)
tmov = 0.0  # Robot and Human movement time

# Simulation execution time (only used for testing and printing, to be removed later)
texecution = 0.0

# Function declares instances depending on variables entered by user

robots = []
robots = [Robot(x) for x in range(0, Num_Robots)]

humans = []
humans = [Human(x, 1, 15) for x in range(0, Num_Human)]

missions = []

map_dict = {}
index = 3600

# We initialize humans at a random point on the map.
for i in range(Num_Human):
    humans[i].set_pos((randint(0, len(map_list) - 1), randint(0, len(map_list[0]) - 1)))
    while vmap[humans[i].get_pos()[0]][humans[i].get_pos()[1]] == 1:
        humans[i].set_pos(
            (randint(0, len(map_list) - 1), randint(0, len(map_list[0]) - 1))
        )
Missions_Assigned = 1


while t <= Sim_s:
    if Missions_left == 0 and xt == 0:
        print("Missions left finished", Missions_left, "Time", round(t, 2))
        xt = 1

    if Missions_left != 0:
        xt = 0

    if t > Sim_s - 1:
        print("Missions left", Missions_left)

    if t < High_demand_s:  # If we are in a period of high demand
        demand = 1

    elif t >= High_demand_s:  # If we are in a period of low demand
        demand = 0

    if twave >= Wave_time or t == 0:
        twave = 0.0

        # Generate wave

        num_mis_gen = randint(
            Missions_Wave[0], Missions_Wave[1]
        )  # Number of missions generated in each wave

        Missions_left = Missions_left + num_mis_gen
        Num_Missions = Num_Missions + num_mis_gen
    ret = 1
    while Missions_left > 0 and ret == 1:  # If Missions remain to be assigned
        # Assign missions
        mission = Mission(Missions_Assigned)
        ret = GenerateMissions(
            vmap, map_list, xmap, robots, mission, Picks_Mission, demand, t
        )  # Generate the missions

        if ret == 1:
            Missions_left = Missions_left - 1
            missions.append(mission)
            Missions_Assigned = Missions_Assigned + 1

    # Saves the map with all the robots
    vmap_save = copy.deepcopy(vmap)

    for x in range(len(missions)):
        vmap_save[
            robots[missions[x].get_robotassigned()].get_pos()[0],
            robots[missions[x].get_robotassigned()].get_pos()[1],
        ] = 2

    for human in humans:
        if vmap_save[human.get_pos()[0], human.get_pos()[1]] == 2:
            vmap_save[
                human.get_pos()[0],
                human.get_pos()[1],
            ] = 4
        else:
            vmap_save[
                human.get_pos()[0],
                human.get_pos()[1],
            ] = 3

    map_dict[round(t, 1)] = vmap_save.tolist()

    if t % 3600 < 1.4 and t != 0:
        name = "map_hour" + str(round(t / 3600)) + ".pickle"
        with open(name, "wb") as f:
            pickle.dump(map_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
            map_dict = {}

    for i in range(0, len(missions)):
        Movement(
            missions[i],
            missions,
            robots[missions[i].get_robotassigned()],
            robots,
            humans,
            xmap,
        )
    j = 0
    while j < len(missions):
        if missions[j].get_process() == 7:
            missions.pop(j)
        else:
            j = j + 1

    # Time Management

    if tday > 86400:  # If we have passed a day
        tday = 0  # Reset the time of day
        zday = 0  # Reset the time zone of the day to tomorrow

    # Update time variables and round to 1 decimal place (since sometimes it stays at .39999...)

    t = t + 1.4
    round(t, 1)  # Total simulation time
    tmov = tmov + 1.4
    round(tmov, 1)  # Robot and human movement time
    twave = twave + 1.4
    round(twave, 1)  # Wave time
    tday = tday + 1.4
    round(tday, 1)  # Time of day

    texecution = texecution + 1.4
    round(texecution, 1)

    if texecution > 10000:
        print("{:.1f}".format(t))
        texecution = 0
for i in range(0, len(missions)):
    data_CSV(missions[i])

name = "map_hour" + str(round(t / 3600)) + ".pickle"
with open(name, "wb") as f:
    pickle.dump(map_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
    map_dict = {}


def GenerateMissions(vmap, map_list, xmap, robots, mission, picks_Mission, demand, t):
    num_picks = randint(picks_Mission[0], picks_Mission[1])
    # Get robots class process
    selected_robot = -1
    available_robots = 0

    for i in range(0, len(robots)):
        if robots[i].get_process() == 0:
            available_robots = available_robots + 1
            selected_robot = i

    if available_robots == 0:
        return 0

    elif available_robots > 0:
        mission.set_robotassigned(robotassigned=selected_robot)
        if xmap == 0:
            robots[mission.get_robotassigned()].set_pos((63, randint(11, 60)))
        elif xmap == 1:
            robots[mission.get_robotassigned()].set_pos((56, randint(0, 40)))
        elif xmap == 2:
            robots[mission.get_robotassigned()].set_pos((90, randint(80, 130)))
        CreatePicks(
            vmap,
            map_list,
            mission,
            robots[mission.get_robotassigned()].get_pos(),
            num_picks,
            demand,
        )
        robots[mission._robotassigned].set_assignedmission(mission.get_ID())
        robots[mission._robotassigned].set_process(1)
        goal = tuple(mission.get_picks()[0].get_pos())
        start = tuple(robots[mission._robotassigned].get_pos())
        robots[mission._robotassigned].set_route(CreateRoute(vmap, start, goal))
        mission.set_process(1)
        robots[mission.get_robotassigned()].set_process(1)
        robots[mission.get_robotassigned()].set_goal(mission.get_picks()[0].get_pos())
        mission.set_tstart(t)
        mission.set_picksdone([])
        mission.set_deb_route([0])

        return 1


def data_CSV(mission):
    # This function creates a new CSV or updates an existing one with the given data.
    for i in range(0, len(mission.get_picksdone()) - 1):
        dataArray = [
            mission.get_picksdone()[i].get_missionID(),
            mission.get_picksdone()[i].get_pickID(),
            mission.get_picksdone()[i].get_pos(),
            mission.get_robotassigned(),
            mission.get_picksdone()[i].get_human_assigned(),
            mission.get_numpicks(),
            round(mission.get_tstart(), 1),
            round(mission.get_picksdone()[i].get_waittime(), 1),
            round(mission.get_picksdone()[i].get_actualwaittime(), 1),
            round(mission.get_picksdone()[i].get_picktime(), 1),
            round(mission.get_picksdone()[i].get_humantime(), 1),
            mission.get_intersec(),
            mission.get_false(),
        ]

        column_names = [  # Name of columns to be declared in csv
            "ID Mision",
            "ID Pick",
            "Posición",
            "Robot Asignado",
            "Humano Asignado",
            "Número de Picks",
            "Tiempo de Inicio",
            "Tiempo de espera a que llegue el humano",
            "Tiempo espera a asignación humano",
            "Tiempo de pick total",
            "Tiempo pick humano cte",
            "Intersecciones",
            "Error False",
        ]

        file_path = Path("data.csv")  # The directory should be set for each computer
        if file_path.exists():  # If the file exists, it is updated.
            data = pd.DataFrame([dataArray])
            data.to_csv(
                file_path, mode="a", index=False, na_rep="Unknown", header=False
            )
        else:
            # If not, it creates
            data = pd.DataFrame([dataArray], columns=column_names)
            data.to_csv(
                file_path, mode="a", index=False, na_rep="Unknown", header=column_names
            )


import pickle
from matplotlib import pyplot as plt
from matplotlib import colors
import ipywidgets
from ipywidgets import Layout, interact, IntSlider
from IPython.display import display, HTML
import cv2
import io
import numpy as np
from PIL import Image, ImageTk
import PIL
import os

with open("map_hour1.pickle", "rb") as handle:
    maps_loaded = pickle.load(handle)

time_list = list(maps_loaded.keys())
map_list = list(maps_loaded.values())

colormap = colors.ListedColormap(["white", "grey", "blue", "red"])

# Creamos una figura de Matplotlib con el tamaño deseado
fig = plt.figure(figsize=(12, 8))

# Generamos todas las imágenes
for i, time in enumerate(time_list):
    plt.clf()
    plt.imshow(map_list[i], cmap=colormap)
    plt.axis("off")
    plt.title(f"Time: {time}")

    # Cambiamos el tamaño de la figura
    fig.set_size_inches(12, 8)

    # Guardamos la figura en un archivo PNG
    name = f"Images/image{str(i)}.png"
    plt.savefig(name, bbox_inches="tight", pad_inches=0, dpi=100)

# Array vacío
img_array = []

# For para leer imagenes desde un directorio
for x in range(len(time_list)):
    path = f"Images/image{x}.png"
    img = cv2.imread(path)
    img_array.append(img)

# Tamaño de la última imagen alto y ancho
height, width = img.shape[:2]

num_video = 1
while True:
    video_name = f"video_sim{num_video}"
    path = f"./{video_name}.mp4"
    num_video += 1
    if not os.path.exists(path):
        break

video = cv2.VideoWriter(
    video_name,
    cv2.VideoWriter_fourcc(*"mp4v"),
    5,
    (width, height),
)

# For para guardar frames en un video
for i in range(len(img_array)):
    video.write(img_array[i])

video.release()


import numpy as np
import heapq


def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


# path finding function


def CreateRoute(array, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # (1,1),(-1,1),(1,-1),(-1,-1) Eliminate diagonal movement
    close_set = set()

    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}

    oheap = []
    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            data = []

            while current in came_from:
                data.append(current)
                current = came_from[current]
            data = data + [start]
            data = data[::-1]
            return data
        close_set.add(current)

        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue

                else:
                    # array bound y walls
                    continue

            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [
                i[1] for i in oheap
            ]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False


import random
import array as arr


def CreatePos(vmap, map_list, section=0, demand=0):
    i = 0
    # i is the value that establishes whether the vector is correct or not.
    # 0: incorrect, 1: Correct

    while i == 0:
        num1 = -1
        num2 = -1
        while num1 < 0 or num2 < 0:
            if demand == 0:  # Generate position with low demand (all the warehouse)
                num1 = random.randint(1, len(map_list)) - 3  # Random value of x
                num2 = random.randint(1, len(map_list[0])) - 3  # Random value of y

            elif (
                demand == 1
            ):  # Generate position with high demand (1/3 of the warehouse)
                num1 = random.randint(1, len(map_list)) - 3
                leny3 = round(
                    len(map_list[0]) / 3, 0
                )  # Round to int so that there is no problem to run the random.randint

                if section == 1:
                    num2 = (
                        random.randint(0, leny3) - 3
                    )  # Place orders only on the left side of the warehouse
                elif section == 2:
                    num2 = (
                        random.randint(leny3, 2 * leny3) - 3
                    )  # Place orders only on the central part of the warehouse
                elif section == 3:
                    num2 = (
                        random.randint(2 * leny3, 3 * leny3) - 3
                    )  # Place orders only on the right side of the warehouse

        # 2 is subtracted from num1 and num2 so that the limits of the matrix are not exceeded when the adjoining squares are checked.
        # Len counts all the numbers from 1,
        # to make it from [0] of the matrix you would subtract 1 and not to exceed it when checking the adjoining squares you subtract 2

        x = 0

        """x is the number of "0's" in the 9 positions next to the selection.
        selection. If there are 4 or less "0", the selection will be valid (since it is not in the aisles).
        (since it is not in the aisles). If there are more than 4 "0's" it means that
        is in an aisle or other space where there is no shelving""" ""

        # Check the 9 contiguous boxes in which there are "0".

        if vmap[num1 + 1, num2] == 0 or vmap[num1 + 1, num2]:
            x = x + 1

        if vmap[num1 + 1, num2 + 1] == 0:
            x = x + 1

        if vmap[num1, num2 + 1] == 0:
            x = x + 1

        if vmap[num1 - 1, num2 + 1] == 0:
            x = x + 1

        if vmap[num1 - 1, num2] == 0:
            x = x + 1

        if vmap[num1 - 1, num2 - 1] == 0:
            x = x + 1

        if vmap[num1, num2 - 1] == 0:
            x = x + 1

        # Check that the position is free and there are 4 or less boxes with "0".
        if x <= 4 and vmap[num1, num2] == 0:
            i = 1

        # Case in which the selection is not valid
        if x > 4 or vmap[num1, num2] == 1:
            i = 0

    return (num1, num2)


from CreatePos import CreatePos
from OrderPicks import OrderPicks
import random
from Pick import Pick


def CreatePicks(vmap, map_list, mission, pos, picks, demand):
    vec = []
    ordered_vec = []

    if demand == 0:  # Low demand. Robots move throughout all the warehouse
        for i in range(0, picks):
            pick = Pick()
            pick.set_missionID(mission.get_ID())
            pick.set_pickID(i)
            pick.set_pos(
                CreatePos(
                    vmap, map_list, 0, demand  # Section not used when demand is low
                )
            )  # Generates a random position
            pick.set_actualwaittime(0)
            pick.set_picktime(0)
            pick.set_intersections(0)
            pick.set_humantime(0)
            vec.append(pick)  # Adds the position to the vector of picks

    if (
        demand == 1
    ):  # High demand. Robots move in three divided sections of the warehouse.
        section = random.randint(1, 3)
        for j in range(0, picks):
            pick = Pick()
            pick.set_missionID(mission.get_ID())
            pick.set_pickID(j)
            pick.set_pos(
                CreatePos(
                    vmap,
                    map_list,
                    section,
                    demand,  # Section not used when demand is low
                )
            )  # Generates a random position
            pick.set_actualwaittime(0)
            pick.set_picktime(0)
            pick.set_intersections(0)
            pick.set_humantime(0)
            vec.append(pick)  # Adds the position to the vector of picks

    # vec.insert(0, robot.get_pos())  # Adds the robot position to the vector of picks
    ordered_vec = OrderPicks(vec, pos)
    for i in range(0, len(ordered_vec) - 1):
        ordered_vec[i].set_pickID(i)
    mission.set_picks(ordered_vec)
    # Sort route by minimum distance

    # print("Pick positions: ", agente._picks)
    # print("pos: ", agente._pos)
    # Generates the following path

    return mission.get_picks()


from abc import ABC
import random
import copy
import pickle
from random import randint
from Robot import Robot  # Import Robot class from Robot.py file
from Human import Human  # Import Human class from Human.py file
from Mission import Mission  # Import Mission class from Mission.py file
from m_CTF import m_CTF  # Import m_CTF function from m_CTF.py file
from m_SPF import m_SPF  # Import m_SPF function from m_SPF.py file
from CreateRoute import (
    CreateRoute,
)  # Import CreateRoute function from CreateRoute.py file
from CreatePos import CreatePos  # Import CreatePos function from CreatePos.py file
from OrderPicks import OrderPicks  # Import OrderPicks function from OrderPicks.py file
from CreatePicks import (
    CreatePicks,
)  # Import CreatePicks function from CreatePicks.py file
from GenerateMissions import GenerateMissions
from Movement import Movement
from data_CSV import data_CSV
from m_Ses import m_SES


# Main

# Declaration of variables included in interface

# We declare map depending on the one introduced in the interface
# The variable array of the map has been created before.
import GUI_functions

if __name__ == "__main__":
    state = 0
    a = 0
    while a != 1:
        if state == 0:
            selection = GUI_functions.ini_GUI()
            if selection == 1:
                state = 1
            if selection == 2:
                state = 3
            if selection == 0:
                break
        if state == 1:
            initial_param = GUI_functions.data_intro_GUI()
            if initial_param["Selection"]:
                state = 2
                a = 1

            else:
                state = 0
            """
            execution_window = GUI_DataIntro.tk.Tk()
            execution_param = GUI_DataIntro.ExecutionParam()
            GUI_DataIntro.execution_GUI(execution_window, execution_param)
            execution_param.set_time(10, 10, 10)
            execution_window.mainloop()
            """


if initial_param["Selection_map"] == "Seseña":
    xmap = 2
elif initial_param["Selection_map"] == "Tarancón SPF":
    xmap = 0
else:
    xmap = 1
# 0: CTF, 1: SPF, 2: SES

if xmap == 0:
    vmap, map_list = m_CTF()  # Load the CTF map

elif xmap == 1:
    vmap, map_list = m_SPF()  # Load the SPF map

elif xmap == 2:
    vmap, map_list = m_SES()

# vmap = map variable

# Declaration of variables entered in interface

Num_Robots = int(initial_param["Num_Robots"])  # Number of robots
Num_Human = int(initial_param["Num_Humans"])  # Number of humans
random.seed(69)
High_demand_days = float(initial_param["High_Demand_Days"])
Low_demand_days = float(initial_param["Low_Demand_Days"])
Sim_days = High_demand_days + Low_demand_days

Sim_s = Sim_days * 60 * 60 * 24
High_demand_s = High_demand_days * 60 * 60 * 24
Low_demand_s = Low_demand_days * 60 * 60 * 24

Wave_time = float(initial_param["T_Wave"]) * 60 * 60  # Time between each wave

Missions_Wave = [
    int(initial_param["Num_Mission_min"]),
    int(initial_param["Num_Mission_max"]),
]  # Missions per wave

Picks_Mission = [
    int(initial_param["Num_Picks_min"]),
    int(initial_param["Num_Picks_max"]),
]  # Range of picks per tote


Missions_left = 0  # Remaining missions that have not been assigned

Num_Missions = 0  # Number of total missions

xt = 1


# Initialization of time variables

t = 0.0  # Total simulation time
tday = 0.0  # Time of day (0s to 86400s)
# Day zone (0 = day, 1 = evening, 2 = night) (0s-28800s, 28800s-57600s, 57600s-86400s)
zday = 0
twave = 0.0  # Wave time (0s to timeola s)
tmov = 0.0  # Robot and Human movement time

# Simulation execution time (only used for testing and printing, to be removed later)
texecution = 0.0

# Function declares instances depending on variables entered by user

robots = []
robots = [Robot(x) for x in range(0, Num_Robots)]

humans = []
humans = [Human(x, 1, 15) for x in range(0, Num_Human)]

missions = []

map_dict = {}
index = 3600

# We initialize humans at a random point on the map.
for i in range(Num_Human):
    humans[i].set_pos((randint(0, len(map_list) - 1), randint(0, len(map_list[0]) - 1)))
    while vmap[humans[i].get_pos()[0]][humans[i].get_pos()[1]] == 1:
        humans[i].set_pos(
            (randint(0, len(map_list) - 1), randint(0, len(map_list[0]) - 1))
        )
Missions_Assigned = 1


while t <= Sim_s:
    if Missions_left == 0 and xt == 0:
        print("Missions left finished", Missions_left, "Time", round(t, 2))
        xt = 1

    if Missions_left != 0:
        xt = 0

    if t > Sim_s - 1:
        print("Missions left", Missions_left)

    if t < High_demand_s:  # If we are in a period of high demand
        demand = 1

    elif t >= High_demand_s:  # If we are in a period of low demand
        demand = 0

    if twave >= Wave_time or t == 0:
        twave = 0.0

        # Generate wave

        num_mis_gen = randint(
            Missions_Wave[0], Missions_Wave[1]
        )  # Number of missions generated in each wave

        Missions_left = Missions_left + num_mis_gen
        Num_Missions = Num_Missions + num_mis_gen
    ret = 1
    while Missions_left > 0 and ret == 1:  # If Missions remain to be assigned
        # Assign missions
        mission = Mission(Missions_Assigned)
        ret = GenerateMissions(
            vmap, map_list, xmap, robots, mission, Picks_Mission, demand, t
        )  # Generate the missions

        if ret == 1:
            Missions_left = Missions_left - 1
            missions.append(mission)
            Missions_Assigned = Missions_Assigned + 1

    # Saves the map with all the robots
    vmap_save = copy.deepcopy(vmap)

    for x in range(len(missions)):
        vmap_save[
            robots[missions[x].get_robotassigned()].get_pos()[0],
            robots[missions[x].get_robotassigned()].get_pos()[1],
        ] = 2

    for human in humans:
        if vmap_save[human.get_pos()[0], human.get_pos()[1]] == 2:
            vmap_save[
                human.get_pos()[0],
                human.get_pos()[1],
            ] = 4
        else:
            vmap_save[
                human.get_pos()[0],
                human.get_pos()[1],
            ] = 3

    map_dict[round(t, 1)] = vmap_save.tolist()

    if t % 3600 < 1.4 and t != 0:
        name = "map_hour" + str(round(t / 3600)) + ".pickle"
        with open(name, "wb") as f:
            pickle.dump(map_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
            map_dict = {}

    for i in range(0, len(missions)):
        Movement(
            missions[i],
            missions,
            robots[missions[i].get_robotassigned()],
            robots,
            humans,
            xmap,
        )
    j = 0
    while j < len(missions):
        if missions[j].get_process() == 7:
            missions.pop(j)
        else:
            j = j + 1

    # Time Management

    if tday > 86400:  # If we have passed a day
        tday = 0  # Reset the time of day
        zday = 0  # Reset the time zone of the day to tomorrow

    # Update time variables and round to 1 decimal place (since sometimes it stays at .39999...)

    t = t + 1.4
    round(t, 1)  # Total simulation time
    tmov = tmov + 1.4
    round(tmov, 1)  # Robot and human movement time
    twave = twave + 1.4
    round(twave, 1)  # Wave time
    tday = tday + 1.4
    round(tday, 1)  # Time of day

    texecution = texecution + 1.4
    round(texecution, 1)

    if texecution > 10000:
        print("{:.1f}".format(t))
        texecution = 0
for i in range(0, len(missions)):
    data_CSV(missions[i])

name = "map_hour" + str(round(t / 3600)) + ".pickle"
with open(name, "wb") as f:
    pickle.dump(map_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
    map_dict = {}
