trait Shape { 
    fn area(&self) -> f64;
}

struct Circle {
    radius: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64{
        std::f64::consts::PI * self.radius.powi(2)
    }
}

struct Rectangle {
    width: f64,
    height: f64,
}

impl Shape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

// Using Traits with Generics
// trait Shape<T> {
//     fn area(&self) -> T;
// }




fn main() {
    let circle = Circle { radius: 3.0};
    println!("The area ofthe circle is {}", circle.area())
}
