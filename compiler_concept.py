// lexer

[
    @|[
        
    ]:type
]:token

[Card:card (Sub SUb Sub)
    func func func
]:a

a==b;
;==(a,b)

[
    Token**(?:n) {'global _start\nstart:\n':buffer;}
    foreach
    .type==[
        @return=>
        i+1<n=>token#(i+1).type==@integer=>
        i+2<n=>token#(i+2).type==@semi_colon=>
        out
        ++'mov rax, 60\n'
        ++'mov rdi, '++(token#(i+1).value ToString)++'\n'
        ++'syscal\n'
        =out;
    ];
    out
]:tokens_to_asm

[..] tokens_to_asm file.create '../out.asm' file.execute


{
    "asdf",
    "asdfasdf",
    "asdfasdf"
} Print;

