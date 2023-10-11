from CreatePicks import CreatePicks
from OrderPicks import OrderPicks
from GenerateMissions import GenerateMissions
from Robot import Robot
from Pick import Pick
from Mission import Mission
from MoveRobot import MoveRobot
from m_CTF import m_CTF

t = 0
xmap = 0
[vmap, map_list] = m_CTF()
robots = []
robots = [Robot(x) for x in range(0, 20)]
mission = Mission(1)
GenerateMissions(vmap, map_list, xmap, robots, mission, [2, 5], 0, t)
t = 0
while robots[mission.get_robotassigned()].get_pos() != mission.get_picks()[0].get_pos():
    if (
        robots[mission.get_robotassigned()].get_pos()
        != mission.get_picks()[0].get_pos()
    ):
        MoveRobot(
            robots[mission.get_robotassigned()],
            mission.get_picks()[0].get_pos(),
            vmap,
            mission.get_picks()[0],
        )
    t = t + 1
print(robots[mission.get_robotassigned()].get_dist())
