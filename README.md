
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# PleePlee Robot

![logo](https://github.com/pleeplee-robot/location/blob/master/resources/logo-pleeplee.png)

PleePlee is a proof of concept of a mobile gardener robot.
This repository is about the code for miscellaneous components of the robot.
It contains the code and documentation for:
- the camera
- the LEDs
- the motor driver
- the odometric captors

## Features

The PleePlee robot is able to:
- :seedling: :shower: Water plants.
- :car: Move in a straight line and turn in place.
- :bulb: :satellite: Localize itself in a small area delimited by luminous landmarks.
- :curly_loop: Avoid obstacles.
- :eyes: Log any changes to the garden. (Foreign object or person crossing).


## Interface

This repository is about the graphical interface used to initialise and
configure the robot. The user fist has to initialize the map. Then after the setup phase of the
robot, it is used to correct mistakes and clarify the map. For example
the robot only recognize an obstacle, it will be the user job through this
interface to dissociate between plants and real obstacles. When processing the data fetched by the 
robot the user will also be able to setup interval watering for each plant.

## How to Build

This a python project to build it, just use the `make init` command in the root of the repository. This will downloaded the needed package and run the application.

## How to Run

Use `make` in the source directory

## Initialization

When you launch the application you must see a menu with 2 buttons. The first one is for the initialization
and the second one aims to fetch the data retrieved by the robot during the mapping. This size and dimension rely 
on the .config file in the source repository, all the user have to do is to provied the longest size of the garden.

<p align="center">
<img src="assets/examples/init_menu.png" width="550">
</p>

Once the initialization is run, the user can add the balises that delimits the perimeter of the garden.
To add a balise you just have to enter its coordinate and color then click on the button "add balise".
When you are done with the main balises you can click on the "done" button. This, will draw the garden 
on the screen and let you add additionnals balises.

<p align="center">
<img src="assets/examples/balise_placing.png" width="550"><img src="assets/examples/balise_placing_2.png" width="550">
</p>

The user have to click on the "Finish" button to finalize the initialization. This action will create two files: data_json,
map.capture_init. At this point data_json contains in Json format, the positions of the different balises. On the other hand, map.capture_init contains an array of characters 'D' or 'G'. 'D' for dust, and 'G' for grass. This will later be overwritten by
the robot which will write 'P' when finding plants, and 'O' for obstacles. The initialization is done, to pass the data to the robot in a directory named "fetch".

## Fetch

Once the robot as done its mapping, you must retrieve the "fetch" directory with the new data_json and map.capture_init files.
The directory msut be at the root of the application repository. To start processing the fetched data, you must relaunch the application and click this time on the second button in the menu.

<p align="center">
<img src="assets/examples/fetched_data.png" width="550">
</p>

On the above screen, you can see the garden with a plant and a box drawn on it. This is because the robot during the mapping has encountered one plant and one obstacle. The user can now click on the plant to set it watering if this is a real plant and not a false positive. Otherwise it could delete it, to ignore it. The obstacles are visible to alert the detection of new object/obstacle in the garden. When an object is selected you can see its picture taken by the robot. To save all the change you can click on the "Finish" button.

## Documentation of the project

The documentation is generated with sphinx.

You can get the documentation of the project by installing the package as specified above and just running the `make doc` command.
Then use your favorite web navigator to open the `index.html` located in `docs/build/html`.
