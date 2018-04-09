import build_extension
import sys

from setuptools import setup

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
    ext_modules=[
        build_extension.ffi.distutils_extension(),
    ],
    zip_safe=False
)
