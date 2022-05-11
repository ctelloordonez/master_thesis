import matplotlib.pyplot as plt

from utils import ASCII_to_dict


def main():
    participant = ASCII_to_dict()

    x = participant['V4']['R']['Angles']['T5']['St2_Knee_X']
    fig, ax = plt.subplots()
    ax.plot(range(0, 1001), x)
    ax.set(xlabel='Gait Cycle %', ylabel='Sagittal Knee Joint Angle [Degrees]',
           title='V4 R Knee angles')
    plt.savefig('data/plots/example_plot.png')
    plt.show()


if __name__ == '__main__':
    main()
