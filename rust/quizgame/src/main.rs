use std::io;

fn main() {
    let mut score = 0; // add mut to make variable mututable  

    loop {
        println!("Welcome to the quiz game!");
        println!("Do you want to play? (yes/no)");

        let mut input = String::new();
        if std::io::stdin().read_line(&mut input).is_err(){
            println!("Error reading input.");
            break;
        }


        println!("{}", input.trim());
        if input.trim() == "yes"{
            loop {
                println!("What's your question?");
                let mut question = String::new();
                if io::stdin().read_line(&mut question).is_err() {
                    println!("Error reading question.");
                    break;
                }

                if !question.contains("answer") {
                    println!("Invalid question. Try again.");
                    continue;
                } else {
                    // Parse the answer
                    let mut parts = question.split_whitespace();
                    if let Some(answer) = parts.next() {
                        match answer.parse::<i64>(){
                            Err(_)=> println!("Invalid answer. Please enter a number."),
                            Ok(answer) => {
                                score += 1;
                                println!("Correct! You got it right.");
                            }
                        }
                    } else {
                        println!("Invalid question format. Try again.");
                    }

                    break;
                }
            }
        } else if input.trim() == "no" {
            println!("Thanks for playing!");
            break;
        } else {
            println!("Invalid answer. Try again.");
        }
        break;
        

    }
}
