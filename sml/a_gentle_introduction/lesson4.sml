fun sum nil     = 0
  | sum(h::t)   = h + sum t;

fun doublist nil   = nil
  | doublist(h::t) = 2*h :: doublist t;

fun triplist nil    = nil
  | triplist (h::t) = 3*h :: triplist t;

fun duplist nil   = nil
|   duplist(h::t) = h::h::duplist t;

fun prodlist nil    = 1
  | prodlist (h::t) = h * prodlist t;

fun len nil    = 0
  | len (h::t) = 1 + len t;

fun vallist nil    = nil
  | vallist (h::t) = (ord(String.sub(h,0)) - ord #"0") :: vallist t;

fun reverse nil   = nil
| reverse(h::t) = (reverse t) @ [h];

fun space nil    = nil
  | space (h::t) = h :: " " :: space t;

fun flatten nil    = nil
  | flatten (h::t) = h @ flatten t;

fun count_1s nil    = 0
  | count_1s (h::t) = 
  if h = 1
  then 1 + count_1s t
  else count_1s t

fun timelist nil _  = nil
  | timelist (h::t) n = n * h :: timelist t n;

fun last [h]    = h
  | last (h::t) = last t;

fun member nil e    = false
  | member (h::t) e =
  if h = e then true
  else member t e;