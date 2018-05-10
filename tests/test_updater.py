import os
import pytest
import shutil
import time

from appimageupdate import Updater, UpdaterState, AppImageUpdateError


@pytest.fixture
def data_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))


@pytest.fixture
def echo_path(data_dir):
    return os.path.abspath(os.path.join(data_dir, "Echo-x86_64.AppImage"))


@pytest.fixture
def appimaged_path(data_dir):
    return os.path.abspath(os.path.join(data_dir, "appimaged-i686.AppImage"))


def test_init_echo(echo_path):
    # try to instantiate Updater
    Updater(echo_path)


def test_describe_echo(echo_path):
    u = Updater(echo_path)

    description = u.describe_appimage()

    assert "AppImage type: 2" in description
    assert "Raw update information: <empty>" in description
    assert "Update information type: Invalid" in description


def test_init_appimaged(appimaged_path):
    # try to instantiate Updater
    Updater(appimaged_path)


def test_describe_appimaged(appimaged_path):
    u = Updater(appimaged_path)

    description = u.describe_appimage()

    assert "AppImage type: 2" in description
    assert "Raw update information: gh-releases-zsync|AppImage|AppImageKit|continuous|appimaged-x86_64.AppImage.zsync" in description
    assert "Update information type: ZSync via GitHub Releases" in description


def test_update_check_appimaged(appimaged_path):
    u = Updater(appimaged_path)

    updateAvailable = u.check_for_changes()

    # the appimaged AppImage is horribly out of date, so libappimageupdate
    # should report there's an update available
    assert updateAvailable


def test_update_appimaged(appimaged_path, tmpdir):
    test_dir = tmpdir.mkdir("test_update_appimaged")

    # need to copy appimaged to another directory
    # as libappimageupdate will update the file in-place (i.e., create a file
    # next to the original file), we need to copy appimaged to the temporary
    # directory and update it there
    new_appimaged_path = test_dir.join("appimaged.AppImage")
    shutil.copyfile(appimaged_path, new_appimaged_path)

    u = Updater(str(new_appimaged_path))
    u.start()

    while not u.is_done():
        time.sleep(1)

    assert not u.has_error()
    assert u.state() == UpdaterState.SUCCESS

    path_to_new_file = u.path_to_new_file()
    assert path_to_new_file == os.path.join(test_dir, "appimaged-x86_64.AppImage")


def test_update_echo(echo_path):
    u = Updater(str(echo_path))
    u.start()

    while not u.is_done():
        time.sleep(1)

    assert u.has_error()
    assert u.state() == UpdaterState.ERROR


# TODO: deactivated until stop() works
#def test_update_appimaged_stop(appimaged_path):
#    u = Updater(appimaged_path)
#    u.start()
#    u.stop()


# TODO: deactivated until stop() works
#def test_update_echo_stop(echo_path):
#    u = Updater(echo_path)
#    u.start()
#
#    # TODO: when stop()ing too early, the C++ backend crashes
#    # this needs to be debugged upstream in libappimage
#    time.sleep(1)
#
#    with pytest.raises(RuntimeError):
#        u.stop()


# TODO: this throws std::bad_alloc -- must be an upstream bug in
# libappimageupdate that needs to be fixed ASAP
#def test_update_echo_progress(echo_path):
#    u = Updater(echo_path)
#    assert u.progress() == 0


def test_path_to_new_file(echo_path):
    u = Updater(echo_path)

    with pytest.raises(AppImageUpdateError):
        u.path_to_new_file()


def test_update_appimaged_progress(appimaged_path, tmpdir):
    test_dir = tmpdir.mkdir("test_update_appimaged")

    # need to copy appimaged to another directory
    # as libappimageupdate will update the file in-place (i.e., create a file
    # next to the original file), we need to copy appimaged to the temporary
    # directory and update it there
    new_appimaged_path = test_dir.join("appimaged.AppImage")
    shutil.copyfile(appimaged_path, new_appimaged_path)

    u = Updater(str(new_appimaged_path))

    u.start()

    while not u.is_done():
        assert u.progress() >= 0
        time.sleep(1)
        assert u.progress() <= 1

    assert u.progress() == 1
