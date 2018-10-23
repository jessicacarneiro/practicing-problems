(* returns a list with all elements replicated n times *)

fun listReplication (nil,_) =  []
  | listReplication (h::t,0) = []
  | listReplication (h::t,n) = 
    [h] @ listReplication(h::t,n-1) @ listReplication(t,n)