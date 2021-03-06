#! /bin/bash

set -x
set -e

# use RAM disk if possible
if [ -d /dev/shm ]; then
    TEMP_BASE=/dev/shm
else
    TEMP_BASE=/tmp
fi

BUILD_DIR=$(mktemp -d -p "$TEMP_BASE" AppImageUpdate-build-XXXXXX)

cleanup () {
    if [ -d "$BUILD_DIR" ]; then
        rm -rf "$BUILD_DIR"
    fi
}

trap cleanup EXIT

# store repo root as variable
REPO_ROOT=$(readlink -f $(dirname $(dirname $0)))
OLD_CWD=$(readlink -f .)

pushd "$BUILD_DIR"

# installing boost::python from source is annoying
# therefore using a miniconda environment for testing
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3*-Linux-x86_64.sh -b -p conda-env/usr -f

. conda-env/usr/bin/activate
python --version

# build AppImageUpdate and install it into conda prefix
git clone --recursive https://github.com/AppImage/AppImageUpdate
pushd AppImageUpdate
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX="$CONDA_PREFIX"/ -DBUILD_QT_UI=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j$(nproc)
make install
popd

env | grep PREFIX

pushd "$REPO_ROOT"
python setup.py develop --prefix="$CONDA_PREFIX"/
pip install pytest
py.test tests/
popd
