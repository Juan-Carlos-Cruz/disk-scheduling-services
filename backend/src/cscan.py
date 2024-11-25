def cscan(arm_position, lrequests, disk_size=200, debug=False):
    """
    C-SCAN implementation (Circular SCAN)

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
        disk_size (int): maximum disk size (default: 200)
    """
    distance = 0
    current_pos = arm_position
    sequence = [arm_position]
    requests = sorted(lrequests)

    left = [r for r in requests if r < arm_position]
    right = [r for r in requests if r >= arm_position]

    for r in right + [0] + left:
        distance += abs(r - current_pos)
        current_pos = r
        sequence.append(current_pos)
        if debug: print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

# print(cscan(96, [125,17,23,67,90,128,189,115,97]))