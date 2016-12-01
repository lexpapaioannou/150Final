file.df <-
  read.csv("C:\\Users\\apapaioannou\\Downloads\\outputFile.csv",
           header = TRUE)

file.df <- file.df[rowSums(is.na(file.df)) != ncol(file.df), ]

plot(file.df$Tst1, file.df$Test2)