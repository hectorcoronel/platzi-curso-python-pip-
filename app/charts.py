import matplotlib.pyplot as plt
# el as genera un alias para hacer mas facil poder llamar la libreria en el proyecto

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./img/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 300]
    generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)
