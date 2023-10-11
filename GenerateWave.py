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
