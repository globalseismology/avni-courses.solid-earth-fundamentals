Conda Environments Guide
=================

AVNI can be installed with various combinations of packages. We have tested the following
sets of packages. Please feel free to update these files or create new ones that work
for specific applications.
* `environment.yml` — Base version that all public CIG users should use. Excludes modules
for documentation and applets.
* `environment_doc.yml` — The version for creating documentation and testing through
Travis CI includes doc modules such as sphinx but exclude applets.
* `environment_devel.yml` — The version that all core developers and maintainers should use. Most comprehensive and up to date.
* `environment_atlas3d.yml` — The version for model assimilation on tiger/tigressdata
* `environment_maps.yml` - Version for making maps with cartopy, pygmt and other plotting tools

Jupyter Notebooks
================

We can individually register each environment you want to show in your kernels list. If you have many environments this might be preferable because it allows you to register and un-register your environment kernels which could help keep that list tidy.

In your new environment install ipykernel

`(new-env)$ conda install ipykernel`

2. Register the kernel spec with Jupyter using the following command. The `--name=` argument will set the name you see in Jupyter Notebooks for this environment’s kernel (so you can call it whatever you want but using the environment’s name might be wise).

`(new-env)$ipython kernel install --user --name=new-env`

3. Now new-env will be displayed in your list of kernels (no need to restart Jupyter Notebook — just reload the page in your browser).

4. When you want to un-register that kernel spec (remove the environment’s kernel from the list of available kernels) use the following command:

`$jupyter kernelspec uninstall new-env`
