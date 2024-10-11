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