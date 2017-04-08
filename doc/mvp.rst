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
- A sign In/Sign Up interface (before authentication).
- A basic user profile interface.
- A method to stream the sensors' measurements from an external source.
- An interface to construct the Bayesian model.
- A page displaying the results (signal and prediction).
- An basic application database to save the models.
- An admin interface.

The web application will provide a GUI for the user (engineer) to construct state-space models by manually entering matrix elements in a dedicated web form. The user will also be able to get the data stream from a remote server (or just upload data), lauch/stop the application, visualize the results, and save/edit the model if desired.

Note that there will be no learning algorithm procedures in the MVP. The user view will only display the data (predicted, real) where the predicted value will be obtained from a simple linear Kalman filter/smoother.

The web application will be constructed using the `Django <https://www.djangoproject.com>`_ web framework and will include the two following applications:

1. A "users" application for authentication.
2. A "numerical" application to manipulate and visualize the data.

As a proof of concept, the web application will be hosted on `Heroku <https://www.heroku.com>`_, a popular Platform as a Service (PaaS) provider in the Python community. The database server and the static file server will be hosted on different servers. The static file server will be hosted on `Amazon S3 <https://aws.amazon.com/s3/?nc2=h_m1>`_.


Sensors Interface
-----------------

The user will have to generate time series (uniform timestep size) that can be used by the web application to simulate signals from sensors.

.. _sec_state_space:

Construction of the Bayesian model
----------------------------------

In order to construct the Bayesian model, multiple inputs must be provided by the user. Here is the exhaustive list of user inputs:

- :math:`N_x`: The number of *state variables*
- :math:`N_z`: The number of *sensor signals*
- :math:`N_u`: The number of *control inputs*
- :math:`\mathbf{x}_0`: The initial *state vector*, a :math:`N_x\times 1` vector.
- :math:`\mathbf{P}_0`: The initial *state covariance matrix*, a :math:`N_x\times N_x` matrix.
- :math:`\mathbf{z}`: The *measurement vector* (sensors' signals at time :math:`t`), a :math:`N_z\times 1` vector.
- :math:`\mathbf{R}`: The *measurement noise covariance matrix*, a :math:`N_z\times N_z` matrix.
- :math:`\mathbf{u}`: The *control input vector* (input signals at time :math:`t`), a :math:`N_u\times 1` vector.
- :math:`\mathbf{B}`: The *control function matrix*, a :math:`N_x\times N_u` matrix.
- :math:`\mathbf{F}`: The *transition function matrix*, a :math:`N_x\times N_x` matrix.
- :math:`\mathbf{Q}`: The *process noise covariance matrix*, a :math:`N_x\times N_x` matrix.
- :math:`\mathbf{H}`: The *measurement noise covariance matrix*, a :math:`N_z\times N_x` matrix. 

Note that the size of a matrix is defined by :math:`\#rows\times \#columns`.


API
---

A basic API (based on open source code) will be hosted on a `GitHub repository <https://github.com/zolware/zolware_API>`_ (eventually on PyPI). Our API will also be installed on the Heroku server using setuptools. The Python API will provide simple classes for manipulating the data and producing the results.

It is planned to use `Numpy <http://www.numpy.org>`_ and `Scipy <https://scipy.org>`_ as the building blocks for the numerical code. The package `filterpy <https://pypi.python.org/pypi/filterpy>`_ can also be used for the MVP (MIT license). 


Localization
------------

The web application will be available in French and in English.


Project Layout
--------------

The Django project layout will be implemented starting from the `Cookiecutter <https://github.com/pydanny/cookiecutter-django>`_ template.


The Django framework
--------------------

The django framework is based on a "MTV" approach – that is, "model", "template", and "view". Here the word *model* refers to database tables. In other words, the Django framework uses Oject Relational Mapping (ORM) to store data. 

For the MVP we consider two applications (*users*, *numerical*) with three basic models:

1- The *User* model, to store users details (username, passwords, etc).
2- The *Numerical* model to link the *User* model to the document database (e.g. `MongoDB <https://docs.mongodb.com>`_), and to store the Bayesian model parameters.
3- The *Sensor* model to link the *Numerical* model to the document database, and to store the sensors parameters  

The *User* model will be placed in the *user* application. The *Numerical* and *Sensor* models will be placed in the *numerical* application. Note that using the postgresql ORM it is possible to avoid the use of external tools such as MongoDB to store documents (e.g. JSON files). As a matter of fact, the postgresql ORM provide the *ArrayField* and the *JSONField* which are very convenient to store matrices and configuration files. These fields are available in the *django.contrib.postgres.fields* module.

The "users" application
-----------------------

The Django project will use `django-allauth <https://github.com/pennersr/django-allauth>`_ for authentication. The django-allauth package provide the basic models, views and templates needed for the MVP.


The "numerical" app
----------------------

The "numerical" application will save the user's inputs and sensors parameters and will provide access to the document database. The application will also provide tools to manipulate and visualize data through the python API.


Models (Database Tables)
########################

   
The *User* model will be imported from the "users" app. The *Numerical* model will contain the basic user inputs listed in :ref:`sec_state_space` entered in *ArrayFields* and the Bayesian model structure saved as a *JSONField* and saved on the static file server or linked to a document database (MongoDB). The *Numerical* model will contain a *CharField* named *owner* with a ForeignKey to the *User* model. The model will also contain a *CharField* named *sensor* with a ManyToManyField to the *Sensor* model. 

Validators will be defined in order to make sure the matrices are invertible and that the JSON file can be generated and overwrited when the model is updated (edited).

The *Sensor* model will store the sensor information as listed in :numref:`table1`.

.. csv-table::  The *Sensor* model.
    :name: table1
    :header: "Field", "Type", "Details"
    :widths: 5, 5, 5

     "name", "C", "unique=true"
     "is_sim", "B", ""
     "index", "I", "unique=true"
     "time_units", "C", "blank=true"
     "signal_name", "C", "blank=false"
     "signal_units", "C", "blank=true"
     "pubDate", "DT", "blank=true"
     "originator", "C", "blank=true"
     "filename", "JF", ""

where "C" is for *CharField*, B" is for *BooleanField*, "I" is for *IntegerField*, and "DT" is for *DateTimeField*. The *filename* field is a link to the document database countaining  the sensor measurements. Optionally it is possible to use a "JF" for *JSONField* to store the data as a JSON file on the static file server (Amazon S3). The *is_sim* atribute is true if the data are simulated, and the index attribute correponds to the length of the measurment array.


Views
#####

Figure :numref:`f_views` shows a schematics of the interaction between the web pages of the application. From the figure we can see that a minimum of 10 views will need to be created.

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

The base template will be based on the front-end framework `Twitter Bootstrap v4.0.0 - alpha 4  <http://v4-alpha.getbootstrap.com>`_. Figure :numref:`f_signIn` shows a basic Sign In page example, the "home" page for non-authenticated users, for the MVP. 

.. figure:: ../images/mvp_signIn.png
    :name: f_signIn
    :width: 600px
    :align: center
    :alt: alternate text
    :figclass: align-center
    
    The Sign In page using the Cookiecutter template.

Forms
#####

The Model Form will contain the user inputs defined in :ref:`sec_state_space`. Note that the size of the matrices could be ajusted be leaving zeros on the diagonal of the rows and columns to be removed. The package `django-crispy-forms <http://django-crispy-forms.readthedocs.io/en/latest/index.html>`_ seems to be an easy option for the MVP.


Deployment
----------

Follow the Heroku `instructions <https://devcenter.heroku.com/articles/deploying-python>`_. Eventually we will follow the best practices presented in :cite:`Roy2015`.

Note that an amazon AWS account (`S3 <https://aws.amazon.com/s3/?nc2=h_m1>`_) and a `mailgun <https://www.mailgun.com>`_ account should be created in order to use the web application in a *production* environment.


Testing
-------

The Python unit tests should be performed using the `pytest <https://docs.pytest.org/en/latest/>`_ package and inspired from the best practivces presented in the introductory book of :cite:`Parcival2014`.

The Javascrip unit test should be performed using the `Jasmine <https://jasmine.github.io>`_ package and the integration tests using the `Karma <https://karma-runner.github.io/1.0/index.html>`_ package.


Future improvments
------------------

- Add unknown parameters (parameters to be learned) to the models.
- Add different learning algorithms, for instance the Maximum Likelihood Estimate (MLE).
- Add different smoothing techniques.
- Add other variation of the Kalman filter (Extended, unscent, switching)
- Add other solving methods, e.g. UD filter, Square-root filter.
- Add a bayesian network visualization tool.
- Support for varying time-step size.
- Switch to Amazon EC2.


References
----------

.. bibliography:: _static/references.bib

