import plotly
import plotly.graph_objs as go
from scipy import stats
from bin.config import name

X_COORDS = []
Y_COORDS = []
Y_COORDS2 = []
DATA = []


def initialize_coords2(X, Y1, Y2):
    for i in range(len(X)):
        X_COORDS.append(X[i])
        Y_COORDS.append(Y1[i]-273.15) # Convert to Celsius
        Y_COORDS2.append(Y2[i]-273.15)
    counter = 0
    while counter < len(X_COORDS):
        if X_COORDS[counter] is None or Y_COORDS[counter] is None or Y_COORDS2[counter] is None:
            X_COORDS.pop(counter)
            Y_COORDS.pop(counter)
            Y_COORDS2.pop(counter)
        else:
            counter += 1


def initialize_coords(X, Y1):
    for i in range(len(X)):
        X_COORDS.append(X[i])
        Y_COORDS.append(Y1[i]-273.15) # Convert to Celsius
    counter = 0
    while counter < len(X_COORDS):
        if X_COORDS[counter] is None or Y_COORDS[counter] is None:
            X_COORDS.pop(counter)
            Y_COORDS.pop(counter)
        else:
            counter += 1


def format_layout():
    layout = go.Layout(
        hovermode='closest',
        xaxis=dict(
            title=X_AXIS,
            ticklen=5,
            zeroline=False,
            gridwidth=2,
        ),
        yaxis=dict(
            title=Y_AXIS,
            ticklen=5,
            gridwidth=2,
        )
    )
    return layout


global X_AXIS, Y_AXIS;
X_AXIS = "Time (s) ";
Y_AXIS = "Temperature (degrees Celsius) ";


def plot2(X, Y1, Y2):
    initialize_coords2(X, Y1, Y2)
    layout = format_layout()
    DATA.append(go.Scatter(
        x=X_COORDS,
        y=Y_COORDS,
        mode='markers',
        name="noClothing"
    ))
    DATA.append(go.Scatter(
        x=X_COORDS,
        y=Y_COORDS2,
        mode='markers',
        name="withClothing"
    ))

    filename = "plots/" + name + ".html"
    plotly.offline.plot({
        "data": DATA,
        "layout": layout,
    }, auto_open=True, filename=filename)


def plot(X, Y1):
    initialize_coords(X, Y1)
    layout = format_layout()
    DATA.append(go.Scatter(
        x=X_COORDS,
        y=Y_COORDS,
        mode='markers',
        name="noClothing"
    ))


    filename = "plots/" + name + ".html"
    plotly.offline.plot({
        "data": DATA,
        "layout": layout,
    }, auto_open=True, filename=filename)