# Spicerack
This project helps you find spice bottles and put them back in the right place through speech and lights.

## Introduction

This project helps you quickly locate a particular spice in a crowded spice cabinet. You can use your voice to ask “Where is the cinnamon?” and it will tell you the shelf and row of the spice.

There is a second, optional level of functionality. If the spice rack is registered, it will turn on a light above the spice bottle’s location.

## About the code

This is written in Python.

* It's not (yet) in the format that can be zipped and uploaded to Amazon.
* The tests don't actually work yet.

### Features

* It should access a DB to remember spice locations from one session to the next, for each user
* It should register and connect to the Raspberry Pi.
* The RPi should turn on the appropriate light


