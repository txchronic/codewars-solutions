def closest_pair(points: tuple) -> tuple:
    def distance(p1: tuple, p2: tuple) -> float:
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def brute_force(p: list) -> tuple:
        dist = float('inf')
        pair = []

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                cur_dist = distance(p[i], p[j])
                if cur_dist < dist:
                    dist = cur_dist
                    pair = [p[i], p[j]]

        return dist, pair[0], pair[1]

    def closest_split(px: list, py: list, d: float) -> tuple:
        x_mid = px[len(px) // 2][0]
        strip = [p for p in py if x_mid - d <= p[0] <= x_mid + d]

        best = d
        best_pair = px[0]

        for i in range(len(strip)):
            for j in range(1, min(8, len(strip) - i)):
                cur_dist = distance(strip[i], strip[i + j])
                if cur_dist < best:
                    best = cur_dist
                    best_pair = strip[i], strip[i + j]

        return best, best_pair[0], best_pair[1]

    def closest(px: list, py: list) -> tuple:
        if len(px) < 4:
            return brute_force(px)

        left_x, left_y = sorted(px[:len(px) // 2], key=lambda p: p[0]), sorted(px[:len(px) // 2], key=lambda p: p[1])
        right_x, right_y = sorted(px[len(px) // 2:], key=lambda p: p[0]), sorted(px[len(px) // 2:], key=lambda p: p[1])

        d_l, p1_l, p2_l = closest(left_x, left_y)
        d_r, p1_r, p2_r = closest(right_x, right_y)
        d_split, p1_s, p2_s = closest_split(px, py, min(d_l, d_r))

        min_dist = min(d_l, d_r, d_split)

        if min_dist == d_l:
            return d_l, p1_l, p2_l
        elif min_dist == d_r:
            return d_r, p1_r, p2_r
        else:
            return d_split, p1_s, p2_s

    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])

    return closest(points_x, points_y)[1:]
