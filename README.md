Example python / C++ project using boost::python and a custom ami to build
and deploy an egg on EC2-spark

1. create a python / c++ project with boost::python that installs sanely
2. use this to also build an egg with a basic egg template
3. Build the egg remotely
4. launch the spark instance and test if your custom function does its thing


Information about what's actually _in_ an egg

http://svn.python.org/projects/sandbox/trunk/setuptools/doc/formats.txt


Installation on osx with anaconda and a brew-based contemporary GCC

CXX=g++-4.9 cmake -DCMAKE_INSTALL_PREFIX=$HOME/anaconda -DBOOST_ROOT=/Users/jonas/anaconda/

Then to do the egg use -DCMAKE_BUILD_TYPE=EGG
make sure to do a make install
