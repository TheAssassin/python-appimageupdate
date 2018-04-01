from setuptools import setup, Extension

appimageupdate_module = Extension(
    "_appimageupdate",
    sources=["appimageupdate/_appimageupdate.cpp"],
    libraries=["appimageupdate", "boost_python-py35"],
    include_dirs=["/usr/include", "/usr/local/include"],
    library_dirs=["/usr/lib", "/usr/lib/x86_64", "/usr/local/lib", "/usr/local/lib/x86_64"],
)

setup(
    name="appimageupdate",
    version="0.0.1",
    description="Python to libappimageupdate bridge.",
    ext_modules=[appimageupdate_module],
    tests_require=["pytest"],
)
