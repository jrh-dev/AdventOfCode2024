input = readLines("d02_full.txt", warn = FALSE)

l = lapply(strsplit(input, " "), as.integer)


solve = function(allow_removal) {
  sum(
    unlist(
      lapply(l,  function(x){
          y = diff(x)
          if (all(y > 0 & y <=3) | all(y < 0 & y >= -3)){
            return (TRUE)
          } else if (allow_removal) {
            for (i in 1:length(x)) {
              y = diff(x[-i])
              if (all(y > 0 & y <=3) | all(y < 0 & y >= -3)) {
                return (TRUE)
              }
            }
            return (FALSE)
          }
        }
      )
    )
  )
}

print(paste("Part 1 answer: ", solve(FALSE)))
print(paste("Part 2 answer: ", solve(TRUE)))