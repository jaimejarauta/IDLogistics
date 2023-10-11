from CreatePos import CreatePos
from OrderPicks import OrderPicks
from m_CTF import m_CTF  # Import m_CTF function from m_CTF.py file
from m_SPF import m_SPF  # Import m_SPF function from m_SPF.py file
from CreateRoute import (
    CreateRoute,
)  # Import CreateRoute function from CreateRoute.py file
from MoveRobot import MoveRobot
from data_CSV import data_CSV
from m_Ses import m_SES

# from datarobot_CSV import datarobot_CSV
import random

import copy

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
