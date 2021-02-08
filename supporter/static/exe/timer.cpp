#include <windows.h>
#include <sstream>
#include <iostream>

int main(int argc, char *argv[]) {
	//ShowWindow(GetConsoleWindow(), SW_HIDE);
	if (argc > 3){
		std::stringstream convert(argv[3]);
		int minutes;
		if (!(convert >> minutes)) minutes = 0;
		Sleep(1000 * minutes * 60);
		if (strcmp(argv[2], "rest") == 0){
			MessageBox(NULL, argv[1], "Info", MB_OK | MB_ICONINFORMATION);
		}
		else if(strcmp(argv[2], "work") == 0){
			MessageBox(NULL, argv[1], "Warning", MB_OK | MB_ICONWARNING);
		}
	}
	return 0;
};
