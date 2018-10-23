(* returns the sum of the odds numbers in the list *)

fun sumOdds nil = 0
  | sumOdds (h::t) = 
  if h mod 2 <> 0 
  then h + sumOdds(t)
  else sumOdds(t)