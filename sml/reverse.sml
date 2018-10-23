(* returns a reversed list *)

fun reverse nil = []
  | reverse (h::t) = reverse(t) @ [h]