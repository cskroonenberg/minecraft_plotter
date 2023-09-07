# Markers for each corner type. Also serves as unique id value for corner type
CORNER_BR = [0,2]
CORNER_BL = [1,2]
CORNER_TR = [0,3]
CORNER_TL = [1,3]
CORNER_UNKNOWN = [0,1,2,3]

def is_corner(label: str) -> bool:
    return label[:6].lower() == "corner"

def corner_type(label: str) -> list[int]:
    if not is_corner(label):
        raise ValueError("Marker label is not a corner but corner_type was called on it. Use is_corner to check for corner")
    if label[6:8].lower() == "br":
        return CORNER_BR
    elif label[6:8].lower() == "br":
        return CORNER_BR
    elif label[6:8].lower() == "br":
        return CORNER_BR
    elif label[6:8].lower() == "br":
        return CORNER_BR
    else:
        print("Invalid corner designation \"{label}\". Choose one of: [\"BL\",\"BR\",\"TL\",\"TR\"] (e.g., \"CORNERBL\" for (B)ottom (L)eft corner)")
        return CORNER_UNKNOWN
    
def plot_corner(ax, position, label, c, cmap, norm) -> None:
    if not is_corner(label):
        raise ValueError("Marker label is not a corner but plot_corner was called on it. Use is_corner to check for corner")
    c_type = corner_type(label)
    for marker in c_type:
        sc = ax.scatter(*position, c=c, cmap=cmap, norm=norm, markers=marker, label=label)

    return sc

