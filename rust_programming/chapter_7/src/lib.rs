fn request_gateaway(){

}
mod font_of_house {
    pub mod hosting {
        fn add_to_blahblahblah(){

        }

        pub fn seat_the_table(){

        }
    }

    mod client {
        use crate::request_gateaway;

        fn eat_order(){

        }

        fn order(){

        }

        fn pay_bill(){
            request_gateaway();
        }

    }
}

pub fn eat_at_other_place(){
    crate::font_of_house::hosting::seat_the_table();
}