(* create an array of n elements in range (1,n) *)

fun arrayN 0 = []
  | arrayN n = arrayN (n-1) @ [n]