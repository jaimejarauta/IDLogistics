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
