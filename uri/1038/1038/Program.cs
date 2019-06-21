using System;

namespace _1038
{
    class Program
    {
        static void Main(string[] args)
        {
            float[] prices = new float[6] {0.0F, 4.0F, 4.5F, 5.0F, 2.0F, 1.5F};
            string line = Console.ReadLine(); 
            string[] values = line.Split(' ');
            int code = Convert.ToInt32(values[0]);
            int amount = Convert.ToInt32(values[1]);
            double total = prices[code] * amount;
            Console.WriteLine("Total: R$ " + String.Format("{0:0.00}", total).Replace(",", "."));
        }
    }
}
