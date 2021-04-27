#include <stdlib.h>
#include <string>
#include <thread>
#include <windows.h>

int main()
{
	std::thread t1(system, "python manage.py runserver");
	Sleep(5000);
	std::thread t2(system, "start chrome http://localhost:8000 /incognito");

	t1.join();
	t2.join();
	return 0;
}
