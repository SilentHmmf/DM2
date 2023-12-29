import matplotlib.pyplot as plt
def writeFromFile(file):
    fin = open(file)
    list1 = list(map(int, fin.readline().split()))
    list2 = list(map(int, fin.readline().split()))

    fig, ax = plt.subplots()


    ax.plot(list1, label='график машины Тьюринга')

    ax.plot(list2, label='график алгоритма Маркова')

    ax.legend()

    ax.set_title('Графики итераций МТ и АМ')
    ax.set_xlabel('Кол-во едениц во втором числе')
    ax.set_ylabel('Кол-во итераций')

    plt.show()