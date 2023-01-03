from datetime import datetime

def solution(m, musicinfos):
    sharps = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': '4', 'A#': '5'}
    for x in sharps:
        m = m.replace(x, sharps[x])
    answer = []
    for i, info in enumerate(musicinfos):
        t_start, t_end, name, melody = info.split(',')
        t_play = int((datetime.strptime(t_end, '%H:%M') - datetime.strptime(t_start, '%H:%M')).total_seconds()/60)
        for x in sharps:
            melody = melody.replace(x, sharps[x])
        melody = melody[:t_play] if len(melody) >= t_play else (melody * int(t_play/len(melody) + 1))[:t_play]
        if m in melody:
            answer.append([t_play, i, name])
    if answer:
        return sorted(answer, key = lambda x: (-x[0], x[1]))[0][2]
    return '(None)'