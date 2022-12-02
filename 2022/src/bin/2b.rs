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
            let mut throw: u8 = 0;
            if b == 0 {
                match a {
                    0 => throw = 2,
                    1 => throw = 0,
                    2 => throw = 1,
                    _ => assert!(false),
                }
            } else if b == 1 {
                throw = a;
            } else {
                match a {
                    0 => throw = 1,
                    1 => throw = 2,
                    2 => throw = 0,
                    _ => assert!(false),
                }
            }

            acc += (throw + 1) as u32;
            if a == throw {
                acc += 3;
            } else {
                match (a, throw) {
                    (0, 1) | (1, 2) | (2, 0) => acc += 6,
                    _ => {}
                }
            }
            println!("{} {} {} {}", a, b, throw, acc);
            acc
        });
    println!("{:?}", games);
}

// 0 rock
// 1 paper
// 2 scissors
