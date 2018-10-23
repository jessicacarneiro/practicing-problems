(* append_lists appends l2 after l1 *)

fun appendLists l1 nil = l1
  | appendLists l1 l2 = l1 @ l2
