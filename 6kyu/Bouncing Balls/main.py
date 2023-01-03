from math import log


def bouncing_ball(h: float, bounce: float, window: float) -> int:
    if h > 0 and 0 < bounce < 1 and window < h:
        return int((log(window + 0.001) - log(h)) / log(bounce)) * 2 + 1
    else:
        return -1