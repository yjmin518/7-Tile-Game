import heapq

def get_pos(state):
        pos = {}
        for i in range(3):
            for j in range(3):
                pos[state[i * 3 + j]] = (i, j)
        return pos

def get_manhattan_distance(from_state, to_state = [1, 2, 3, 4, 5, 6, 7, 0, 0]):
    from_pos = get_pos(from_state)
    to_pos = get_pos(to_state)
    manhattan_distance = 0
    for num in from_state:
        if num != 0:
            fromx, fromy = from_pos[num]
            tox, toy = to_pos[num]
            manhattan_distance += abs(fromx - tox) + abs(fromy - toy)
    return manhattan_distance

def get_succ(state):
    possmoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    succ = []
    empty= [i for i, val in enumerate(state) if val == 0]
    for slot in empty:
        row, col = divmod(slot, 3)
        for rc, cc in possmoves:
            nrow, ncol = row + rc, col + cc
            if 0 <= nrow < 3 and 0 <= ncol < 3:
                new = state[:]
                new[slot], new[nrow * 3 + ncol] = new[nrow * 3 + ncol], new[slot]
                if new != state:
                    succ.append(new)
    return sorted(succ)

def print_succ(state):
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))

def solve(state, goal_state = [1, 2, 3, 4, 5, 6, 7, 0, 0]):
    max_length = 0
    Open = []
    closed = []
    In = (get_manhattan_distance(state), state, (0, get_manhattan_distance(state), -1))
    heapq.heappush(Open, In)
    pid = -1
    parents = {}
    while Open:
        max_length = max(max_length, len(Open))
        cnode = heapq.heappop(Open)
        cstate = cnode[1]
        pid += 1
        parents[pid] = cnode
        closed.append(cstate)
        if cstate == goal_state:
            path = [cstate]
            rid = pid
            while rid != -1:
                pstate = parents[rid][1]
                path.append(pstate)
                rid = parents[rid][2][2]
            path = path[1:][::-1]
            break
        for s in get_succ(cstate):
            h = get_manhattan_distance(s)
            g = cnode[2][0] + 1
            f = h + g
            n = (f, s, (g, h, pid))
            if s in closed or n in Open:
                continue
            heapq.heappush(Open, n)
    move = 0
    for state in path:
        current_state = state
        h = get_manhattan_distance(state)
        print(current_state, "h={}".format(h), "moves: {}".format(move))
        move += 1
    print("Max queue length: {}".format(max_length))

initial_state = [4, 3, 0, 5, 1, 6, 7, 2, 0]
goal_state = [1, 2, 3, 4, 5, 6, 7, 0, 0]
solve(initial_state, goal_state)