fn main() {
    const MAX_POINTS: u32 = 100_000;

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
}
