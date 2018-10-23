(* repeats returns true if the list has at
   least one element that repeats *)

fun repeats nil = false
  | repeats ([h]) = false
  | repeats (h1::h2::t) =
  if h1 = h2 then true
  else repeats (h2::t)