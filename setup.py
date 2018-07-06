import sys

from distutils.command.build import build
from setuptools import setup
from setuptools.command.install import install



if sys.version_info[0] != 3:
    print("Sorry, this library is only available for Python 3")
    exit(1)


def get_ext_modules():
    import build_extension
    return [build_extension.ffi.distutils_extension()]


class CFFIBuild(build):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        build.finalize_options(self)


class CFFIInstall(install):
    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        install.finalize_options(self)


setup(
    name="appimageupdate",
    version="0.0.1",
    description="Python to libappimageupdate bridge.",
    tests_require=["pytest"],
    install_requires=["cffi"],
    setup_requires=["cffi"],
    packages=["appimageupdate"],
    cmdclass={
        "build": CFFIBuild,
        "install": CFFIInstall,
    },
    zip_safe=False
)
