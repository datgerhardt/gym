
enum Color {
    Red,
    Green,
    Blue
}
enum IP {
    V4(String),
    V6(String),
}

// Enums with Methods 
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

impl Shape {
    fn area(&self) -> f64 {
        match self { 
            Shape::Circle(r) => std::f64::consts::PI * r.powi(2),
            Shape::Rectangle(w, h) => w * h
        }
    }
}


fn main() {
    let color = Color::Green; 

    match color {
        Color::Red => println!("The color is red"),
        Color::Green => println!("The color is green"),
        Color::Blue => println!("The color is blue"),
    }

    // Enums with Associated Values
    let ip = IP::V4("192.168.0.1".to_string());
    match ip {
        IP::V4(s) => println!("IP address: {}", s),
        IP::V6(s) => println!("IP address: {}", s),
    }


    // Enums with Methods 
    let shape = Shape::Circle(5.0);
    println!("Area: {}", shape.area());

}
