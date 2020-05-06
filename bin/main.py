# This python file runs the main simulation and provides the output data to the Scatterplot file

# Import from config

from bin.config import *
import math

STEFANBOLTZMANNCONSTANT = 5.670373 * math.pow(10, -8)
WATERHEATCAPACITY = 4186

# Store the data in arrays
bodyTempData = [bodyTemp]
time = [0]

# First, we seek to calculate the heat lost from body without clothing in case numberOfClothing =0

# All heat lost in our scenario is due to radiation
# We use the Stefan-Boltzmann equation for radiation temperature loss given skin has a coefficient of emissivity near 1
if(numberOfClothing==0):
    surfaceArea = radius * 2 * math.pi * height

    for i in range(totalStep):
        diffTempFourthPower = math.pow(outerTemp, 4) - math.pow(bodyTemp, 4)
        # diffTemp should be negative if outer temp is less than body temp

        QDot = surfaceArea * diffTempFourthPower * STEFANBOLTZMANNCONSTANT
        bodyTemp += stepSize * QDot / weight / WATERHEATCAPACITY
        time.append((i+1)*stepSize)
        bodyTempData.append(bodyTemp)

    #graph(time, bodyTempData)



else:
    clothingTemp = outerTemp # We also wish to store clothingTemp data
    clothingTempData = [outerTemp]
    # I will be implementing simultaneous updates to numerically calculate integrals

    surfaceArea = distanceOfClothing(numberOfClothing-1) * 2 * math.pi * height

    for i in range(totalStep):
        diffTempFourthPower = math.pow(outerTemp, 4) - math.pow(bodyTemp, 4)
        # diffTemp should be negative if outer temp is less than body temp

        QDot = surfaceArea * diffTempFourthPower * STEFANBOLTZMANNCONSTANT
        bodyTemp += stepSize * QDot / weight / WATERHEATCAPACITY
        time.append((i + 1) * stepSize)
        bodyTempData.append(bodyTemp)



