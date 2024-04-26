function matchDigitOrName(input)
    local digitNames = {
        [0] = "zero",
        [1] = "one",
        [2] = "two",
        [3] = "three",
        [4] = "four",
        [5] = "five",
        [6] = "six",
        [7] = "seven",
        [8] = "eight",
        [9] = "nine"
    }

    -- Match a digit or its name using a pattern
    local digitOrName = input:match("(%d+)|(" .. table.concat(digitNames, "|") .. ")")

    return digitOrName
end

-- Test the function
print(matchDigitOrName("3"))     -- Should print "3"
print(matchDigitOrName("seven")) -- Should print "seven"
-- local count = 0
-- for line in io.lines("input1.txt") do
-- 	print(line)
-- 	local digits = {}
-- 	for digit in line:gmatch("(%d+|[onetwothreefourfive])") do
-- 		print(digit)
-- 		table.insert(digits, digit)
-- 	end
-- 	local number = table.concat({digits[1], digits[#digits]}, "")
-- 	print(number)
-- 	count = count + tonumber(number)
-- end





















-- local function part1 ()
-- 	local count = 0
-- 	for line in io.lines("input1.txt") do
-- 		print(line)
-- 		local digits = {}
-- 		for digit in line:gmatch("%d") do
-- 			table.insert(digits, digit)
-- 		end
-- 		local number = table.concat({digits[1], digits[#digits]}, "")
-- 		print(number)
-- 		count = count + tonumber(number)
-- 	end
-- 	return count
-- end
-- 
-- print(part1())
