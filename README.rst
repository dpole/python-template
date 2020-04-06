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
* Build and publish the documentation

How to use
##########
1. Create your (empty) project on github:
   https://github.com/username_or_organization/new_project
2. Activate Travis-ci for your project. Follow this step of the 
   `tutorial <https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github>`_.
2. On your local machine, clone this template and push it to your new repo

.. code-block:: bash
    git clone --bare https://github.com/dpole/python-template.git
    cd python-template
    git push --mirror https://github.com/username_or_organization/new_project
    cd ..
    rm -rf python-template
