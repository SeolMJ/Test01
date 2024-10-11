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
        scanln; int.parse; clamp 1 3;
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