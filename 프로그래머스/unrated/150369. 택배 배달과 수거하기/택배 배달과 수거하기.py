def solution(cap, n, deliveries, pickups):
    dist = 0
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        dist += max(len(deliveries) * 2, len(pickups) * 2)
        tmp = cap
        for x in [deliveries, pickups]:
            tmp = cap
            while x and tmp > 0:
                if tmp - x[-1] >= 0:
                    tmp -= x[-1]
                    x.pop()
                elif tmp < x[-1]:
                    x[-1] -= tmp
                    break
    return dist