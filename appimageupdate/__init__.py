import enum

from _appimageupdate import Updater as _Updater, AppImageUpdateError


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
        self._updater = _Updater(path_to_appimage)

    def check_for_changes(self, method=0):
        """
        Check whether an update is available.

        This can only be done before the update process is started.

        See AppImageUpdate's documentation for the meaning of method.

        :param int method: method to use
        :return: True if an update is available, False otherwise
        :rtype: bool
        """

        return self._updater.checkForChanges(method)

    def start(self):
        """
        Start the update process in the background.

        Use isDone() to check whether the update has finished.

        You can stop the update process with stop().

        :return: True if successful, False if the update has been started
            already.
        :rtype: bool
        """

        return self._updater.start()

    def describe_appimage(self):
        """
        Describe the AppImage in a standard format. Useful for debugging.

        :return: String containing information about the AppImage
        :rtype: str
        """

        return self._updater.describeAppImage()

    def is_done(self):
        """
        Check whether the running update process has finished.

        Internally tests whether state() reports a final state.

        You should check this in a loop, and e.g., sleep between the calls.

        :return: True if the process is done, False otherwise
        :rtype: bool
        """

        return self._updater.isDone()

    def has_error(self):
        """
        Checks whether the update failed.

        This checks whether the state() is set to an error value.

        :return: True if an error has occured, False otherwise
        """

        return self._updater.hasError()

    def state(self):
        """
        Returns the state of the updater.

        :return: state of the updater
        :rtype: UpdaterState
        """

        return UpdaterState(self._updater.state())

    def stop(self):
        """
        Stop the update process

        Please beware this feature has most likely not been implemented in
        AppImageUpdate yet, causing this function to raise a RuntimeError.

        :return: True when stopping worked, False otherwise
        :rtype: bool
        :raises: RuntimeError
        """

        return self._updater.stop()

    def progress(self):
        """
        Get the current progress value.

        :return: current progress (0 < progress < 1)
        :rtype: double
        """

        return self._updater.progress()
