fn solution(input: &str) -> u32 {
    let matrix: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
    let mut most_common = Vec::<char>::new();
    for x in 0..matrix[0].len() {
        let mut zeros = 0;
        for line in &matrix {
            println!("{} {}", line[x], line[x] == '0');
            if line[x] == '0' {
                zeros += 1;
            }
        }
        if zeros > matrix.len() - zeros {
            most_common.push('0');
        } else {
            most_common.push('1');
        }
    }
    let least_common_str = most_common
        .iter()
        .map(|c| if *c == '0' { '1' } else { '0' })
        .collect::<String>();
    let most_common_str = most_common.iter().collect::<String>();
    println!("Least common: {}", least_common_str);
    println!("Most common: {}", most_common_str);
    u32::from_str_radix(&least_common_str, 2).unwrap()
        * u32::from_str_radix(&most_common_str, 2).unwrap()
}

fn main() {
    let input = include_str!("../../inputs/day3.txt");
    println!("{}", solution(input));
}

#[cfg(test)]
mod tests {
    use crate::solution;

    #[test]
    fn test() {
        let input = "00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010";
        assert_eq!(solution(input), 198);
    }
}
