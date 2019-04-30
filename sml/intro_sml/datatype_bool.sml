datatype bool = True | False;

fun myNot True  = False
  | myNot False = True;

fun myAndAlso (False, _)   = False
  | myAndAlso (_, False)   = False
  | myAndAlso (True, True) = True;

fun myOrElse (True, _)      = True
  | myOrElse (_, True)      = True
  | myOrElse (False, False) = False;
