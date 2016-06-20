#include <stdio.h>
#define MAX 1000

int main(int argc, char const *argv[])
{
	int n;
	int quadrado[MAX][MAX];

	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			scanf("%d", &quadrado[i][j]);
		}
	}

	// verifica o valor da soma da primeira 
	// linha e compara com as outras
	int soma = 0;
	for (int i = 0; i < n; ++i)
	{
		soma += quadrado[0][i];
	}

	// verifica as linhas horizontais
	int soma_geral;
	for (int i = 0; i < n; ++i)
	{
		soma_geral = 0;
		for (int j = 0; j < n; ++j)
		{
			soma_geral += quadrado[i][j];
		}
		if(soma_geral != soma) 
		{
			printf("0");
			return 0;
		}
	}

	// verifica as linhas verticais
	for (int i = 0; i < n; ++i)
	{
		soma_geral = 0;
		for (int j = 0; j < n; ++j)
		{
			soma_geral += quadrado[j][i];
		}
		if(soma_geral != soma) 
		{
			printf("0");
			return 0;
		}
	}

	// verifica a linha diagonal esquerda
	int k = 0;
	soma_geral = 0;
	for (int i = 0; i < n; ++i)
	{
		soma_geral += quadrado[i][k];
		k++;
	}
	if(soma_geral != soma) 
	{
		printf("0");
		return 0;
	}

	// verifica a linha diagonal direita
	k = n-1;
	soma_geral = 0;
	for (int i = 0; i < n; ++i)
	{
		soma_geral += quadrado[i][k];
		k--;
	}
	if(soma_geral != soma) 
	{
		printf("0");
		return 0;
	}
	

	printf("%d", soma);
	return 0;
}