# Time Series

Predictions based on past time lines

**Contents**
- [Time Series](#time-series)
  - [Background - Everyone Wants to Know](#background---everyone-wants-to-know)
    - [An Introduction to Time Series Forecasting](#an-introduction-to-time-series-forecasting)
    - [Preprocessing](#preprocessing)
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

### An Introduction to Time Series Forecasting

A **time series** of data is an ordered set of data that measures one thing as it changes over time.
* In effect, it is a series of numbers, each with a timestamp associated with it. It has a name and labelled dimensions.

Main takeaway:

* each new datum is given a timestamp and a new entry
* data arrives in time order
* time is the axis upon which all data will be aligned (primary axis)

Essentially, you spam `append` on the array to edit it.

**Foercasting** is predicting the future based on the past.

To train in forecasting, we'll need a dataset of past values, and we'll take a fraction of it for use in training. The remainder can be used in testing. This way, the model can be evaluated using data it has yet to see, but that has known correct values.
* the `scikit-learn` (which replaced the `sklearn`) Python library has training and evaluating tools

There are various methods for prediction. From the simplest "assume it will always be equal to the most recent value" to more nuanced weighted moving averages that look at recent values and predict based on their averages.

**Trends** are general patterns observed over a time period. Holt's Linear Method is a way of training for this.

**Seasonality** are similarly general patterns, but more like noticing when there are tendencies to go up and down.

**Holt's Winter Method** smooths both of these alongisde consideration with the average in order to create a prediction significantly more accurate than simpler methods.
* This is specialized for single-variable (univariate) data, data that depends on a single variable for a single outcome. Reality generally has many varaibles at play, however.

For multivariate data, **Vector Auto Regression** model  can create a general calculation.

Ideally, a learning model such as an LSTM RNN is used.

### Preprocessing

There are a number of preprocessing techniques to make data as usable as possible; here are some, and where/when they are used.

**Normalization**: Just about all learning models will include this step as a precaution. Normalization in this context refers to compressing all numeric "input/output" values to between 0 and 1 (`[0,1)`) so that there is minimal chance it is incompatible with anything used in training.

**Data Splitting** is particularly important for Time Series. In order to evaluate the forecast, we'll have to test it on data it has never seen before, but that *we* have. Data Splitting refers to dividing our historical data into "training" and "test" data. This is because we can't just make up or pull new data for testing. Everything will come from the past, and we don't want the model to see the test before it takes the test.

**Imputation Techniques** can be specially implemented for datasets with missing values.

### Resources Consulted

* [Time Series Prediction](https://www.youtube.com/watch?v=d4Sn6ny_5LI)
* [Preprocessing of Time Series Data](https://medium.com/enjoy-algorithm/pre-processing-of-time-series-data-c50f8a3e7a98)
