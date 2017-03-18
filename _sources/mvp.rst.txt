======================
Minimum Viable Product
======================

|

.. comments

:Author(s):
   Francois Roy

:Date Created: 03-14-2017

:Language: None

:Status: :red:`Draft`

-----------

Description
-----------

The proof of concept would be a simple web application with the following components:

- A home page containing a list of saved models (database).
- A sign In/Sign Up interface (bfore authentiacation).
- A basic user profile interface.
- An interface to get the signals source.
- A model constructor Interface.
- A user view displaying the results (signal and prediction).
- An basic application database on a postgreSQL server.
- An admin interface.

The web application will provide a GUI for the engineer to construct a two-state-spaces model, get a data stream composed of two uncorelated time series, lauch the application to observe the results in the user view and save the model if desired. Note that there will be no hiden state and learning algorithm procedures in the MVP. The user view will only display the data (predicted, real) where the predicted value will be obtained from a simple linear Kalman filter. Only one solver option would be available, i.e. the LU method.


Measurement Interface
---------------------

The application will get the two uncorelated time series (uniform time steps) using the zolware data service available at zolware.com.


Construction of the model
-------------------------

The state-transition matrix :math:`A` and the state-to-measurement matrix :math:`H` can be defined by the user. For now only constants  are allowed (including the constant timestep size).

We assume that the covariance noise matrix of the state-transition is diagonal (uncorelated system) and that the diagonal matrix elements, :math:`Q_{11}` and :math:`Q_{22}`, the variances of random number obtained from a normal distribution of mean 0.

We also assume that the initial state space vector is known, i.e. :math:`X_0`.

The user inputs for the model are:

1. The initial state-space vector :math:`X_0`.
2. The four entries of the matrices :math:`A` and :math:`H`.
3. The diagonal components of the matrix :math:`Q`.
4. The standard deviation of the covariance noise matrix :math:`R_{11}`, and :math:`R_{22}`. The matrix is diagonal for uncorelated signals. We assume that the matrix elements are the variance of the random numbers obtained from a normal distribution of mean 0.

Note that the covariance matrix of the measurement noise :math:`R` is diagonal for uncorelated signals. The data format will consist of a :math:`N`-by-3 matrix where the first column will represent the time, and the second and third the data obtained by the signal emulator.


API
---

The zolware package will be cloned from the GitHub repository and installed on the ponteligo server using setuptools. The Python API will provide simple classes for the application.


Localization
------------

The web application must be in French and in English.


Architecture
------------

A good template to begin with is `Cookiecutter <https://github.com/pydanny/cookiecutter-django>`_.

.. todo::
   Diagram using graphviz.


Models
------

Views
-----

.. figure:: ../images/mvp_architecture.svg
    :name: f_architecture
    :width: 600px
    :align: center
    :height: 450px
    :alt: alternate text
    :figclass: align-center
    
    Schematics of the link between the components (views) of the application.


Forms
-----

Deployment
----------

Follow best practices presented in [Roy2015]_. 


Testing
-------

Compare with the estimation velocity from position example presented in [Phil2010]_

Future improvments
------------------

- Add more information on the sensors: type, location, units...
- Add unknown parameters (parameters to be learned) to the models.
- Add different learning algorithms, for instance the Maximum Likelihood Estimate (MLE).
- Add different smoothing techniques.
- Add other variation of the Kalman filter (Extended, unscent, switching)
- Add other solving methods, e.g. UD filter, Square-root filter.
- Add a bayesian network visualization tool.
- Support for varying time-step size.
- Switch to Amazon EC2?

References
----------

.. [Roy2015] `Daniel and Audrey Roy, Two Scoops of Django: Best Practices for Django 1.8, third edition. Two scoops press, 2015 <https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342>`_

.. [Phil2010] `Phil Kim, Kalman Filter for Beginners with MATLAB Examples. A-JIN Publishing Company, 2010. <https://www.amazon.com/Kalman-Filter-Beginners-MATLAB-Examples/dp/1463648359>`_
