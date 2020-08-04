def plot_with_rookies(x0, y0, list0, x_rookie, y_rookie, list_rookie, xlabel, ylabel, title, slope, intercept, ylimmin,
                      ylimmax):
    """

    :param x0:
    :param y0:
    :param list0:
    :param x_rookie:
    :param y_rookie:
    :param list_rookie:
    :param xlabel:
    :param ylabel:
    :param title:
    :param slope:
    :param intercept:
    :param ylimmin:
    :param ylimmax:
    :return:
    """
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.scatter(x0, y0, marker='*', color='#E84A27', s=500)
    line_plot(slope, intercept, 0.82, 1, 1000, ax)
    plt.ylim(ylimmin, ylimmax)
    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(ylabel, fontsize=25)
    ax.set_title(title, fontsize=25)
    for i in range(len(list0)):
        plt.annotate(list0[i], xy=(x0[i], y0[i]), xytext=(x0[i], y0[i] - ylimmax / 20), fontsize=15)

    ax.scatter(x_rookie, y_rookie, marker='*', color='#13294B', s=500)
    for i in range(len(list_rookie)):
        if i != 1:
            plt.annotate(list_rookie[i], xy=(x_rookie[i], y_rookie[i]),
                         xytext=(x_rookie[i], y_rookie[i] - ylimmax / 20), fontsize=15)
        else:
            plt.annotate(rookie_list[i], xy=(x_rookie[i], y_rookie[i]),
                         xytext=(x_rookie[i] - 0.015, y_rookie[i] + ylimmax / 30), fontsize=15)