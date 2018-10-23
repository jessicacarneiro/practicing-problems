fun smaller a b c =
  if a < b andalso b < c
  then true
  else false

fun pyth a b c =
  if a*a + b*b = c*c
  then true
  else false