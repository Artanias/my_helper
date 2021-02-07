import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


# Дописать возможность выбирать как часто пополнять - раз в месяц либо раз в год
# Дописать капитализацию раз в год
def calc_contrib(percentage=1, years=10, start_val=10000,
                 add=0, capitaliz=0):
    MONTHS = 12
    earn = np.zeros((years + 1, MONTHS))

    if capitaliz == 0 or capitaliz == 1:
        for year in range(years + 1):
            earn[year][0] = start_val
            for month in range(1, MONTHS):
                earn[year][month] = (earn[year][month - 1] * 
                                    (1 + percentage / 100 / 12) + add)
            start_val = earn[year][11] * (1 + percentage / 100 / 12) + add
    elif capitaliz == 1:
        pass

    df = pd.DataFrame(earn, index=range(0, years + 1),
                      columns=['Янв', 'Фев', 'Март', 'Апр',
                               'Май', 'Июнь', 'Июль', 'Авг',
                               'Сен', 'Окт', 'Нояб', 'Дек'])
    df.index.name = 'Год'

    return df


def save_plot(df, path="contrib.png"):
    plot = sns.jointplot(x=df.index, y=df['Янв'],
                         kind='reg',
                         xlim=(df.index.start, df.index.stop))
    plt.ylabel('Сумма вклада')
    plt.plot([0, df.index.stop],
             [df.iloc[-1, 0], df.iloc[-1, 0]], 'go--',
             linewidth=1, color='black', marker=',')
    plt.ylim((0, plt.ylim()[1]))
    plot.savefig(path)


if __name__ == '__main__':
    earn = calc_contrib()
    save_plot(earn)