(* pow returns a^b *)

fun pow (a:real,b):real =
  if b = 0 then 1.0
  else
    a * pow (a:real,b-1):real