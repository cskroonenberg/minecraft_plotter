def is_walkway(label: str) -> bool:
    return label[:7].lower() == "walkway"

def plot_walkway(ax, position, label, c, cmap, norm):
    return ax.scatter(*position, c=c, cmap=cmap, norm=norm, markers="s", label=label)