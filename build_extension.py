import cffi
import os


ffi = cffi.FFI()

cur_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(cur_dir, "appimageupdate")


with open(os.path.join(src_dir, "_wrapper.h")) as f:
    ffi.cdef(f.read())


extra_compile_args = []

if "CONDA_PREFIX" in os.environ:
    include_dir = os.path.join(os.environ["CONDA_PREFIX"], "include")
    extra_compile_args.append("-I{}".format(include_dir))

if "INCLUDE_DIRS" in os.environ:
    extra_compile_args += ["-I{}".format(i) for i in os.environ["INCLUDE_DIRS"].split(":")]


with open(os.path.join(src_dir, "_wrapper.cpp")) as f:
    ffi.set_source(
        "_appimageupdate",
        f.read(),
        source_extension='.cpp',
        libraries=["appimageupdate"],
        extra_compile_args=["-std=c++11"] + extra_compile_args,
    )


if __name__ == "__main__":
    ffi.compile(verbose=True, debug=True)
