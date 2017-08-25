def main():
    a = float(raw_input("Unesite kvadratni clan a: "))
    b = float(raw_input("Unesite linearni clan b: "))
    c = float(raw_input("Unesite slobodni clan c: "))

# modification to create new branch
    quadratic_equation_solution(a, b, c)


def quadratic_equation_solution(a, b, c):
    if a != 0:
        x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        y = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        print('Resenja jednacine su x = %s , y = %s' % (x, y))
    else:
        x = -c / b
        print('Jednacina ima samo jedno resenje x= %s' % x)


if __name__ == "__main__": main()
