import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def set_labels(ax: plt.Axes, title: str, fontsize: int) -> plt.Axes:
    """Modify axes labels

    Formats labels from snake case, sets text color to grey

    Args:
        ax (plt.Axes): axis of plot to update
        title (str): title of plot
        fontsize (int): fontsize of smaller lables (xlabel, ylabel, legend title)

    Returns:
        plt.Axes: axis of plot to update
    """

    ax.set_xlabel(
        xlabel=ax.get_xlabel().replace("_", " ").capitalize(),
        color="grey",
        fontsize=fontsize,
    )
    ax.set_ylabel(
        ylabel=ax.get_ylabel().replace("_", " ").capitalize(),
        color="grey",
        fontsize=fontsize,
    )
    ax.set_title(
        title,
        pad=10,
        fontsize=np.ceil(fontsize * 1.3),
        color="grey",
    )
    # if legend exists then also update
    if ax.get_legend() is not None:
        handles, labels = ax.get_legend_handles_labels()
        labels = [label.replace("_", " ").capitalize() for label in labels]
        ax.legend(
            title=ax.get_legend().get_title().get_text().replace("_", " ").capitalize(),
            handles=handles,
            labels=labels,
            labelcolor="grey",
        )
        ax.get_legend().get_title().set_color("grey")
    return ax



def style_plot(ax: plt.Axes) -> plt.Axes:
    """styles plot

    Sets major x gridlines, modify axis, ticks and labels

    Args:
        ax (Axes):  axis of plot to update

    Returns:
        Axes:  axis of plot to update
    """
    sns.despine()
    ax.grid(which="major", alpha=0.5, linestyle=":", axis="x")
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_linewidth(2)
        ax.spines[spine].set_color("lightgray")
        ax.tick_params(
            width=1,
            color="grey",
            length=4,
            labelcolor="grey",
            labelfontfamily="sans-serif",
        )
    return ax
