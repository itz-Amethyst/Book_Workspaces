mod ownership;

fn main() {

    let mut x = String::from("Hello");

    x.push_str("World");

    println!("{}", x);

    let s1 = String::from("New");

    // Move mechanism works fine with integer and bool and single char (does not need clone)
    
    let s2 = s1.clone();

    println!("{}, {}", s1, s2);

    let mut owner = String::from("Owner");

    let len = take_owner_return_len(&owner);

    println!("Owner is {}, len is {}", owner, len);

    take_owner_and_change(& mut owner);
    println!("New owner is {}", owner);


    fn take_owner_return_len(s: &String) -> usize {
        let len = s.len();
        len
    }
    
    fn take_owner_and_change (s: & mut String) {
        let var: () = s.push_str("is me!");
        var
    }

    ownership::main();

}
