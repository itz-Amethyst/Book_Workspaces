use std::{collections::HashMap, hash::Hash};

mod exercices;
fn main() {
    let mut v : Vec<i32> = vec![2, 4, 6];

    match v.get(0){
        Some(first) => println!("First is {}", first),
        None => println!("There is nothing")
    }

    let third = &v[2];

    v.push(0);

    for i in &mut v {
        *i += 50;
        println!("{}", i)
    }


    enum SpreedSheetIndex{
        Int(i32),
        Float(f32),
        Bool(bool)
    }

    let row = vec![
        SpreedSheetIndex::Int(3),
        SpreedSheetIndex::Float(2.3),
        SpreedSheetIndex::Bool(true)
    ];

    match &row[1] {
        SpreedSheetIndex::Int(i) => println!("Its an int!! {}",i),
        _ => println!("not an int")
    }


    let s1 = String::from("Test");

    let s2 = String::from("World");

    let s3 = format!("{} {}", s1, s2);
    println!("{}",s3);

    if let Some(c) = s1.chars().nth(1){
        println!("Second index is: {}", c);
    }

    let blue = String::from("Blue");
    let red = String::from("Red");

    let mut scores = HashMap::new();

    scores.insert(&blue, 20);

    let blue_score = scores.get(&blue);


    for (key, value) in &scores{
        println!("{}: {}", key, value);
    }

    let mut scores2 = HashMap::new();

    scores2.insert(String::from("Green"), 100);

    // if yellow wasnt defined set to 30
    scores2.entry(String::from("Yellow")).or_insert(30);
    // won't apply in fact
    scores2.entry(String::from("Yellow")).or_insert(60);

    println!("{:?}", &scores2);


    let text = "Hello my name is nobody! and i dont like myself like and";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }
    println!("{:?}", map);



    let text = "hello 365 days no kidding br9";

    let without_numbers:Vec<String> = text.split(char::is_numeric)
    // To iterate over vector and remove the whitespaces
    .map(str::trim)
    .filter(|s| !s.is_empty())
    .map(String::from)
    .collect();

    println!("{:?}", without_numbers);

    exercices::first::mean();

    let mut numbers_to_median = vec![5, 6, 23 ,2 ,5 ,2 ,1];
    let median_value = exercices::first::median(&mut numbers_to_median);

    println!("median is :{}", median_value);
}
