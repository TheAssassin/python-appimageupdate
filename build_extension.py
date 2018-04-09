import cffi
import os


ffi = cffi.FFI()

cur_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(cur_dir, "appimageupdate")


with open(os.path.join(src_dir, "_wrapper.h")) as f:
    ffi.cdef(f.read())


with open(os.path.join(src_dir, "_wrapper.cpp")) as f:
    ffi.set_source(
        "_appimageupdate",
        f.read(),
        source_extension='.cpp',
        libraries=["appimageupdate"],
        extra_compile_args=["-std=c++11"]
    )


if __name__ == "__main__":
    ffi.compile()
