fn five() -> i32{
    return 5;
}

fn main() {
    const MAX_POINTS: u32 = 100_000;


    let x = five();

    println!("{}", x);
    // Wrong XXX
    // let mut spaces = "   ";
    // spaces = spaces.len();

    //? Shadowing
    let spaces = "    ";
    let spaces = spaces.len();
    println!("Lines {}", spaces);


    // Unsigned => like u8 => from 0 to 256 (positive number without any sign (- , +))
    // signed => like i8 => from -128 to 127 (number with sign like (-14, +15 , -21))

    // remainder
    println!("{}", remainder = 43 % 5);


    let x : (u32, f32, bool) = (45, 34.0, true);

    let first = x.0;

    let second = x.1;

    println!("{}", second);

    let a = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"];

    const INDEX :usize = 11;

    if INDEX >= a.len(){
        // Todo
        return println!("Index out of range, enter between 0 and {}", a.len() - 1);
    } 
    let first = a[INDEX];
    println!("{}", first);
        
    

    // let first = a[0];


    let number = 0;

    if number != 0 {
        println!("Number was something other than 0")
    }
    else if number >= 100 {
        println!("Number is bigger than 100");
    }
    else{
        println!("something");
    }

    let condition: bool = true;
    // this will throw an error both estatements must be same type like 5 and 6
    let number = if condition {
        5
    }
    else{
        // wrong
        // "6"
        // true
        6
    };


    let mut limit = 3;

    while limit != 0 {
        limit = limit -1;
        println!("{}", limit);
    }

    for month in a.iter() {
        println!("{}", month);
    }

    // rev == reverse
    for number in (1..4).rev(){
        println!("{}", number);
    }
}
