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
        .fold(0, |mut acc: u32, [a, b]| {
            acc += (b + 1) as u32;
            if a == b {
                acc += 3;
            } else {
                match (a, b) {
                    (0, 1) | (1, 2) | (2, 0) => acc += 6,
                    _ => {}
                    
                }
            }
            acc
        });
    println!("{:?}", games);
}

// 0 rock 
// 1 paper
// 2 scissors