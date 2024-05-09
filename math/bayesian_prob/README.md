# bayesian probability

![Bayes Formula](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oKi6F9CNeCyhLajj_RRSoA.jpeg)

  [image source](https://towardsdatascience.com/what-is-bayes-rule-bb6598d8a2fd)

# Task 0

[This](https://stats.stackexchange.com/questions/181035/how-to-derive-the-likelihood-function-for-binomial-distribution-for-parameter-es) seems to be the liklihood formula

* We are likely multiplying the function's liklihood by binomial coefficient because "You can assume that `x` follows a binomial distribution.

basic idea you'll want to code:

* P(x = k) = \binom{n}{k} \times p^k \times (1-p)^{n-k}
  * \binom{n}{k} = \frac{n!}{k!(n-k)!}

# Task 1

Intersection = liklihood / Pr

# Task 2

Marginal Probability = sum of intersections

# Task 3

![Bayes Formula](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oKi6F9CNeCyhLajj_RRSoA.jpeg)

Posterior probability = (liklihood * `Pr`ior) / Marginal probability