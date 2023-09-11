coords = [tuple(map(int, input().split())) for _ in range(3)]
ccw = coords[0][0] * coords[1][1] + coords[1][0] * coords[2][1] + coords[2][0] * coords[0][1] - \
      coords[1][0] * coords[0][1] - coords[2][0] * coords[1][1] - coords[0][0] * coords[2][1]

if ccw:
    print(int(ccw/abs(ccw)))
else:
    print(ccw)