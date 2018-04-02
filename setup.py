import os
import sys

from setuptools import setup, Extension

if sys.version_info[0] != 3:
    print("Sorry, this library is only available for Python 3")
    exit(1)


prefix = "/usr"
boost_lib = "boost_python-py35"

if "CONDA_PREFIX" in os.environ:
    prefix = os.environ["CONDA_PREFIX"]
    boost_lib = "boost_python3"
    print("Conda environment detected, using {} as prefix".format(prefix))


appimageupdate_module = Extension(
    "_appimageupdate",
    sources=[
        os.path.abspath(os.path.join(os.path.dirname(__file__), "appimageupdate/_appimageupdate.cpp")),
    ],
    libraries=[
        "appimageupdate",
        boost_lib
    ],
    include_dirs=[
        os.path.join(prefix, "include"),
        os.path.join(prefix, "local/include"),
    ],
    library_dirs=[
        os.path.join(prefix, "lib"),
        os.path.join(prefix, "lib/x86_64"),
        os.path.join(prefix, "local/lib"),
        os.path.join(prefix, "local/lib/x86_64"),
    ],
)

setup(
    name="appimageupdate",
    version="0.0.1",
    description="Python to libappimageupdate bridge.",
    ext_modules=[appimageupdate_module],
    tests_require=["pytest"],
    packages=["appimageupdate"],
)
