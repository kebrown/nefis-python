===============================
NEFIS
===============================


.. image:: https://img.shields.io/pypi/v/nefis.svg
        :target: https://pypi.python.org/pypi/nefis

.. image:: https://img.shields.io/travis/openearth/nefis-python.svg
        :target: https://travis-ci.org/openearth/nefis-python

.. image:: https://readthedocs.org/projects/nefis/badge/?version=latest
        :target: https://nefis.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/openearth/nefis-python/shield.svg
     :target: https://pyup.io/repos/github/openearth/nefis-python/
     :alt: Updates


NEFIS is a library of functions designed for scientific programs. These programs are characterised by their large volume of input and output data. NEFIS is able to store and retrieve large volumes of data on file or in shared memory. To achieve a good performance when storing and retrieving data, the files are self-describing binary direct access files.

* Free software: Lesser GNU General Public License v3
* Documentation: https://oss.deltares.nl


Building
--------
We aim to provide the binaries for different platforms as wheel files at pypi. If you want to install nefis from source you can follow the following steps:

* Download the source code of Delft3D (includes the nefis library(*.so, *.dll) from https://oss.deltares.nl
* Edit the 'setup.cfg' file so that it can find the directory containing the nefis library (libnefis.so, nefis.dll). Adjust the next line(s) in the 'set.cfg' file.

.. code:: bash

    [build_ext]
    library-dirs=./lib

* Run `make dist` to create a whl file that you can install (using `pip install dist/nefis-x.x.x-cpxx-platform-architecture.whl` on similar platforms or `pip install -e .` to install from the local directory.

If you want to install the source code version (for developers) you can use pip install -e .

.. code:: bash

    pip install -e .


Testing
-------
The nefis library is available through the path-environment

Linux or OSX: Test use the command 'make test'.
Windows     : Test use the command 'py.test -v'


Running
-------
* Run nefis

.. code:: bash

    nefis
 
or (example) 

.. code:: bash

    nefis dump tests/data/trim-f34.def


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

# nefis-python
