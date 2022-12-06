const s = require("fs").readFileSync("inputs/day1.txt", "utf8");
const calories = s.split("\n\n").map((line) =>
  line
    .split("\n")
    .map((x) => parseInt(x))
    .reduce((acc, x) => acc + x, 0)
);

console.log(Math.max(...calories));
