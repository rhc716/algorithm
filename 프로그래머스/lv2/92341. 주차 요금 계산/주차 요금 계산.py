import math

def solution(fees, records):
    def timeToMin(strTime):
        return int(strTime[0:2]) * 60 + int(strTime[3:5])
    record = {}
    times = {}
    lastMin = timeToMin('23:59')
    for r in records:
        time, car, gbn = r.split(' ')
        car = int(car)
        if gbn == 'IN':
            record[car] = timeToMin(time)
        else:
            useTime = timeToMin(time) - record[car]
            del record[car]
            if car in times:
                times[car] += useTime
            else:
                times[car] = useTime
    for key in record:
        useTime = lastMin - record[key]
        if key in times:
            times[key] += useTime
        else:
            times[key] = useTime
    times = [times[x] for x in sorted(times)]
    return [fees[1] if t <= fees[0] else fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3] for t in times]