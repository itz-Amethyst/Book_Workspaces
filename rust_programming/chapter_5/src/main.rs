mod _struct;
struct  User {
    user_name: String,
    email: String,
    sign_in_count: u64,
    active: bool

}

fn main() {
    // let mut user1 = User{
    //     email: String::from("Milad@gmail.com"),
    //     user_name: String::from("Milad"),
    //     active: true,
    //     sign_in_count: 1
    // };

    // let name = user1.user_name;
    // user1.user_name = String::from("Milad2");

    // let user2 = build_user(String::from("Ali@gmail.com"), String::from("Milad222"));

    // let user3 = User{
    //     email: String::from("Test@gmail.com"),
    //     user_name: String::from("test"),
    //     active: user1.active
    //     //! active and sign_in come from user2
    //     ..user2
    // };

    // struct Color(i32, i32 , i32);
    // struct Point(i32, i32, i32);

    _struct::main();

}

fn build_user(email: String, user_name: String) -> User {
    User {
        email,
        user_name,
        active: true,
        sign_in_count:1
    }

}
