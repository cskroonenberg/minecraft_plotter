# minecraft_plotter
Plot waypoints in your Minecraft world with Matplotlib.

Store relevant waypoints in CSV files. `minecraft_plotter.py` will plot them.

## Getting Started
```bash
# Clone repo
git clone https://github.com/cskroonenberg/minecraft_plotter
cd minecraft_plotter

# Init coordinate CSVs
echo "x,y,z,label" > overworld.csv
echo "x,y,z,label" > nether.csv

# Add waypoints to overworld.csv or nether.csv: <X>, <Y>, <Z>, <WAYPOINT-LABEL>

# Plot Overworld coordinates
python3 minecraft_plotter.py

# Plot Nether coordinates
python3 minecraft_plotter.py --nether

# See all plotting options
python3 minecraft_plotter.py -h
```
