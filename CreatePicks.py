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
