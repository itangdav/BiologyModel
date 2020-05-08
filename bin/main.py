# This python file runs the main simulation and provides the output data to the Scatterplot file
import bin.Scatterplot
# Import from config
import bin.config
bodyTemp = bin.config.bodyTemp
numberOfClothing = bin.config.numberOfClothing
radius = bin.config.radius
totalStep = bin.config.totalStep
outerTemp = bin.config.outerTemp
height = bin.config.height
weight = bin.config.weight
distanceOfClothing = bin.config.distanceOfClothing
k = bin.config.k
cOuter = bin.config.cOuter
density = bin.config.density
stepSize = bin.config.stepSize
Qinternal = bin.config.Qinternal


#TODO: from bin.Scatterplot import plot
import math

STEFANBOLTZMANNCONSTANT = 5.670373 * math.pow(10, -8)
WATERHEATCAPACITY = 4186



# First, we seek to calculate the heat lost from body without clothing

# All heat lost in our scenario is due to radiation
# We use the Stefan-Boltzmann equation for radiation temperature loss given skin has a coefficient of emissivity near 1

# Store the data in arrays
noClothingBodyTempData = [bodyTemp]
time = [0]
surfaceArea = radius * 2 * math.pi * height

for i in range(totalStep):
    diffTempFourthPower = math.pow(outerTemp, 4) - math.pow(bodyTemp, 4)
    # diffTemp should be negative if outer temp is less than body temp

    QDot = surfaceArea * diffTempFourthPower * STEFANBOLTZMANNCONSTANT
    bodyTemp += stepSize * (QDot+Qinternal) / weight / WATERHEATCAPACITY
    time.append((i+1)*stepSize)
    noClothingBodyTempData.append(bodyTemp)
#Refresh all parameters
bodyTemp = bin.config.bodyTemp

if numberOfClothing>0:
    # Store the data in arrays
    withClothingBodyTempData = [bodyTemp]
    # This represents the temperature of the outermost layer of clothing
    clothingTemp = outerTemp
    clothingTempData = [outerTemp]

    # Implementing simultaneous updates to numerically calculate integrals

    surfaceArea = distanceOfClothing[numberOfClothing-1] * 2 * math.pi * height

    diffSquare=0
    if numberOfClothing==1:
        diffSquare = distanceOfClothing[numberOfClothing-1]*distanceOfClothing[numberOfClothing-1] - radius*radius
    else:
        diffSquare = distanceOfClothing[numberOfClothing-1]*distanceOfClothing[numberOfClothing-1] - distanceOfClothing[numberOfClothing-2]*distanceOfClothing[numberOfClothing-2]
    outerClothingWeight = density * math.pi * height * diffSquare
    totalResistance = 0

    for j in range(numberOfClothing):
        r_1 = 0.0
        if j == 0:
            r_1 = radius
        else:
            r_1 = distanceOfClothing[j - 1]
        r_2 = distanceOfClothing[j]
        totalResistance += math.log(r_2 / r_1) / (2 * math.pi * k[j] * height)
    for i in range(totalStep):
        diffTempFourthPower = math.pow(outerTemp, 4) - math.pow(clothingTemp, 4)

        # diffTemp should be negative if outer temp is less than body temp
        # Implements simultaneous update
        QDotRadiation = surfaceArea * diffTempFourthPower * STEFANBOLTZMANNCONSTANT

        QDotTransfer = (bodyTemp - clothingTemp)/totalResistance

        clothingTemp += stepSize * QDotRadiation / outerClothingWeight / cOuter
        clothingTemp += stepSize * QDotTransfer / outerClothingWeight / cOuter
        # Note the minus sign in front of the Qinternal cancels with the minus in the equation
        bodyTemp -= stepSize * (QDotTransfer-Qinternal) / weight / WATERHEATCAPACITY

        withClothingBodyTempData.append(bodyTemp)
        clothingTempData.append(clothingTemp)
    bin.Scatterplot.plot2(time, noClothingBodyTempData, withClothingBodyTempData)
else:
    bin.Scatterplot.plot(time, noClothingBodyTempData)

