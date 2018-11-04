package main

import "fmt"

func main() {
	var id1, id2, no1, no2 int
	var price1, price2 float32
	fmt.Scanf("%d %d %f", &id1, &no1, &price1)
	fmt.Scanf("%d %d %f", &id2, &no2, &price2)

	var total float32 = float32(no1) * price1 + float32(no2) * price2

	fmt.Printf("VALOR A PAGAR: R$ %.2f\n", total)
}