.. image:: https://img.shields.io/badge/Author-Francisco%20Bustamante-red.svg
    :alt: Francisco Bustamante
    :target: https://www.linkedin.com/in/flsbustamante
.. image:: https://img.shields.io/badge/Python-3.8+-blue.svg
    :alt: Python
    :target: https://www.python.org/
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
    :alt: LICENSE
    :target: LICENSE.txt
.. image:: https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat
    :alt: Contributions are welcome
    :target: https://github.com/chicolucio/pH-diagrams/issues
.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/
.. image:: https://readthedocs.org/projects/ph-diagrams/badge/?version=latest
    :target: https://ph-diagrams.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/pypi/v/pH-diagrams.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/pH-diagrams/

===========
pH diagrams
===========

    A Python package to plot fractional composition diagrams and pH-log c diagrams

.. image:: https://github.com/chicolucio/pH-diagrams/blob/master/images/animation.gif?raw=true
    :alt: header animation
    :align: center

|

Interactive web app:

.. image:: https://img.shields.io/badge/-Streamlit%20app-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
    :alt: Streamlit app
    :align: center
    :target: https://phdiagrams.herokuapp.com/

Installation
============

::

   pip install pH-diagrams

Usage
=====

The class ``Acid`` must be imported from ``ph_diagrams``. To create diagrams for the
acetic acid::

   >>> from ph_diagrams import Acid
   >>> import matplotlib.pyplot as plt
   >>> fig, axs = plt.subplots(nrows=1, ncols=2)
   >>> acetic_acid = Acid(pKa=(4.76,), acid_concentration=0.1)
   >>> acetic_acid.plot(plot_type='distribution', backend='matplotlib',
                        title='Acetic acid - Distribution diagram',
                        ax=axs[0], legend=False)
   >>> acetic_acid.plot(plot_type='pC', backend='matplotlib',
                        title='Acetic acid - pH-log c diagram', ax=axs[1])
   >>> plt.show()

As can be seen, the parameter ``pKa`` must be a tuple even if there is only one value.
The above example generates the following plot, with both diagrams side by side:

.. image:: https://github.com/chicolucio/pH-diagrams/blob/master/images/acetic_acid.png?raw=true
    :alt: acetic acid example
    :align: center

The plots above were made with Matplotlib_, the default backend.

Changing the ``backend`` parameter to ``plotly``, and removing the ``ax`` parameter
(it works only with Matplotlib), will open a browser window for each plot.
Since Plotly_ is interactive, the user can zoom, pan, and see values on hover.

Full documentation is hosted on `Read the Docs`_.

A live interactive version of this project can be seen clicking in the following badge:

.. image:: https://img.shields.io/badge/-Streamlit%20app-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
    :alt: Streamlit app
    :align: center
    :target: https://phdiagrams.herokuapp.com/

The web app was made with Streamlit_ and hosted on Heroku_.

A brief explanation on the chemical theory behind each diagram can be seen
`here <https://phdiagrams.herokuapp.com/How_to_use_and_theory>`_.

Local Streamlit app and Jupyter notebooks
-----------------------------------------

This repo has Jupyter Notebooks and scripts for a fully functional
Streamlit_ app. First, create a virtual environment, clone the repo and
install dependencies::

    python -m venv .venv
    source .venv/bin/activate
    git clone git@github.com:chicolucio/pH-diagrams.git
    cd pH-diagrams
    pip install -r requirements.txt

This considers that you have `Jupyter Notebook`_ installed. If not, install it with
``pip install notebook``.

For more basic usage examples, see the ``tutorial.ipynb`` notebook on ``notebooks`` folder.
In the same folder, the ``tutorial_interactive_ipywidgets.ipynb`` file shows how to
use ipywidgets_ to create interactive diagrams. Just run ``jupyter notebook`` on a
terminal from the repo root folder and select the files.

A local version of the Streamlit_ app can be used running, from the repo root folder,
``streamlit run Home.py`` on a terminal. A browser window will open (if not, follow
the instructions shown on the terminal output).

Contributing
============

All contributions are welcome.

**Issues**

Feel free to submit issues regarding:

- recommendations
- more examples for the tutorial
- enhancement requests and new useful features
- code bugs

**Pull requests**

- before starting to work on your pull request, please submit an issue first
- fork the repo
- clone the project to your own machine
- commit changes to your own branch
- push your work back up to your fork
- submit a pull request so that your changes can be reviewed

For full contribution guidelines and details check out our `contributing guide`_.



Citing
======

If you use this project in a scientific publication or in classes, please consider citing as

   F. L. S. Bustamante & H. B. Soares & N. O. Souza, pH diagrams, 2021.
   Available at: https://github.com/chicolucio/pH-diagrams

.. _Matplotlib: https://matplotlib.org
.. _Streamlit: https://streamlit.io
.. _Heroku: https://www.heroku.com
.. _Plotly: https://plotly.com/python/
.. _contributing guide: CONTRIBUTING.rst
.. _Read the Docs: https://ph-diagrams.readthedocs.io/en/latest/?badge=latest
.. _ipywidgets: https://ipywidgets.readthedocs.io/en/stable/
.. _Jupyter Notebook: https://jupyter.org/
