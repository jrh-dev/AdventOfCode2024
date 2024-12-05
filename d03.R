
library(stringr)

s = readLines("./d03_full.txt", warn = FALSE)
p = "mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don\\'t\\(\\)"

myprod = function(x) {if (length(x)==0) {0} else {prod(x)}}

solve = function(input, pattern, conditional) {
  total = 0
  run = TRUE
  for (i in unlist(str_extract_all(input, pattern))) {
    if (i == "don't()" & conditional) {
      run = FALSE
    } else if (i == "do()" & conditional) {
      run = TRUE
    } else if (run) {
      total = total + myprod(as.integer(unlist(str_extract_all(i, "\\d+"))))
    }
  }
  return (total)
}

print(paste("Part 1 answer: ", solve(s, p, FALSE)))
print(paste("Part 2 answer: ", solve(s, p, TRUE)))