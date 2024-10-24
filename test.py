1:int + 2
=> 3

random ?
3 {
    ...
}
4 {
    ...
}
_ {
    asdfasdf
}


{
    a > 0 ? 
    true a
    false a * -1;
}
:abs

{
    a * a
}
:square

1000:i
1 2
{+ i 1-}


Http.Post "https://www.google.com" "application/json" [
        "asdf": code
        "javascript": language
    ].Json.Serialize;
    ;
await {
    .Http.Send;
};

Http.Post "https://www.google.com" "application/json" ([
        "asdf": code
        "javascript": language
    ] Json.Serialize;);
await {
    Http.Send;
};

[
    "asdf": code
    "javascript": language
]
Json.Serialize; :content

Http.Post "https://www.google.com" "application/json" content;
Send;

# showcase
print "Hello, World!";
"Hello, World!" print;

0 :a
a = 3;
a + 2; :b
4 =+ b;;

print b to_string;;
b to_string; print;

Std::random 0..<4; ; :rand "random value " <> if rand == 0 "is zero"; if != 0 "is not zero"; ;

"random value " :text
Std::random 0..<4; ; if == 0 {text =<> "is zero"}; if != 0 {text =<> "is not zero"};

Http::post "https://www.google.com" "application/json" Json::serialize [
    ...(content)
]

Http::post Urls::get "google" Http::post::type::json Json::serialize [
    
]






int a = 4;

4 :a

int b = a + 3;

a .+ 3 :b

+ a 3 // Add(a, 3)
// a.Add(3)
a .+ 3 



#showcase
print "Hello, World!"; //print("Hello, World!");
"hello, World!" print; //"Hello, World!".print();

1 :a //int a = 1;
a + 2; :b //int b = a + 2;

a = 3; //a = 3;
a =+ 4;; //a = a + 4;

if a == 0 {
    print "a is zero";
};

# 베스킨라빈스31

["me":name]:me
["ai":name]:ai

[
    me
    ai**4;
]:players

0:|0..<players##|turn
0:|0..31|number

{
    1..Math::clamp 30-number; 1 3;; Random::range; =>
}:select_random

loop {
    players#turn; :current_player
    println "{current_player.name}'s turn!";
    if current_player === me; {
        scanln; int::parse; clamp 1 3;
    };
    if current_player === ai {
        select_random;
    };
    :move
    += number;
    for 1..move; {:i
        println "{i}";
    }
    if number >= 31 {
        println "{current_player.name} lose";      
    } else: {
        continue;
    }
};

# add 3
{[?:a ?:b ?:c]
    a+b;+c;=>;
}:add3

# onecard simulation


[
    @|[
        Diamond
        Spade
        Heart
        Clover
    ]::Type

    @|[
        A
        Two
        Three
        Four
        Five
        Six
        Seven
        Eight
        Nine
        Ten
        J Q K
        BlackJoker ColorJoker
    ]::Num

    Type:type
    Num:num
]:Card

{[?:a ?:b]
    a & b; != [];
}:match

[]:Card|@none:last
0:stack

{[Card:card]
    (last == null=>!!;)
    card.type != last.type; && card.num != last.num; => {}

    stack 
}:OneCard.Simulate


#asdf
Settings.get @NewSetting Int;

@[?]:Setting

{[Setting:setting $:type]
    ...
}:Settings.get

print("Hello World")
if(last == null {
    asdf
})

############################

[
    @|[
        diamond
        spade
        heart
        clover
    ]::Type

    @|[
        A
        Two
        Three
        Four
        Five
        Six
        Seven
        Eight
        Nine
        Ten
        J Q K
        BlackJoker ColorJoker
    ]::Num

    Type:type
    Num:num
]:Card

{[?:a ?:b]
    a & b; != [];
}:match



[]:Card|@none:last
0:stack


{[Card:card]
    last==(@none)=>(!!)
    card.type!=(last.type)&&(card.num!=(last.num))=>>@failed
    stack!=(0)=>({//need to attack
        card.num!=(@Two)=>({
            
        })
    })
}

{
    {@|{
        a,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine,
        Ten,
        j,q,k,
        joker
    }}:Number
    
    {@|{
        spade,
        heart,
        clover,
        diamond
    }}:Symbol

    Number.a:a
    Symbol.diamond:symbol
}:Card

// 2(<-3)[2]->A(<-5)[3]->A-Spade(<-5)[5]<->Spade-Joker[5]->Heart-Joker[7]

{{Card:card}
    card.symbol!=[last.symbol]&&[card.number!=[last.number]]=>[!!]
    last==|(
        [{@a,?}]&&[card.symbol!=&[{@a,@five,@joker}]],
        [{@a,@spade}]&&[card.symbol!=[@joker]],
        [{@two,?}]&&[card.symbol!=&[{@a,@two,@three,@joker}]],
        [{@joker,@spade}]&&[card!=[{@joker,@heart}]],
        [{@joker,@heart}]
    )=>[!!]
}:check_counter

{>-[int]+=[stack]
}:incr_stack

{>-{Card:card}
    last==[@none]=>[!!]
    card.symbol!=[last.symbol]&&[card.number!=[last.number]]=>[!!]
    stack!=[0]=>[{// this player needs to attack.
        card.number(
            !=&[{@a, @two, @three, @black_joker, @color_joker}]=>[!!],
            ==[@a]=>[{
                card.type==[@spade]=>[]
            }]
        )
        check_counter[card.number]
        card==(
            [@a,@spade]=>[5->],
            [@a,?]=>[3->],
            [@two,?]=>[2->],
            [@joker,@spade]=>[5->],
            [@joker,@heart]=>[7->]
        )incr_stack[]

        card==(
            {@a,@spade}=>{5->},
            {@a,?}=>{3->},
            {@two,?}=>{2->},
            {@joker,@spade}=>{5->},
            {@joker,@heart}=>{7->}
        )incr_stack
    }]
}

[>-[Card.card]
    last=={
        [@a,?]=>card.number!={@a;@five;@joker};
        [@a,@spade]=>card.symbol!=@joker;
        [@two,?]=>card.symbol!={@a;@two;@three;@joker};
        [@joker,{@spade;@clover}]=>card!=[@joker,{@spade;@clover}];
        [@joker,{@heart;@diamond}]=>card!=[@joker,{@heart;@diamond}]
    }=>!!
]:counter_move

[>-[Card:card]
    last==@none=>[!!]
    card.number==joker{
        =>[card.symbol,last.symbol]=={
            [{@spade;@clover},{@heart;@diamond}],
            [{@heart;@diamond},{@spade;@clover}]
        }=>!!
        !>card.symbol!=last.symbol=>card.number!=last.number=>!!
    }
    stack!=0=>[
        last=={
            [@a,?]=>card.number!={@a;@five;@joker}=>;
            [@a,@spade]=>card.symbol!=@joker=>;
            [@two,?]=>card.symbol!={@a;@two;@three;@joker}=>;
            [@joker,{@spade;@clover}]=>card!=[@joker,{@spade;@clover}]=>;
            [@joker,{@heart;@diamond}]=>card!=[@joker,{@heart;@diamond}]=>
        }!!

        card.number=={
            @a=>card.symbol==@spade{
                =>5,
                !>3
            },
            @two=>2,
            @joker=>card.symbol==@spade{
                =>5,
                !>7
            }
        }+=stack
    ]
]:submit_card

{0,1,2,3,4}==[3]

3==[{0,1,2,3,4}]

a(==[b],==[c],==[d])

a!=&[{b,c,d}]
a!=|[{b,c,d}]