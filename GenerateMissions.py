from random import randint
from m_CTF import m_CTF
from CreatePicks import CreatePicks
from CreateRoute import CreateRoute


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
