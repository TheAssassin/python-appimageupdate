import os
import sys

from setuptools import setup, Extension

if sys.version_info[0] != 3:
    print("Sorry, this library is only available for Python 3")
    exit(1)

setup(
    name="appimageupdate",
    version="0.0.1",
    description="Python to libappimageupdate bridge.",
    tests_require=["pytest"],
    requires=["cffi"],
    packages=["appimageupdate"],
)
