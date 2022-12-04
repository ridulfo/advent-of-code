use aoc::input::read_stdin;
fn main() {
    let input_str = read_stdin();
    let cmds = input_str
        .lines()
        .map(|x| x.split_whitespace().collect::<Vec<_>>());

    let (mut pos, mut depth, mut aim) = (0i64, 0i64, 0i64);
    for line in cmds {
        let (dir, dist) = (line[0], line[1].parse::<i64>().unwrap());
        match dir {
            "forward" => {
                pos += dist;
                depth += aim * dist;
            }
            "down" => aim += dist,
            "up" => aim -= dist,
            _ => panic!("Unknown command: {}", line[0]),
        }
    }

    println!("{}", pos * depth);
}
