from collections import deque

def solution(cacheSize, cities):
    cache = deque([None] * 4, maxlen=cacheSize)
    cities = list(map(lambda x: x.lower(), cities))
    time = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    for c in cities:
        if c in cache:
            del cache[cache.index(c)]
            cache.appendleft(c)
            time += 1
        elif len(cache) != cache.maxlen:
            cache.appendleft(c)
            time += 5
        else:
            cache.pop()
            cache.appendleft(c)
            time += 5
    return time