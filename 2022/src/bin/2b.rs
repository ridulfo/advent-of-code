use aoc::input::read_stdin;
fn main() {
    fn to_win(opponent: u8) -> u8 {
        match opponent {
            0 => 1,
            1 => 2,
            2 => 0,
            _ => unreachable!(),
        }
    }
    fn to_lose(opponent: u8) -> u8 {
        match opponent {
            0 => 2,
            1 => 0,
            2 => 1,
            _ => unreachable!(),
        }
    }
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
            let throw = match b {
                0 => to_lose(a),
                1 => a,
                2 => to_win(a),
                _ => unreachable!(),
            };

            acc + (throw as u32 + 1)
                + match (a, throw) {
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
