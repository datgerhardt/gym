// mod foo;
// mod bar;

use tokio::prelude::*;

// fn main() {
//     println!("Hello, world!");
//     foo::foo();
//     bar::bar();
// }

async fn main() {
    // Create two tasks that run concurrently
    let handle1 = spawn(async move {
        println!("Task 1 finished");
    });

    let handle2 = spawn(async move {
        println!("Task 2 finished");
    });

    // Wait for both tasks to finish
    handles.await;
}