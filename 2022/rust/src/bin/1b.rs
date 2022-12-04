use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let mut calories: Vec<u32> = input_str
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|line| line.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect();

    calories.sort();
    calories.reverse();

    println!("{}", calories.iter().take(3).sum::<u32>());
}
