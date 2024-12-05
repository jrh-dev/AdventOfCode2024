
input = readLines("d01_full.txt", warn = FALSE)

l = as.integer(unlist(strsplit(input, "   ")))
lhs = sort(l[seq_along(l) %% 2 != 0])
rhs = sort(l[seq_along(l) %% 2 == 0])

p1 = sum(abs(lhs-rhs))

p2 = 0

for (i in lhs) {
  p2 = p2 + (i * length(rhs[rhs==i]))
}

print(paste("Part 1 answer: ", p1))
print(paste("Part 2 answer: ", p2))