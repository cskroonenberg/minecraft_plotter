import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
import argparse as argparse
from math import ceil
import corner, walkway, debugger

parser = argparse.ArgumentParser()
parser.add_argument("--plot_3d", action="store_true", default=False, help="Set to plot in 3D")
parser.add_argument("--plot_struct", action="store_true", default=False, help="Set to plot regions where structures can spawn")
parser.add_argument("--nether", action="store_true", default=False, help="Set to plot the Nether (otherwise, overworld is plotted)")
parser.add_argument("--hide_corners", action="store_true", default=False, help="Set to hide corner markers")
parser.add_argument("--hide_walk", action="store_true", default=False, help="Set to hide walkway markers")
parser.add_argument("--debug", action="store_true", default=False, help="Set to run debugger")

args = parser.parse_args()
print(args)
PLOT_3D = args.plot_3d
csv_path = "nether_coords.csv" if args.nether else "overworld_coords.csv"
crop=""
debug = debugger.Debugger(args.debug)

plotStructRegions = args.plot_struct
crop="ALL"

# Load the CSV file with coordinates
df = pd.read_csv(csv_path)

# Extract the x, y, z, and label values
x = df['x']
y = df['y']
z = df['z']
labels = df['label']
print(labels)
debug.set_flag()
# Create a scatter plot
fig = plt.figure()
if PLOT_3D:
    ax = fig.add_subplot(111,projection='3d')
else:
    ax = fig.add_subplot(111)
debug.set_flag()

if plotStructRegions:
    for i in range(ceil(z.min()/480),ceil(z.max()/480)):
        for j in range(ceil(x.min()/480)-1, ceil(x.max()/480)):
            bot_left_z = i*480
            bot_left_x = j*480
            rect = Rectangle((bot_left_x, bot_left_z), 416, 416, alpha=0.3, color='green')
            ax.add_patch(rect)
debug.set_flag()

# Normalize the Y values for color mapping
norm = plt.Normalize(y.min(), y.max())
cmap = plt.cm.jet
debug.set_flag()

# Create the scatter plot with colors based on Y intensity and markers based on labels
for label in labels:
    mask = labels == label
    if PLOT_3D:
        x[mask], z[mask], y[mask]
    else:
        position = x[mask], z[mask]

    # Check waypoint type and plot accordingly
    if not corner.is_corner(label) and not walkway.is_walkway(label):
        sc = ax.scatter(*position, c=y[mask], cmap=cmap, norm=norm, label=label)
    elif corner.is_corner(label) and not args.hide_corners:
        print("Plotting corner :)\t args.hide_corners = {args.hide_corners}")
        sc = corner.plot_corner(ax,position,label,y[mask],cmap,norm)
    elif walkway.is_walkway(label) and not args.hide_walk:
        print(f"Plotting corner :)\t args.hide_walk = {args.hide_walk}")
        sc = walkway.plot_walkway(ax,position,label,y[mask],cmap,norm)

        
debug.set_flag()


# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title("Nether" if args.nether else "Overworld")
debug.set_flag()

# Create a colorbar to show intensity
cbar = plt.colorbar(sc)
cbar.set_label('Y Level')
debug.set_flag()

# Label the points with their corresponding labels
for i, label in enumerate(labels):
    # Check skip conditions
    if corner.is_corner(label) and args.hide_corners:
        continue
    if walkway.is_walkway(label) and args.hide_walk:
        continue

    # Set text position
    if PLOT_3D:
        position = x[i], z[i]+2, y[i]
    else:
        position = x[i], z[i]+2

    # Plot text
    ax.text(*position, label, fontsize=8, ha="center")

debug.set_flag()

# Crop regions for Nether. This code could be handled better
if crop=="BASTION":
    plt.xlim(-190,-275)
    plt.ylim(310, 375)
if crop=="BIG":
    plt.xlim(-100,-960)
    plt.ylim(-100, 960)
debug.set_flag()

# Show the plot
debug.set_flag()
ax.invert_xaxis()
plt.show()
