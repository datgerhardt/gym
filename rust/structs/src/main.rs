// Struct

struct Person {
    name: String,
    age: u32,
}

// Defining Methods on Structs

impl Person {
    fn greet(&self) {
        println!("Hello, my name is {}!", self.name);
    }
}

// Tuple Structs 

struct Point(u32, u32);

fn main() {
    let person = Person {
        name: "John".to_string(),
        age: 30,
    };
    
    println!("Name: {}", person.name);
    println!("Age: {}", person.age);

    person.greet();


    let point = Point(1, 2);

    match point {
        (x, y) => println!("X: {}, Y: {}", x, y),
    }
}
