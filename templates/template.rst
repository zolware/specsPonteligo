[Title]
=======

|

.. comments

:Author(s):
   Francois Roy, 
   Simon Clucas

:Date Created: 03-11-2017

:Language: C++

:Status: :red:`Draft`

-----------

Description
-----------

Here is a short description of the feature.

.. sidebar:: Sidebar Title

   dddd


Theory
------

A typical equation:

.. math:: T(\mathbf{x},0)=T_0(\mathbf{x}),\qquad \textrm{at }t=0.
   :label: eq:1

Where :math:`T_0` is the initial temperature.

.. math::
  \int_{x_1}^{x_2} \varphi_n(x)\varphi_m(x)dx = \left\{
  \begin{array}{rl}
  1 & \text{if } m = n,\\
  0 & \text{if } m\neq n.
  \end{array} \right.
  :label: eq:2

Equation :eq:`eq:1` and :eq:`eq:2` have been used in [Polyanin2001]_ to demonstrate...

.. note::
   This is a note.

A simple bokeh plot?

.. raw:: html

    <iframe src="_static/example.html" height="300px" width="350px"></iframe>


Sub-theory
~~~~~~~~~~

A basic table is presented in :numref:`table_label`.

.. _table_label:
.. csv-table:: :math:`\Lambda_i` for Different Homogeneous Boundary Type.
   :header: "Boundary Type", ":math:`k_1`", ":math:`k_2`", ":math:`s_1`", ":math:`s_2`", ":math:`\\Lambda_1,~x=x_1`", ":math:`\\Lambda_2,~x=x_2`"
   :widths: 15, 2, 2, 2, 2, 9, 9

   "Temperature, Dirichlet", 1, 1, 0, 0, ":math:`\frac{\partial}{\partial \xi}G(x,\xi,t-\tau)`", ":math:`-\frac{\partial}{\partial \xi}G(x,\xi,t-\tau)`"
   "Heat Flux, Neumann", 0, 0, 1, 1, ":math:`-G(x,\xi,t-\tau)`", ":math:`G(x,\xi,t-\tau)`"
   "Convection, Robin ", <0, >0, 1, 1, ":math:`-G(x,\xi,t-\tau)`", ":math:`G(x,\xi,t-\tau)`"
   "Mixed I", 1, 0, 0, 1, ":math:`\frac{\partial}{\partial \xi}G(x,\xi,t-\tau)`", ":math:`G(x,\xi,t-\tau)`"
   "Mixed II", 0, 1, 1, 0, ":math:`-G(x,\xi,t-\tau)`", ":math:`-\frac{\partial}{\partial \xi}G(x,\xi,t-\tau)`"



Third-Party Packages
--------------------

Invoke is a `Python <http://www.python.org/>`_ (2.6+ and 3.3+) task execution tool: `<http://www.pyinvoke.org/>`_

-- see `Deployment`_


Architecture
------------

A guide for understanding what things evolved from as a project ages and grow in scope -- see :numref:`my_figure`.

.. figure:: ../../figures/architecture.svg
    :name: my_figure
    :width: 600px
    :align: center
    :height: 450px
    :alt: alternate text
    :figclass: align-center
    
    Architecture


User Interface
--------------

.. code-block:: html
    :linenos:
    :name: my_block
    :caption: Block caption

    <h1>code block example</h1>

As refered in :numref:`my_block` 


or referencing manually :ref:`Code 1 <my_block>`.


other info can be downloaded :download:`template.py <../snippets/template.py>`

Deployment
----------

A simple way to do it is demonstrated in -- see :ref:`snippets.template module`

.. literalinclude:: ../snippets/template.py
    :linenos:
    :language: python
    :lines: 12, 14-18

Testing
-------

.. todo:: Something to do

Bullet lists:

- This is item 1 
- This is item 2

Enumerated lists:

3. This is the first item 
4. This is the second item  
#. This item is auto-enumerated

Definition lists: 

what 
  Definition lists associate a term with 
  a definition. 

-- see :ref:`tests.testTemplate module`

|longtext|

This text is :red:`colored red` and so is :red:`this`

References
----------

.. [Polyanin2001] `Andrei D. Polyanin, Handbook of Linear Partial Differential Equations for Engineers and Scientists, Chapman and Hall/CRC 2001 <http://goo.gl/jVjUFX>`_


.. Definitions

.. |longtext| replace:: This is a very very long text to include by substitution.
