import math, sys
PI = math.pi
VERSION = sys.version.split()[0]

def circle_area(r): return PI * r ** 2
def circle_len(r):  return 2 * PI * r
def _helper():      return PI / 2

if__name__ == "__main__":
    print(f"[{VERSION}] Самопроверка mymodule:")
    print(" S(r=2)=", circle_area(2))
    print(" L(r=2)=", circle_len(2))