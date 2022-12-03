use std::collections::HashSet;

use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let chars = input_str
        .lines()
        .map(|line| {
            let (sec1, sec2) = (&line[0..line.len() / 2], &line[line.len() / 2..]);
            sec1.chars()
                .collect::<HashSet<_>>()
                .intersection(&sec2.chars().collect::<HashSet<_>>())
                .map(|c| *c)
                .map(|c| {
                    if c.is_uppercase() {
                        c as u16 - b'A' as u16 + 27
                    } else {
                        c as u16 - b'a' as u16 + 1
                    }
                })
                .sum::<u16>()
        })
        .sum::<u16>();
    println!("{:?}", chars);
}
