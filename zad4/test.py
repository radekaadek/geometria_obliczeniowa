from matplotlib import pyplot as plt
import numpy as np


def azymut(p1: tuple, p2: tuple) -> float:
    """Oblicza azymut do północy promienia łączącego dwa punkty.

    Args:
        p1 (tuple): Pierwszy punkt. (x, y)
        p2 (tuple): Drugi punkt. (x, y)

    Returns:
        float: Dodatni azymut w radianach.
    """
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    azymut_rad = np.arctan2(delta_y, delta_x)
    
    # Zamień azymut na zakres od 0 do 2*pi
    azymut_rad = (azymut_rad + 2 * np.pi) % (2 * np.pi)
    return azymut_rad


# print(azymut((180.0, 415.435), (300.0, 315.067)))
# print(azymut((180.0, 415.435), (200, 340)))

deg_angles = [i * 10 for i in range(36)]
rad_angles = [np.deg2rad(i) for i in deg_angles]
# create points on circle
points = [(np.cos(i), np.sin(i)) for i in rad_angles]
# print(points)
azymuts = list(map(lambda x: azymut((0, 0), x), points))
for i in range(len(points)):
    print(deg_angles[i], np.rad2deg(azymuts[i]))

pts = [(180.0, 300.0), (415.435, 315.067), (200, 340)]
print(azymut(pts[0], pts[1]))
print(azymut(pts[0], pts[2]))
plt.plot([i[0] for i in pts], [i[1] for i in pts], 'ro')
plt.show()
