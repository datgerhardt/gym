use std::thread;

// Concurrency
// Concurrent programming allows multiple tasks to execute simultaneously, improving overall system performance and responsiveness.

// Rust's Concurrency Model
// Rust uses a thread-safe concurrency model based on async/await. This allows us to write asynchronous code that is easy to read and maintain.

// Building Blocks of Concurrency
// Tasks: A task represents an execution unit in our program.
// Spawning tasks: We spawn new tasks using the std::thread module or by using async functions with the async/await syntax.
// Blocking

// Concurrency Techniques
// Parallelism: Execute tasks concurrently using threads or fibers.
// Cooperativity: Tasks cooperate with each other to achieve common goals.
// Asynchronous IO: Use async functions to perform I/O operations without blocking the program.

fn main() {
    // Create two threads that run concurrently
    let handle1 = thread::spawn(move || {
        for i in 0..10 {
            println!("Thread 1: {}", i);
        }
    });

    let handle2 = thread::spawn(move || {
        for i in 0..5 {
            println!("Thread 2: {}", i);
        }
    });

    // Wait for both threads to complete
    handle1.join().unwrap();
    handle2.join().unwrap();
}