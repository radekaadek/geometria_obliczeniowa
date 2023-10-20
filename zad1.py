import matplotlib.pyplot as plt


def tofloat(numbers: list[str]) -> list[float]:
    try:
        retv = [float(x) for x in numbers]
        if len(retv) != 2:
            raise ValueError
        return retv
    except ValueError:
        raise ValueError("Podano błędne dane")


def det(A: list[int], B: list[int], P: list[int]) -> float:
    return A[0] * B[1] + B[0] * P[1] + P[0] * A[1] - P[0] * B[1] - A[0] * P[1] - B[0] * A[1]


def cross_product(A: list[int], B: list[int], P: list[int]) -> float:
    return (B[0] - A[0]) * (P[1] - A[1]) - (B[1] - A[1]) * (P[0] - A[0])


def main():
    A = tofloat(input("Podaj współrzędne punktu A po spacji: ").split())
    B = tofloat(input("Podaj współrzędne punktu B po spacji: ").split())
    P = tofloat(input("Podaj współrzędne punktu P po spacji: ").split())

    det_p = det(A, B, P)
    cross_p = cross_product(A, B, P)

    print(f"\n\nDet = {det_p:.5f}\n")
    print(f"\n\nIloczyn wektorowy = {cross_p:.5f}\n")

    if cross_p > 0:
        print("Punkt P leży po lewej stronie odcinka AB")
    elif cross_p < 0:
        print("Punkt P leży po prawej stronie odcinka AB")
    else:
        print("Punkty A, B i P są współliniowe")

    # prezentacja wyników na wykresie
    plt.plot([A[0], B[0]], [A[1], B[1]], color='blue', linewidth=2, linestyle='solid')
    plt.plot(P[0], P[1], color='green', marker='o', markersize=7)
    plt.text(A[0], A[1], 'A', color='blue', fontsize=12)
    plt.text(B[0], B[1], 'B', color='blue', fontsize=12)
    plt.text(P[0], P[1], 'P', color='green', fontsize=12)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
