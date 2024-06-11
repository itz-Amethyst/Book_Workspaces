use rand::{Rng, CryptoRng, ErrorKind::Transient};

// messy
use std::io;
use std::io::Write;

// refactored way:
use std::io::{self, Write};

use std::io::*;

mod restaurant {
    pub struct Brakefast {
        food: String,
        seassonal_fruid: String
    }

    impl Brakefast{
        pub fn Summer(food: &str) -> Brakefast {
            Brakefast{
                food: String::from(food),
                seassonal_fruid: String::from("Apple")
            }
        }
    }
}

mod front_of_restuarunt {
    pub mod hosting{
        pub fn serving(){

        }
    }
}

// I
use crate::front_of_restuarunt::hosting;
pub fn eat_at_summer() {
    let mut meat = restaurant::Brakefast::Summer("Fries");
    // I
    hosting::serving();
}