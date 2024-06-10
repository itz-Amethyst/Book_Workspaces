pub fn main(){

    let s = String::from("Hello world.");

    let s2 = "Hello world.";

    let word_manual = &s2[6..];
    let copy_kindda = &s2[..];

    println!("first: {}, second: {}", word_manual, copy_kindda);
    // s2 or s1 both works fine
    let word = first_word_before_space(&s2);

    println!("from ownership file: {}", word);


    fn first_word_before_space(s: &str) -> &str {
        let bytes = s.as_bytes();

        for (index, &item) in bytes.iter().enumerate() {
            if item == b' '{
                return &s[0..index];
            }
        }
        
        // return whole
        &s[..]
    }

    let a = [1, 3 ,5 , 7, 8];
    let slice = &a[0..2];
}