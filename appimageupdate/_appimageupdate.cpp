// boost::python is used to generate a wrapper for the
// appimage::update::Updater class
#include <boost/python.hpp>

// library includes
#include "appimage/update.h"

using namespace appimage::update;
using namespace boost::python;
using namespace std;
using namespace std;

PyObject* createExceptionClass(const char* name, PyObject* baseTypeObj = PyExc_Exception) {
    string scopeName = extract<string>(scope().attr("__name__"));
    string qualifiedName0 = scopeName + "." + name;
    char* qualifiedName1 = const_cast<char*>(qualifiedName0.c_str());

    PyObject* typeObj = PyErr_NewException(qualifiedName1, baseTypeObj, 0);
    if(!typeObj) throw_error_already_set();
    scope().attr(name) = handle<>(borrowed(typeObj));
    return typeObj;
}

PyObject* AppImageUpdateError = NULL;

void raiseAppImageUpdateError(const std::string& description) {
    PyErr_SetString(AppImageUpdateError, strdup(description.c_str()));
}

string Updater__describeAppImage(Updater& self) {
    string description;

    if (!self.describeAppImage(description))
        raiseAppImageUpdateError("Failed to describe AppImage");

    return description;
}

bool Updater__checkForChanges(Updater& self, unsigned int method = 0) {
    bool updateAvailable;

    if (!self.checkForChanges(updateAvailable, method))
        raiseAppImageUpdateError("Failed to check for changes");

    return updateAvailable;
}

double Updater__progress(Updater& self) {
    double progress;

    if (!self.progress(progress))
        raiseAppImageUpdateError("Failed to fetch progress");

    return progress;
}

int Updater__state(Updater& self) {
    return (int) self.state();
}

BOOST_PYTHON_MODULE(_appimageupdate) {
    class_<Updater>("Updater", init<std::string>())
        .def("start", &Updater::start)
        .def("stop", &Updater::stop)
        .def("isDone", &Updater::isDone)
        .def("hasError", &Updater::hasError)
        .def("nextStatusMessage", &Updater::nextStatusMessage)
        .def("pathToNewFile", &Updater::pathToNewFile)
        .def("remoteFileSize", &Updater::remoteFileSize)
        .def("progress", &Updater__progress)
        .def("state", &Updater__state)
        .def("describeAppImage", &Updater__describeAppImage)
        .def("checkForChanges", &Updater__checkForChanges);

    // needs to be initialized in init function
    AppImageUpdateError = createExceptionClass("AppImageUpdateError");
}


