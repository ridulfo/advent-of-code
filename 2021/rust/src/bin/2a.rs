use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let cmds = input_str
        .lines()
        .map(|x| x.split_whitespace().collect::<Vec<_>>());

    let (mut pos, mut depth) = (0, 0);
    for line in cmds {
        let (dir, dist) = (line[0], line[1].parse::<i32>().unwrap());
        match dir {
            "forward" => pos += dist,
            "down" => depth += dist,
            "up" => depth -= dist,
            _ => panic!("Unknown command: {}", line[0]),
        }
    }

    println!("{}", pos * depth);
}
