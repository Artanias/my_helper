#include <windows.h>
#include <sstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
	//ShowWindow(GetConsoleWindow(), SW_HIDE);
	if (argc > 2){
		std::stringstream convert(argv[1]);
		int minutes;
		if (!(convert >> minutes)) minutes = 0;
		bool haveSpaces = false;
		std::string temp(argv[2]), run_music;
		for (int i = 0; i < temp.length(); i++){
			if (temp[i] == ' '){
				haveSpaces = true;
				break;
			}
		}
		if (haveSpaces){
			run_music = "\"";
			run_music  += temp;
			run_music += "\"";	
		}
		else run_music = temp;
		Sleep(1000 * minutes * 60);
		system(run_music.c_str());
		/*if (strcmp(argv[2], "rest") == 0){
			//MessageBox(NULL, argv[1], "Info", MB_OK | MB_ICONINFORMATION);
		}
		else if(strcmp(argv[2], "work") == 0){
			//MessageBox(NULL, argv[1], "Warning", MB_OK | MB_ICONWARNING);
		}*/
	}
	system("start chrome https://www.youtube.com/watch?v=qx4FLF5QcAw /incognito");
	return 0;
};
