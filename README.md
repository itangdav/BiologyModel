# BiologyModel
Project for Grade 12 Biology modelling heat loss and homeostasis using numerical integrals and physics equations

For my model, I will assume based on published results that the coefficient of emissivity of human skin and clothing is around unity.
Also, I will be assuming that the specific heat capacity for a human body is approxiamately the specific heat capacity of water, or 4186 J/kg. In addition, the model will assume the power produced by the human body is constant throughout the entire time. You can change it by modelling every time period between the changes seperately. 

To use this, you require a python compiler. The following files will be found in the "bin" folder. Using the compiler, run the main.py file and to change the parameters, edit the config.py file. The output graphs should be directly in the graphs folder. There will be a sample graph for the sample config file already in there. 

Notes on the sample:
Most of the human features are accurate for the average Canadian male
I used two pieces of clothing, both with a thickness of 1 cm or 0.01m. The first one was a wool shirt and the second one was a leather jacket.

Notes on config: 
Keep in mind all constants are given in standard SI units, so every number imputted must also be in SI units (seconds, kg, meters, etc).

Notes on Scatterplot:
It requires you to install the plotly add-on for python. If you are using a python compiler like PyCharm, you should get a message prompting the installing of plotly though pip-install. 
