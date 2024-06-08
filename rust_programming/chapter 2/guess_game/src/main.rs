extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main(){
    println!("Guess game i guess?!");
    let secret_number = rand::thread_rng().gen_range(1, 101);
    loop {
        println!("Enter your guess: ");
        let mut guess = String::new();
    
        io::stdin().read_line(&mut guess).expect("Failed to read the line");
    
        let guess: u32 = match guess.trim().parse() {
            Ok(number) => number,
            Err(_) => continue,
        };
    
        // println!("The secret number is {}", secret_number);
    
    
        println!("You guessed {}", guess);
    
        match guess.cmp(&secret_number){
            Ordering::Less => println!("Too low!"),
            Ordering::Equal => {
                println!("Correct!");
                break;
            },
            Ordering::Greater => println!("Too high!")
        }
    }
      
}