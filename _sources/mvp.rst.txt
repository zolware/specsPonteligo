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
- A method to get the measurements from zolware.com.
- An interface to construct the state-space model.
- A page displaying the results (signal and prediction).
- An basic application database on a postgreSQL server.
- An admin interface.

The web application will provide a GUI for the engineer to construct a state-spaces model by entering the different matrix elements manually. The user will be able to get the data stream from zolware.com, lauch the application, visualize the results, and save/edit the model if desired. 

Note that there will be no hiden state and learning algorithm procedures in the MVP. The user view will only display the data (predicted, real) where the predicted value will be obtained from a simple linear Kalman filter.

The web application will be constructed using the Django web framework and will include two following applications:

1. A *users* app for authentication and registration.
2. A *modData* app to manipulate and visualize the data.


Measurement Interface
---------------------

The user will have to create an acount on zolware.com and generate a time series (uniform time steps) using two or three measurements.


Construction of the state-space model
-------------------------------------

The state-transition matrix :math:`A` and the state-to-measurement matrix :math:`H` can be defined by the user. For now only constants are allowed (including the constant timestep obtained from the simulated measurements).

We assume that the covariance matrix of the state-transition noise is diagonal (uncorelated system) and that the matrix elements, :math:`Q_{11}` and :math:`Q_{22}`, are the variances of random number obtained from a normal distribution of mean 0. A similarly assumption is made for the covariance matrix of the measurement noise :math:`R`.

We also assume that the initial state space vector is known, i.e. :math:`X_0`.

The user inputs for the model are:

1. The initial state-space vector :math:`X_0`.
2. The entries of the matrices :math:`\mathbf{A}` and :math:`\mathbf{H}`.
3. The diagonal components of the matrix :math:`\mathbf{Q}`.
4. The diagonal components of the matrix :math:`\mathbf{R}`.


API
---

The zolware package will be cloned from the GitHub repository and installed on the ponteligo server using setuptools. The Python API will provide simple classes for manipulating the data and producing the results.


Localization
------------

The web application must be in French and in English.


Project Directory Structure
---------------------------

A good template to begin with is `Cookiecutter <https://github.com/pydanny/cookiecutter-django>`_.


The *users* app
---------------

The Django project will use the django-allauth app. 


The *modData* app
-----------------

Models
######

The *User* model is imported from the *users* app.

.. csv-table:: The *KalmanModel* model.
   :header: "Field", "Type", "Details"
   :widths: 10, 5, 15

    "owner", "CharField", "ForeignKey(User, on_delete=CASCADE)"
    "measurements", "CharField", "ManyToManyField(Measurement)"
    "initial_states", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"
    "a_matrix", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"
    "b_matrix", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"
    "h_matrix", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"
    "r_matrix", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"
    "results", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"

The Project model will not be used in the MVP.

.. csv-table:: The *Project* model.
   :header: "Field", "Type", "Details"
   :widths: 10, 5, 15

    "company", "CharField", "unique=True"
    "location", "CharField", "blank=False"

The Measurement model is constructed from the data streamed by zolware.com

.. csv-table:: The *Measurement* model.
   :header: "Field", "Type", "Details"
   :widths: 10, 5, 15

    "name", "CharField", "unique=true"
    "project", "CharField", "ForeignKey(Project, on_delete=CASCADE)"
    "isSimulated", "BooleanField", ""
    "index", "IntegerField", "unique=true"
    "xname", "CharField", "blank=false"
    "xunit", "CharField", "blank=true"
    "yname", "CharField", "blank=false"
    "yunit", "CharField", "blank=true, validator for unit format"
    "sensorType", "CharField", "blank=true"
    "sensorLabel", "CharField", "blank=true"
    "sensorLocation", "CharField", "blank=true"
    "pubDate", "DateTimeField", "blank=true"
    "originator", "CharField", "blank=true"
    "reference", "CharField", "blank=true"
    "details", "CharField", "blank=true"
    "filename", "FileField", "upload_to=generate_filename, storage=OverwriteStorage()"

.. todo::
   Define the fields. Index is position of the last measurement (the length) of the series.


Views
#####

.. figure:: ../images/mvp_views.svg
    :name: f_views
    :width: 600px
    :align: center
    :height: 450px
    :alt: alternate text
    :figclass: align-center
    
    Schematics of the link between the views of the application. The red links shows are only available before the user registers and the blue links when the user is registered.

Templates
#########

Forms
#####

Deployment
----------

Follow best practices presented in [Roy2015]_. 


Testing
-------

TBD

.. Future improvments
.. ------------------

.. - Add unknown parameters (parameters to be learned) to the models.
.. - Add different learning algorithms, for instance the Maximum Likelihood Estimate (MLE).
.. - Add different smoothing techniques.
.. - Add other variation of the Kalman filter (Extended, unscent, switching)
.. - Add other solving methods, e.g. UD filter, Square-root filter.
.. - Add a bayesian network visualization tool.
.. - Support for varying time-step size.
.. - Switch to Amazon EC2?

References
----------

.. [Roy2015] `Daniel and Audrey Roy, Two Scoops of Django: Best Practices for Django 1.8, third edition. Two scoops press, 2015 <https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342>`_
