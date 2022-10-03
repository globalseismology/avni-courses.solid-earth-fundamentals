Conda Environments Guide
=================

This course can be installed with various combinations of packages. We have tested the following
sets of packages. Please feel free to update these files or create new ones that work
for specific applications.
* `environment_base.yml` — Base version that was provided by Princeton research computing as the default GEO203 environment 
on Jupyter for Classes servers on Adroit. Excludes several modules necessary for the course.
* `environment_fall2022.yml` — The working version for the Fall 2022 semester. Includes cv2 through pip as a way to install it with conda
was not found.

Jupyter Notebooks
================

We can individually register each environment you want to show in your kernels list. If you have many environments this might be preferable because it allows you to register and un-register your environment kernels which could help keep that list tidy. ipykernel module is needed to see the
environment options listed on the right of Jupyter notebooks.
