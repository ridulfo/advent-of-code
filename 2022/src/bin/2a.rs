use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let games = input_str
        .lines()
        .map(|line| {
            [
                line.chars().nth(0).unwrap() as u8,
                line.chars().nth(2).unwrap() as u8,
            ]
        })
        .map(|[a, b]| [a - b'A', b - b'X'])
        .fold(0, |acc: u32, [a, b]| {
            acc + (b as u32 + 1)
                + match (a, b) {
                    (0, 1) | (1, 2) | (2, 0) => 6,
                    (0, 0) | (1, 1) | (2, 2) => 3,
                    _ => 0,
                }
        });
    println!("{:?}", games);
}

// 0 rock
// 1 paper
// 2 scissors
