from nose.tools import *
import pycppdeploy
from pycppdeploy import subdir

def test_basic():
    assert_equal(pycppdeploy.pycpptest.helloworld(), "Hello World from C++")
