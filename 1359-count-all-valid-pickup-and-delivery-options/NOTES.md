explanation
if n ==1
only one opition ---> p1 d1
if n ==2
[] p1 [] d1 []
we have 3 gaps to put p2 and d2
when p2 is in the first gap d2 canbe put in the first second and third gap (3 ways)
when p2 is int he second gap d2 canbe put int second and third gap (2 ways)
when p2 is in the third gap d2 canbe only have one opetion thrid gap(1 ways)
the total ways is 3+2+1 or gaps * (gaps+1)//2
the number gaps is :
for 2 we have 3 gaps
for 3 we have 5 gaps
in general 2*i - 1
:: the total way is prev * current ways