Documentation for the ifupdownaddons package helper modules
***********************************************************

This package contains modules that provide helper methods
for ifupdown2 addon modules to interact directly with tools
like iproute2, brctl etc.


bridgeutils
===========

Helper module to work with bridgeutil commands

.. automodule:: bridgeutils

.. autoclass:: brctl

<<<<<<< HEAD
ifenslaveutil
=============
=======
bondutil
========
>>>>>>> cumulus/dev

Helper module to interact with linux api to create bonds.
Currently this is via sysfs.

<<<<<<< HEAD
.. automodule:: ifenslaveutil

.. autoclass:: ifenslaveutil
=======
.. automodule:: bondutil

.. autoclass:: bondutil
>>>>>>> cumulus/dev

dhclient
========

Helper module to interact with dhclient tools.

.. automodule:: dhclient

.. autoclass:: dhclient

iproute2
========

Helper module to interact with iproute2 tools.

.. automodule:: iproute2

.. autoclass:: iproute2
