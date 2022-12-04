use std::io::{self, Read};

/**
 * Reads from stdin and returns a string.
 */
pub fn read_stdin() -> String {
    let mut buffer = String::new();
    let result = io::stdin().read_to_string(&mut buffer);
    match result {
        Ok(_) => buffer.trim().to_string(),
        Err(_) => panic!("Failed to read from stdin"),
    }
}
