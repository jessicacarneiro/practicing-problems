using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution
{

	// Complete the sockMerchant function below.
	static int sockMerchant(int n, int[] ar)
	{
		var pairs = new Dictionary<int, int>();

		foreach (var sock in ar)
		{
			if (pairs.TryGetValue(sock, out var sockCount))
			{
				pairs[sock] = ++sockCount;
			}
			else
			{
				pairs.Add(sock, 1);
			}
		}

		var total = 0;
		foreach (var sockType in pairs)
		{
			total += sockType.Value/2;
		}

		return total;
	}

	static void Main(string[] args)
	{
		TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

		int n = Convert.ToInt32(Console.ReadLine());

		int[] ar = Array.ConvertAll(Console.ReadLine().Split(' '), arTemp => Convert.ToInt32(arTemp))
			;
		int result = sockMerchant(n, ar);

		textWriter.WriteLine(result);

		textWriter.Flush();
		textWriter.Close();
	}
}
