fib(0, 0).
fib(1, 1).
fib(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, Result1),
    fib(N2, Result2),
    Result is Result1 + Result2.

fibonacci_series(0, []).
fibonacci_series(N, [Result|Series]) :-
    N >= 0,
    fib(N, Result),
    N1 is N - 1,
    fibonacci_series(N1, Series).
