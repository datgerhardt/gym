fn main() {
    let mut x = 10; // x owns an integer value

    // borrow x for reading 
    let y = &x;
    println!("{}", y); // prints the value of x without moving it
    
    // The Three Rules of Ownership
    // 1. Each value has an owner: The variable itself is the owner.
    // 2. Every value has a copy: Even if no explicit copy is made, Rust creates a new copy when a variable is moved into another scope.
    // 3. You cannot move a value while it's being borrowed: This ensures that borrowing and moving don't happen simultaneously.
    

    // move x to y 
    let z = std::mem::take(&mut x); //takes ownship from x
    // println!("{}", x); // after taking ownership you cannot access the viariable
    // println!("{}", y);
    println!("{}", z);

}
