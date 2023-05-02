% facts
on(a, table).
on(b, table).
on(c, table).
clear(a).
clear(b).
clear(c).

% rules
move(X, Y) :-
    clear(Y),
    on(X, Z),
    clear(X),
    X \= Y,
    Y \= table,
    Z \= Y,
    retract(on(X, Z)),
    assert(on(X, Y)),
    retract(clear(Y)),
    assert(clear(X)),
    assert(clear(Z)),
    write(X), write(' moved to '), write(Y), nl.

% queries
move(a, b).
move(a, c).
move(b, c).
