=============================
kpfm
=============================

.. image:: https://travis-ci.org/marohngroup/kpfm.svg?branch=master
    :target: https://travis-ci.org/marohngroup/kpfm

.. image:: http://readthedocs.org/projects/kpfm/badge/?version=latest
    :target: http://kpfm.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/86489214.svg
   :target: https://zenodo.org/badge/latestdoi/86489214

Kelvin Probe Force Microscopy (KPFM) data analysis.


Motiviation
-----------

Collect useful code for custom Kelvin probe force microscopy experiments into a single repository.
The motivation for using a single repository is prior experience and `this article <http://danluu.com/monorepo/>`_.

Structure
---------

A tentative structure for the repository is

.. code-block:: none

    kpfm
    ├── __init__.py
    ├── _version.py
    ├── experiment
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   └── test_kpfm.py
    ├── scratch
    │   ├── __init__.py
    │   └── temporary_code.py
    └── util
        ├── __init__.py
        └── plot.py

Each experiment is contained in its own module.
The ``util`` module collects useful functions and decorators that are useful across a range of modules.
Tests are placed in the ``tests`` module.
Scratch contains a place for code that will not be maintained.
If a particular experiment or procedure is useful over a longer period,
it can be moved to its own experiment module.

Development life cycle of new code
----------------------------------

1. Workup data and write provisional code in an IPython notebook
2. If many data files are going to be processed in this way, move the routine to a new module in ``scratch``.
     - Workups in ``scratch`` come with no guarantees that they will not break.
     - In practice, it would be useful to create a new copy of the temporary code if there is likely to be significant breakage.
3. If the experiment is useful enough, copy / edit the scratch code and move it to its own experiment folder. In doing so, we commit to leave the experiment in a usable, backward compatible state, which means consistent LabView code for collecting the data, as well as consistent, backward-compatible routines for working up the data.

The idea would be that with a powerful set of utility, signal processing, and data analysis tools in the ``kpfm`` package, many analyses could be performed quickly at (1) or (2).
Even having a file in scratch (perhaps copied occasionally as the data analysis or LabView code changes significantly) is a significant improvement over code copied between IPython notebooks.
The other consideration is that it is a large investment of time to maintain code, so that code related to a "one-off" experiment should be saved, but not maintained.

Features
--------

* TODO

