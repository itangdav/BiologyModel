#Configuration file

# Parameters for Simulation

# The step of time between each data point in seconds
stepSize = 60
# The total number of steps taken until end of simulation
totalStep = 100


# Parameters for Human Model

# Body temperature of person in degrees Kelvin (add 273.15 to Celsius temperature)
bodyTemp = (37) + 273.15
# Temperature of outside surroundings in degrees Kelvin
outerTemp = (29) + 273.15
# Height of person in meters
height = 1.72
# Radius of person in direction parallel to floor in meters
radius = 0.15
# Weight of person in kg
weight = 70
# Number of clothing worn
numberOfClothing = 2
# An array for the distance of the outer layer of each piece of clothing from center axis in meters
# This must be sorted in increasing order and each distance must be greater than the radius of the person
distanceOfClothing = [0.16, 0.17]
# An array for thermal conductivity coefficients k given in W m^-1 K^-1 for each layer of clothing
# This must be in the same order as the previous array and the same size
k = [0.039, 0.14]
# Specific heat capacity of outer layer of clothing in J kg^-1 K^-1 (if numberOfClothing = 0, put 0)
cOuter = 1500
# Density of outer layer of clothing in kg m^-3
density = 860

