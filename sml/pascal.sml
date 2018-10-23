(* pascal triangle *)

fun pascal (0,_) = 1
  | pascal (_,0) = 1
  | pascal (i,j) = 
  if i = j
  then 1
  else pascal(i-1,j-1) + pascal(i-1,j)