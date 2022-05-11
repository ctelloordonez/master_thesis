import matplotlib.pyplot as plt
import numpy as np

from utils import ASCII_to_dict


def main():
    participant = ASCII_to_dict()

    init_value = 0
    fin_value = 1001
    no_samples = np.arange(init_value, fin_value)
    m = (100-0) / (fin_value - init_value)
    b = 0 - m * init_value
    new_x = no_samples * m + b

    y = participant['V4']['R']['Angles']['T5']['St2_Knee_X']

    fig, ax = plt.subplots()
    ax.plot(new_x, y)
    ax.set(xlabel='Gait Cycle %', ylabel='Sagittal Knee Joint Angle [Degrees]',
           title='V4 R Knee angles')
    plt.savefig('data/plots/example_plot.png')
    plt.show()


if __name__ == '__main__':
    main()
