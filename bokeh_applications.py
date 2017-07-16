## in shell execute:
## bokeh serve --show myapp.py  or
## bokeh serve --show myappdir/
# Consult bokeh.pydata.org for more usages and examples

from bokeh.io import curdoc
from bokeh.plotting import figure

# Creating a simple line plot
plot = figure()
plot.line = ([1,2,3,4,5],[2,5,4,6,7])

curdoc().add_root(plot)

#######################################################################################
# Creating a slider that can be utilized
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(title='slider1', start=0,end=10,step=0.1,value=2)

# Create second slider: slider2
slider2 = Slider(title='slider2', start=10, end=100, step=1, value=20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1, slider2)

# Add the layout to the current document
curdoc().add_root(layout)

#######################################################################################
#Combining Bokeh models into layouts
# Create ColumnDataSource: source
source = ColumnDataSource(data={'x':x,'y':y})

# Add a line to the plot
plot.line('x','y', source=source)

# Create a column layout: layout
layout = column(widgetbox(slider),plot)

# Add the layout to the current document
curdoc().add_root(layout)

################################################
# Add the callback function so that the slider updates the plot

# Define a callback function: callback
def callback(attr,old,new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)


##################################################################################
#Updating plots from dropdowns
# Perform necessary imports
from bokeh.models import ColumnDataSource, Select

# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy':
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
        }

# Create a dropdown Select widget: select
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value',update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)


####################################################################
# buttons - callbacks are easier
from bokeh.models import buttons
button = Button(label='press me')
# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data= {'x':x, 'y':y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)

from bokeh.models import checkboxGroup, RadioGroup, Toggle

toggle = Toggle(label='Some on/off',button_type='success')
checkbox = checkboxGroup(labels=['foo','bar','baz'])
radio = RadioGroup(labels=['2000','2010','2020'])

def callback(active):
    # Active tells which button is active
