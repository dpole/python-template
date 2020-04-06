.. image:: https://travis-ci.com/dpole/python-template.svg?branch=master
    :target: https://travis-ci.com/dpole/python-template

.. image:: https://img.shields.io/badge/docs-dev-blue.svg
    :target: https://dpole.github.io/python-template/index.html

***************************************
Template repository for python packages
***************************************

Overview
########

Minimize thinking when setting up your new python project. This (minimal)
template project and the following set of instructions will allow you to get

* Standard python packaging structure
* Make a git-clone of your package pip installable
* Test your package automatically with pytest on Travis-ci
* Build and publish the documentation on github.io

How to use
##########

1. Create your (empty) project on github:
   https://github.com/username_or_organization/new_project
2. Activate Travis-ci for your project. Follow this step of the 
   `tutorial <https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github>`_.
3. To allow the auto-deployment of the documentation to github pages

   a. On github, in your repo settings, in the GitHub Pages section, set the
      ``gh-pages branch`` as the source
   b. On github, in your account setting, in the developer settings, generate a
      new personal access token (e.g., note ``Travis-sphinx``, scope ``repo``)
   c. On Travis, in your repo settings, set a variable called ``GH_TOKEN`` with
      value equal to the token you just created

4. On your local machine, clone this template and push it to your new repo

   .. code-block:: bash

       git clone --bare https://github.com/dpole/python-template.git
       cd python-template
       git push --mirror https://github.com/username_or_organization/new_project
       cd ..
       rm -rf python-template

5. Edit your package

   a. Edit this README. Remember to replace ``dpole`` with
      ``username_or_organization`` and ``python-template`` with
      ``new_project`` in the urls of the badges (see the ``image`` at the top
      of the file).
   b. Rename the ``package_name`` folder with the name of your package,
      edit and/or rename the files in it (don't forget ``__init__.py``).
   d. Edit the ``setup.py`` file. Don't forget to add the dependencies of your
      package in the ``isntall_requires`` list.
   e. Edit every file in the ``docs/source`` folder and subfolders. 
   f. Write doctrings using the
      `numpy sphinx syntax <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html>`_
