#include <iostream>

using namespace std;


int main()
{
    string username;
    string password;
    string try_u , try_p;
    string menu;
    int logged = 0;
    while(logged == 0)
    {
        cout << "R to register / L to login\n";
        cin >> menu;
        if(menu == "R")
        {
            cout << "enter username\n";
            cin >> username;
            cout << "enter password\n";
            cin >> password;
        }
        if(menu == "L")
        {
            cout << "enter username\n";
            cin >> try_u;
            if(try_u == username)
            {
                cout << "enter password\n";
                cin >> try_p;
                if(try_p == password)
                {
                    cout << "logged in\n";
                    logged = 1;
                }
            }
        }
    }
}

