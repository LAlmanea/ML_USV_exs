
# Exercise 3

# Read file
x = read.csv("poisson.csv")
x = data.matrix(x)

# Lambda values
lambda = seq(from = 0.1, to = 50, by = 0.1)

# log-likelihood equation
log_likelihood = -n*lambda + log(lambda)*sum(x)-sum(log(factorial(x)))

# Plotting
plot(lambda, log_likelihood,"l", col = 'Blue')

# Plot a line for the max value for lambda
abline(v=sum(x)/n, col = "Red")


