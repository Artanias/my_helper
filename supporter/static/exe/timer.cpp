#include <windows.h>
#include <sstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
	if (argc > 2){
		std::stringstream convert(argv[1]);
		int minutes;
		if (!(convert >> minutes)) minutes = 0;
		std::string temp(argv[2]), run_music;

		Sleep(1000 * minutes * 60);
		
		if(temp != "-"){
			bool haveSpaces = false;
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

			system(run_music.c_str());
		}
	}

	if(argc > 3){
		std::string command = "start chrome ";
		command += argv[3];
		command += " /incognito";
		system(command.c_str());
	}

	return 0;
};
