"Hello World!"; (* a simple hello world *)

(* using integer operators *)
fun double x = 2*x;
fun inc x = x + 1;

(* adapting to use real numbers *)
fun doubleReal x:real = 2.0*x;
fun incReal x:real = x + 1.0;

(* concatenating strings *)
fun adda s = s ^ "a";

(* calculating an average *)
fun averI (x,y) = (x+y) div 2;
fun averR (x,y) = (x+y)/2.0;

(* reusing functions *)
fun triple x = 3*x;
fun times4 x = double(double x);
fun times6 x = double(triple x);
fun times9 x = triple(triple x);

fun duplicate s = s ^ s;
fun quadricate s = duplicate(duplicate s);
fun octicate s = quadricate(duplicate s);
fun hexadecicate s = quadricate(quadricate s);

(* using pre-defined functions for char and string *)
fun middle s = substring(s,size s div 2,1);
fun dtrunc s = substring(s,1,size s - 2);
fun incFirst s = 
  str(chr(ord(String.sub(s,0)) + 1)) ^ substring(s,1,size s - 1);
fun switch s =
  substring(s,size s div 2, size s div 2) ^ substring(s,0, size s div 2);
fun dubmid s =
  substring(s,0,(1 + size s) div 2) ^ substring(s,size s div 2, (1 + size s) div 2);
fun sndhalf s = substring(s, size s div 2, size s div 2);