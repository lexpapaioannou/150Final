file.df <-
  read.csv("C:\\Users\\apapaioannou\\Downloads\\outputFile.csv",
           header = TRUE)
labels <- read.table("C:\\Users\\apapaioannou\\Downloads\\graphLabels.txt")

file.df <- 
  file.df[rowSums(is.na(file.df)) != ncol(file.df), ]

jpeg(file = "Rplot.jpg")

plot(x = file.df[, 1],
     y = file.df[, 2],
     main = "Python Graph",
     xlab = labels[1, 1],
     ylab = labels[2, 1],
     type = 'l'
)

graphics.off()

dev.off
