def solution(files):
    newArr = []
    for i, v in enumerate(files):
        head = ''
        number = ''
        for c in v:
            if c.isdigit():
                number += c
            else:
                if number == '':
                    head += c
                else:
                    break
        newArr.append([head.lower(), int(number), i])
    newArr.sort(key=lambda x: (x[0], x[1], x[2]))
    return [files[x[2]] for x in newArr]