def judgeCircle(moves):
    count = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
    """Count number of U, D, L, R"""
    for x in moves:
        count[x] += 1

    return (count['U'] == count['D']) and (count['L'] == count['R'])
