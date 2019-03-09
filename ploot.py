import matplotlib.pyplot as plt
def plut(generation, score):
    #X = [] #generation
    #Y = [] #score

    plt.scatter(generation, score)
    plt.plot(generation, score, '.r-')
    plt.title('Graph between generation and score')
    plt.show()
    plt.savefig('plot.png')