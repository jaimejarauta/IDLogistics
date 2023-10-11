import copy
from CreateRoute import CreateRoute

import numpy as np
from matplotlib import pyplot
from matplotlib import colors


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
