from nose.tools import *
import pycppdeploy

def test_basic():
    assert_equal(pycppdeploy.pycpptest.helloworld(), "Hello World from C++")
