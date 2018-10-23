(* less returns a list of all elements except e *)

fun less (e,nil) = nil
  | less (e,h::t) = 
  if h < e 
  then [h] @ less(e,t)
  else less(e,t)