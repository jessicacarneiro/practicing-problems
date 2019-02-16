#include <iostream>
#define N_BILLS 6
#define N_COINS 6

using namespace std;

int main() {
    int bills[N_BILLS] = {10000, 5000, 2000, 1000, 500, 200};
    int coins[N_COINS] = {100, 50, 25, 10, 5, 1};

    double value;
    cin >> value;
    int int_value = (100 * value);

    int bills_used[N_BILLS] = {0, 0, 0, 0, 0, 0};
    int coins_used[N_COINS] = {0, 0, 0, 0, 0, 0};

    int i = 0;
    while (int_value > 100 && i < N_BILLS)
    {
        if (bills[i] <= int_value)
        {
            int_value -= bills[i];
            bills_used[i]++;
        }
        else i++;
    }

    i = 0;
    while (int_value > 0 && i < N_COINS)
    {
        if (coins[i] <= int_value)
        {
            int_value -= coins[i];
            coins_used[i]++;
        }
        else i++;
    }

    cout.precision(2);
    cout << "NOTAS:" << endl;
    for (int i = 0; i < N_BILLS; i++)
        cout << bills_used[i] << " nota(s) de R$ " << 
                        fixed << bills[i]/100.0 << endl;

    cout << "MOEDAS:" << endl;
    for (int j = 0; j < N_COINS; j++)
        cout << coins_used[j] << " moeda(s) de R$ " <<
                        fixed << coins[j]/100.0 << endl;

    return 0;
}