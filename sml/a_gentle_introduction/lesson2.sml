(* creating a binding *)
val a = 4;
val (d,e) = (2,"two");
val [one,two,three] = [1,2,3];
0::[1,2,3];
[0]@[1,2,3];

(* functions to use with lists *)
hd [1,2,3,4]; (* val it = 1 : int *)
tl [1,2,3,4]; (* val it = [2,3,4] : int list *)
rev [1,2,3,4]; (* val it = [4,3,2,1] : int list *)

(* functions with strings *)
explode "north";

(* the function composition operator is o (say of).
   We can use it to create functions from functions. *)
val first = hd o explode;
val second = hd o tl o explode;
val third = hd o tl o tl o explode;
val fourth = hd o tl o tl o tl o explode;

fun roll s =
  str(fourth s) ^ str(first s) ^ str(second s) ^ str(third s);
fun exch s =
  str(second s) ^ str(first s) ^ str(third s) ^ str(fourth s);

fun fb s = roll(roll (roll s));
fun fc s = roll(exch (fb s));
fun fd s = exch(fc(exch s));