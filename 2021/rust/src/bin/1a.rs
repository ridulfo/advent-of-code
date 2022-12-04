use aoc::input::read_stdin;
fn main() {
    let l = read_stdin()
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let count = l.windows(2).map(|w| w[0] < w[1]).filter(|&x| x).count();
    println!("{}", count);
}
