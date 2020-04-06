.. image:: https://travis-ci.com/dpole/python-template.svg?branch=master
    :target: https://travis-ci.com/dpole/python-template

***************
python-template
***************
Template repository for python packages
#######################################

Overview
########

Minimize thinking when setting up your new python project. This (minimal)
template project and folowing set of isntructions will allow you to have the
following within minutes

* Standard python packaging structure
* Make a git-clone of your package pip installable
* Test you package automatically with pytest on Travis-ci
* Build and publish the documentation on github.io

How to use
##########

1. Create your (empty) project on github:
   https://github.com/username_or_organization/new_project
2. Activate Travis-ci for your project. Follow this step of the 
   `tutorial <https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github>`_.
3. To allow the auto-deployment of the documentation to github pages,
   got to the setting of your repo on Travis and set a variable called
   ``GH_TOKEN`` with any value (if the repo is public, otherwise set it equal to
   an access token of your personal account)
3. On your local machine, clone this template and push it to your new repo

.. code-block:: bash

    git clone --bare https://github.com/dpole/python-template.git
    cd python-template
    git push --mirror https://github.com/username_or_organization/new_project
    cd ..
    rm -rf python-template

4. Edit your package

   a. edit this README. Remember to replace ``dpole/python-template`` with
      ``username_or_organization/new_project`` in the urls of the badges (see the
      ``image`` at the top of the file)
   b. edit very file in the ``docs/source`` folder and subfolders
