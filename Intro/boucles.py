# -*-coding:Latin-1 -*
import os


def table_multiple_nb(nb, mam=10):
    for i in range(1, mam + 1):
        print(nb, ' * ', i, ' = ', nb * i)

if __name__ == "__main__":
    table_multiple_nb(7)
    os.system("pause")
