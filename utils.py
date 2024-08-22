import math


def check_float(el) -> bool:
    try:
        float(el)
        return True
    except ValueError:
        return False


def round_to_1_sf(num):
    return round(num, -int(math.floor(math.log10(abs(num)))))
