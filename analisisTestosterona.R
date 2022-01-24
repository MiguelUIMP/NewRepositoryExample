# PROBLEMA 1
datos <- scan("./test.txt")

# i)
mu <- 600

plot(datos, pch=19, xlab="ciclistas", ylab="testosterona (ng/dL)")
abline(h=mu, col="red")