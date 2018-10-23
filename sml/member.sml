(* member returns true if e is an element in the list *)

fun member (e,nil) = false
  | member (e,h::t) = 
  if h = e then true
  else 
    member(e,t)