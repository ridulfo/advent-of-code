use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let calories: Vec<u32> = input_str
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|line| line.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect();
    println!("{}", calories.iter().max().unwrap());
}
