# AppImageUpdate Python bindings

![build status](https://travis-ci.org/TheAssassin/python-appimageupdate.svg?branch=master)

This library provides a Python wrapper for libappimageupdate.

It was written in C++ using
[boost::python](https://www.boost.org/doc/libs/1_66_0/libs/python/doc/html/),
and provides an elegant, Pythonic API which Python applications can use.

Please beware this is alpha quality software. There is a set of unit tests
that cover most of the functionality. If you find bugs, please do not hesitate
to open issues here on GitHub. If you think the issues are not in this wrapper
but right in libappimageupdate, though, please report the issues in the
[AppImageUpdate repository](https://github.com/AppImage/AppImageUpdate/issues).


## Build instructions

You will have to install libappimageupdate in order to build the C++
extension this library provides.

Please either install a distribution package, or use CMake and `make install`
to set it up. You should set CMake installation prefix to `/usr` for maximum
compatibility.

Then, install this module via pip right from GitHub. It will automatically
build the extension:

```
> pip install -e git+https://github.com/TheAssassin/python-appimageupdate.git#egg=appimageupdate
```
