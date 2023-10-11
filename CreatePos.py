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
