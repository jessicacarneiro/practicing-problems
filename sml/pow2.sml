(* pow returns a^b *)

fun pow (a:real,0):real = 1.0
  | pow (a:real,1):real = a
  | pow (a:real,b):real =
    a * pow(a:real,b-1):real