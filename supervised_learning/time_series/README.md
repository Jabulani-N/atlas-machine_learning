# Time Series

Predictions based on past time lines

**Contents**
- [Time Series](#time-series)
  - [Background - Everyone Wants to Know](#background---everyone-wants-to-know)
    - [An Introduction to Time Series](#an-introduction-to-time-series)
    - [Resources Consulted](#resources-consulted)

<details>
    <summary>Project Instructions</summary>

Allowed editors: `vi`, `vim`, `emacs`

All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (`version 3.9`)

Your files will be executed with `numpy` (version 1.25.2), `tensorflow` (version 2.15) and `pandas` (version 2.2.2)

All your files should end with a new line

The first line of all your files should be exactly `#!/usr/bin/env python3`

All of your files must be executable

A `README.md` file, at the root of the folder of the project, is mandatory

Your code should follow the `pycodestyle style` (version 2.11.1)

All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)

All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)

All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)


</details>

## Background - Everyone Wants to Know

### An Introduction to Time Series

A time series of data is an ordered set of data that measures one thing as it changes over time.
* In effect, it is a series of numbers, each with a timestamp associated with it. It has a name and labelled dimensions.

Main takeaway:

* each new datum is given a timestamp and a new entry
* data arrives in time order
* time is the axis upon which all data will be aligned (primary axis)

Essentially, you spam `append` on the array to edit it.

### Resources Consulted

* [Time Series Prediction](https://www.youtube.com/watch?v=d4Sn6ny_5LI)
