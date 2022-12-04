fn main() {
    let test = "2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8";
    let input_str = include_str!("../../inputs/day4.txt");
    let mut count = 0;
    for line in input_str.lines() {
        let mut ranges = line
            .split(|c| c == '-' || c == ',')
            .map(|num| num.parse::<u8>().unwrap());
        let (a1, a2, b1, b2) = (ranges.next(), ranges.next(), ranges.next(), ranges.next());
        let (a_range, b_range) = (a1..=a2, b1..=b2);
        if a_range.contains(&b1) && a_range.contains(&b2) {
            count += 1;
        }
        if b_range.contains(&a1) && b_range.contains(&a2) {
            count += 1;
        }
    }
    println!("{:?}", count);
}
