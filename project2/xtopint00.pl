% Zadani c. 2:
% Napiste program resici ukol dany predikatem u2(LIN,LOUTL,LOUTR), kde LIN je 
% vstupni seznam s nejmene dvema prvky. Vystupni promenna LOUTL vraci levou
% polovinu seznamu LIN a vystupni promenna LOUTR vraci pravou polovinu 
% seznamu LIN. Pokud ma seznam LIN lichy pocet prvku, je prostredni prvek 
% soucasti seznamu LOUTR.

% Testovaci predikaty:                                  % LOUTL		LOUTR
u2_1:- u2([5,a0,b,16,c,kolo,-4],LOUTL,LOUTR),
       write(LOUTL),write(' '),write(LOUTR).	  	% [5,a0,b]	[16,c,kolo,-4]
u2_2:- u2([5,a0,b,c,kolo,-4],LOUTL,LOUTR),
       write(LOUTL),write(' '),write(LOUTR).	  	% [5,a0,b]	[c, kolo, -4]
u2_3:- u2([5], LOUTL, LOUTR),
       write(LOUTL),write(' '),write(LOUTR).	  	% []		[5]
u2_r:- write('Zadej LIN: '),read(LIN),
       u2(LIN,LOUTL,LOUTR),write(LOUTL),write(' '),write(LOUTR).

% Reseni:
u2(LIN, LOUTL, LOUTR) :-
    length(LIN, Len),   
    HalfLen is Len // 2,
    split_list(LIN, HalfLen, LOUTL, LOUTR).

% Helper predicate to split the list into two parts
split_list(LIN, 0, [], LIN).
split_list([Head|Tail], N, [Head|LOUTL], LOUTR) :-
    N > 0,
    N1 is N - 1,
    split_list(Tail, N1, LOUTL, LOUTR).
