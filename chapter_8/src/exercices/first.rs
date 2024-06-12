pub fn mean(){
    let numbers = vec![1,3 , 5 ,6 ,7 ,89];

    let count = numbers.len();
    let mut sum = 0;
    for &i in &numbers{
        sum += i;

    }    

    let mean = sum as f64 / count as f64;

    println!("mean is :{}", mean);

}


pub fn median(numbers: &mut Vec<i32>) -> f64{
    numbers.sort();

    let len = numbers.len();

    if len == 0{
        panic!("Cannot compute median");
    }

    if len % 2 == 0 {
        let middle_index = len / 2;
        let middle_value = (numbers[middle_index - 1] + numbers[middle_index]) as f64 / 2.0;

        middle_value
    }
    else{
        numbers[len / 2] as f64
    }
}