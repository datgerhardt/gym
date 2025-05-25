fn main() {
    let result = add(5, 3);
    println!("Result: {}", result);

    let result = subtract(10, 4);
    println!("Result: {}", result);

    let result = multiply(7, 2);
    println!("Result: {}", result);

    let result = divide(9, 3);
    println!("Result: {}", result);
}


fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn subtract(a: i32, b: i32) -> i32 {
    a - b 
}

fn multiply(a: i32, b: i32) -> i32 {
    a * b 
}

fn divide(a: i32, b: i32) -> f64 {
    match b {
        0 => panic!("Cannot divide by zero"),
        _ => (a as f64) / (b as f64)
    } 
}

