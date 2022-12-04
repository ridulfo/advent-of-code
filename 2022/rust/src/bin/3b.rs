use std::collections::HashSet;

use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let chars = input_str
        .lines()
        .collect::<Vec<_>>()
        .chunks_exact(3)
        .into_iter()
        .map(|line| {
            let (sec1, sec2, sec3) = (
                &line[0].chars().collect::<HashSet<_>>(),
                &line[1].chars().collect::<HashSet<_>>(),
                &line[2].chars().collect::<HashSet<_>>(),
            );
            sec1.intersection(sec2)
                .map(|c| *c)
                .collect::<HashSet<_>>()
                .intersection(sec3)
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
