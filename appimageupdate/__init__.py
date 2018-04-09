import enum

from _appimageupdate import ffi, lib


class AppImageUpdateError(Exception):
    pass


class UpdaterState(enum.IntEnum):
    # TODO: keep this in sync!

    INITIALIZED = 0
    RUNNING = 1
    STOPPING = 2
    SUCCESS = 3
    ERROR = 4


class Updater:
    """
    Updates AppImages.
    """

    def __init__(self, path_to_appimage):
        buffer = ffi.new("char[]", path_to_appimage.encode())
        self._updater = lib.Updater__create(buffer)

    def check_for_changes(self, method=0):
        """
        Check whether an update is available.

        This can only be done before the update process is started.

        See AppImageUpdate's documentation for the meaning of method.

        :param int method: method to use
        :return: True if an update is available, False otherwise
        :rtype: bool
        """

        rv = lib.Updater__checkForChanges(self._updater, method)

        if rv < 0:
            raise AppImageUpdateError("Updater__checkForChanges")

        return rv

    def start(self):
        """
        Start the update process in the background.

        Use isDone() to check whether the update has finished.

        You can stop the update process with stop().

        Raises AppImageUpdateError if the update has been started already.

        :raises: AppImageUpdateError
        """

        rv = lib.Updater__start(self._updater)

        if not rv:
            raise AppImageUpdateError("Updater__start")

    def describe_appimage(self):
        """
        Describe the AppImage in a standard format. Useful for debugging.

        :return: String containing information about the AppImage
        :rtype: str
        :raises: AppImageUpdateError
        """

        ptr = lib.Updater__describeAppImage(self._updater)

        if ptr == ffi.NULL:
            raise AppImageUpdateError("Updater__describeAppImage")

        rv = ffi.string(ptr).decode()

        lib.free(ptr)

        return rv

    def path_to_new_file(self):
        """
        Return path to updated AppImage.

        :return: String containing information about the AppImage
        :rtype: str
        :raises: AppImageUpdateError
        """

        ptr = lib.Updater__pathToNewFile(self._updater)

        if ptr == ffi.NULL:
            raise AppImageUpdateError("Updater__pathToNewFile")

        rv = ffi.string(ptr).decode()

        lib.free(ptr)

        return rv

    def is_done(self):
        """
        Check whether the running update process has finished.

        Internally tests whether state() reports a final state.

        You should check this in a loop, and e.g., sleep between the calls.

        :return: True if the process is done, False otherwise
        :rtype: bool
        """

        return lib.Updater__isDone(self._updater)

    def has_error(self):
        """
        Checks whether the update failed.

        This checks whether the state() is set to an error value.

        :return: True if an error has occured, False otherwise
        """

        return lib.Updater__hasError(self._updater)

    def state(self):
        """
        Returns the state of the updater.

        :return: state of the updater
        :rtype: UpdaterState
        """

        state = lib.Updater__state(self._updater)
        return UpdaterState(state)

    def stop(self):
        """
        Stop the update process

        Please beware this feature has most likely not been implemented in
        AppImageUpdate yet, causing this function to raise a RuntimeError.

        Once it works, it should return None, and will raise
        AppImageUpdateError if it fails.

        :raises: RuntimeError, AppImageUpdateError
        """

        rv = lib.Updater__stop(self._updater)

        if not rv:
            raise AppImageUpdateError("Updater__stop")


    def progress(self):
        """
        Get the current progress value.

        :return: current progress (0 < progress < 1)
        :rtype: double
        """

        rv = lib.Updater__progress(self._updater)

        if rv < 0:
            raise AppImageUpdateError("Updater__progress")

        return rv


__ALL__ = (UpdaterState, Updater, AppImageUpdateError,)
