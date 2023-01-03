def closest_pair(points: tuple) -> tuple:
    def distance(x: tuple, y: tuple) -> float:
        return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    
    def bruteforce(p: list) -> tuple:
        dist = float('inf')
        pair = []

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if distance(p[i], p[j]) < dist:
                    dist = distance(p[i], p[j])
                    pair = [p[i], p[j]]
        
        return dist, pair[0], pair[1]

    def closest_split(px: list, py: list, d: float) -> tuple:
        x_bound = px[len(px) // 2][0]
        p_bound = [p for p in py if x_bound - d <= p[0] <= x_bound + d]

        best = d
        best_pair = px[0]

        for i in range(len(p_bound)):
            for j in range(1, min(8, len(p_bound) - i)):
                if distance(p_bound[i], p_bound[i + j]) < best:
                    best = distance(p_bound[i], p_bound[i + j])
                    best_pair = p_bound[i], p_bound[i + j]

        return best, best_pair[0], best_pair[1]

    def closest(px: list, py: list) -> tuple:
        if len(px) < 4:
            return bruteforce(px)
        
        pl, pr = px[:len(px) // 2], px[len(px) // 2:]
        
        pl_x, pl_y = sorted(pl, key=lambda p: p[0]), sorted(pl, key=lambda p: p[1])
        pr_x, pr_y = sorted(pr, key=lambda p: p[0]), sorted(pr, key=lambda p: p[1])

        dl, pl_1, pr_1 = closest(pl_x, pl_y)
        dr, pl_2, pr_2 = closest(pr_x, pr_y)
        dc, pl_3, pr_3 = closest_split(px, py, min(dl, dr))

        d_min = min(dl, dr, dc)

        if d_min == dl:
            return dl, pl_1, pr_1
        elif d_min == dr:
            return dr, pl_2, pr_2
        else:
            return dc, pl_3, pr_3

    p_x = sorted(points, key=lambda p: p[0])
    p_y = sorted(points, key=lambda p: p[1])

    return closest(p_x, p_y)[1:]