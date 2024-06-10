enum IpAddrKind {
    V6(u8, u8, u8, u8),
    V7(String)
}

enum Message{
    Quit,
    Move {x: i32, y: i32},
    Write(String),
    ChangeColor(i32, i32 ,i32)

}

struct IPAddress {
    kind: IpAddrKind,
    address: String
}

// enum Option<T>{
//     Some(T),
//     None
// }

#[derive(Debug)]
enum State {
    Tehran,
    Mazandaran,
    Shiraz,
    Esfahan
}

#[derive(Debug)]
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(State)
}

impl Coin{
    fn value_in_coin(&self) -> u32 {
        match self {
            Coin::Penny => 1,
            Coin::Nickel => 5,
            Coin::Dime => 10,
            Coin::Quarter(state) => {
                println!("State Quarter from: {:?}", state);
                25
            },
        }
    }
}

fn main() {

    let six = IpAddrKind::V6(127, 0, 0, 1);

    let home = IPAddress{
        kind: six,
        address:String::from("Home")
    };

    let some_number = Some(5);

    let absent_number: Option<i32> = None;

    let x = 4;

    let y :Option<i32> = None;

    println!("{}", x + y.unwrap_or(3));

    let dime = Coin::Dime;

    let quarter = Coin::Quarter(State::Tehran);

    println!("Penny value is:{}", dime.value_in_coin());
    println!("Quarter value is:{}", quarter.value_in_coin());

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);


    let three = Some(3);

    match three {
        Some(3) => println!("Three!!!"),
        _ => ()
    }
    // same as match
    if three == Some(3) {
        println!("THreeee !!")
    }


}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => {
            let result = Some(i + 1);
            println!("value is: {:?}", result);
            result
        },
        _ => None
    }
}