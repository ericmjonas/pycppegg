#include <unistd.h>

#include <boost/python.hpp>
#include <boost/python/class.hpp>
#include <boost/utility.hpp>
#include "cpptest.h"
namespace bp=boost::python; 


BOOST_PYTHON_MODULE(pycpptest)
{
  using namespace boost::python;
 
  def("helloworld", &helloworld); 
  
}

