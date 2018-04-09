/* CFFI wrapper code */

// library includes
#include "appimage/update.h"

using namespace appimage::update;
using namespace std;

extern "C" {
    void* Updater__create(const char* pathToAppImage) {
        auto updater = new Updater(pathToAppImage);
        return (void*) updater;
    }

    void Updater__delete(void* self) {
        delete (Updater*) self;
    }

    bool Updater__start(void* self) {
        return ((Updater*) self)->start();
    }

    bool Updater__stop(void* self) {
        return ((Updater*) self)->stop();
    }

    bool Updater__isDone(void* self) {
        return ((Updater*) self)->isDone();
    }

    bool Updater__hasError(void* self) {
        return ((Updater*) self)->hasError();
    }

    char* Updater__nextStatusMessage(void* self) {
        std::string nextStatusMessage;

        if (!((Updater*) self)->nextStatusMessage(nextStatusMessage))
            return nullptr;

        auto* outBuffer = (char*) malloc(nextStatusMessage.size() + 1);
        strcpy(outBuffer, nextStatusMessage.c_str());

        return outBuffer;
    }

    char* Updater__pathToNewFile(void* self) {
        std::string pathToNewFile;

        if (!((Updater*) self)->pathToNewFile(pathToNewFile))
            return nullptr;

        auto* outBuffer = (char*) malloc(pathToNewFile.size() + 1);
        strcpy(outBuffer, pathToNewFile.c_str());

        return outBuffer;
    }

    int Updater__remoteFileSize(void* self) {
        off_t remoteFileSize;

        if (!((Updater*) self)->remoteFileSize(remoteFileSize))
            return -1;

        return (int) remoteFileSize;
    }

    double Updater__progress(void* self) {
        double progress;

        if (!((Updater*) self)->progress(progress))
            return -1;

        return progress;
    }

    int Updater__state(void* self) {
        return (int) ((Updater*) self)->state();
    }


    char* Updater__describeAppImage(void* self) {
        std::string description;

        if (!((Updater* ) self)->describeAppImage(description))
            return nullptr;

        return strdup(description.c_str());
    }

    int Updater__checkForChanges(void* self, unsigned int method) {
        bool updateAvailable;

        if (!((Updater*) self)->checkForChanges(updateAvailable, method))
            return -1;

        return updateAvailable ? 1 : 0;
    }
}
