// CFFI header

void* Updater__create(const char const*);
void Updater__delete(void*);
bool Updater__start(void*);
bool Updater__stop(void*);
bool Updater__isDone(void*);
bool Updater__hasError(void*);
char* Updater__nextStatusMessage(void*);
char* Updater__pathToNewFile(void*);
int Updater__remoteFileSize(void*);
double Updater__progress(void*);
int Updater__state(void*);
char* Updater__describeAppImage(void*);
int Updater__checkForChanges(void*, unsigned int);

void free(void*);
