#[derive(Debug)]
struct Rectangle {
    width: u64,
    height: u64
}

impl Rectangle {
    fn area(&self) -> u64 {
        self.height * self.width
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

impl Rectangle {
    // Assosiated func doesnt get &self
    fn square(size: u64) -> Rectangle {
        Rectangle {
            width: size,
            height: size
        }
    }
}

pub fn main(){
    let rect = Rectangle {
        width: 50,
        height: 60
    };

    let rect2 = Rectangle {
        width: 70,
        height: 260
    };

    let rect3 = Rectangle {
        width: 20,
        height: 20
    };

    let rect4 = Rectangle::square(30);
    println!("{:#?}", rect4);


    println!("{}", rect.area());

    println!("Rect is :{:#?}", rect);

    println!("Can hold is: {}", rect.can_hold(&rect2));
    println!("Can hold is: {}", rect.can_hold(&rect3));


}

// Old
// fn area(rectangle: &Rectangle) -> u64 {
//     rectangle.width * rectangle.height
// }