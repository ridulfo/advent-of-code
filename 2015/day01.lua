local path = "input01.txt"

local sum = 0
for line in io.lines(path) do
    local words = {}
    
    for word in line:gmatch("%d+") do
        table.insert(words, tonumber(word))
    end

    local l, w, h = unpack(words)

	sum = sum + 2*l*w + 2*w*h + 2*h*l + math.min(l*w, w*h, h*l)
end
print(sum)
