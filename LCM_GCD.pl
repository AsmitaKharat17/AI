gcd(X,Y,G):- X=Y,G=X.
gcd(X,Y,G):- X<Y,
C is Y-X,
gcd(X,C,G).
gcd(X,Y,G):- X>Y, gcd(Y,X,G).
lcm(X,Y,LCM):-gcd(X,Y,GCD), LCM is X*Y//GCD.
