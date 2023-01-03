from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    time = 0
    while bridge:
        bridge_weight -= bridge.popleft()
        if trucks:
            if (bridge_weight + trucks[0]) <= weight:
                t = trucks.popleft()
                bridge.append(t)
                bridge_weight += t
            else:
                bridge.append(0)
        time += 1
    return time