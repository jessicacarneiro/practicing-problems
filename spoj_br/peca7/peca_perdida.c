#include <stdio.h>
#define MAX 1000

int main(int argc, char const *argv[])
{
	int i, j, temp;
	int n, pecas[MAX];

	scanf("%d", &n);
	for (i = 0; i < n-1; ++i)
	{
		scanf("%d", &pecas[i]);
	}

	for (i = 0; i < n-1; ++i)
	{
		for (j = 0; j < n-2; ++j)
		{
			if (pecas[j] > pecas[j+1])
			{
				temp = pecas[j];
				pecas[j] = pecas[j+1];
				pecas[j+1] = temp;
			}
		}
	}

	for (i = 0; i <= n-1; ++i)
	{
		if(pecas[i] != i+1) {
			printf("%d", i+1);
			return 0;
		}
	}

	return 0;
}