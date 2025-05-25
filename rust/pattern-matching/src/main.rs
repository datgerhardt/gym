
struct Person {
    name: String,
    age: u32,
}

fn main() {

    // Pattern Matching 
    let x = 5;
    match x {
        1 => println!("x is 1"),
        2 => println!("x is 2"),
        _ => println!("x is something else"),
    }

    // struct pattern matching 
    let person = Person {name: "John".to_string(), age: 30};
    match person {
        Person {name, age}  => println!("Name is {}", name),
        Person {age, ..} => println!("Age is {}", age),
    }

}
