female(asmita).
female(akshaya).
female(laxmi).
female(vaishali).
male(vijay).
male(janu).

parent(janu,vijay).
parent(laxmi,vijay).
parent(vijay,asmita).
parent(akshaya,asmita).
parent(vijay,vaishali).
parent(akshaya,vaishali).

mother(A,B):- parent(A,B), female(A).
father(A,B):- parent(A,B), male(A).

grandfather(A,C):-parent(A,B),parent(B,C),male(A).
grandmother(A,C):-parent(A,B),parent(B,C),female(A).

siblings(A,B):-father(C,A),father(C,B),mother(D,A),mother(D,B).
