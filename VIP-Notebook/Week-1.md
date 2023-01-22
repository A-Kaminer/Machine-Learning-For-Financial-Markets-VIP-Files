# Week 1 (January 16 - January 22)

## 1/19/23

### Working on initial assignment

I spent about an hour working on the coding assignment. It's tricky because I 
have no idea how the statistics work. Lots of unfamiliar letters and words.
I'm familiar with numpy at least so hopefully it won't be too bad. Unfortunately
I can't get my code to do what I want it to do, so I'm taking a break. Here's
a look at what I currently have:

```python
    import numpy as np


    alpha = 3
    delta = -2
    lam = 0.5
    N = 10000
    np.random.seed(0)

    A = np.zeros(shape=(N, 3))
    b = np.zeros(shape=(N, 1))

    for i in range(N):

        x1 = np.random.normal(0,1)


        epsilon = np.random.uniform(-1, 1)
        x2 = alpha + (.2 * x1) + epsilon

        y = delta + (1.2 * x1) + np.random.exponential(lam)

        A[i] = [delta, x1, x2]
        b[i] = [y]

    x = np.linalg.lstsq(b, A)

    print(f"{A}\n\n{b}\n\n{x}")
```

It doesn't work at all lol. The link to the current code is [here](https://github.com/A-Kaminer/Machine-Learning-For-Financial-Markets-VIP-FIles/tree/master/Assignment-0)

**Total hours today: 1**

# 1/22/23

### Getting familiar with the XBLR dataset

I just watched an hour-long video on this dataset. Some key takeaways:
1. I'm probably going to mostly use the python api
2. There will be lots of problems with cleaning data and dealing with 
inconsitencies
3. There are lots of tools available for the dataset
4. Levels of access can vary depending on how my account is set up, usually by
rate limits on what I can request
5. The levels of rawness of the dataset vary.
6. This should probably by number 1. The XBLR dataset is a set of data that
the SEC forces companies to publish in a specific format. This format lends
itself to databases and research and such.

This dataset seems very useful for research. I'm spending some time looking
through it, and there are way too many tags. It's going to be quite a ride to
figure out what we want to get out of this dataset. It's kind of odd to think
that I'm looking at a dataset that theoretically contains the key to the perfect
trading strategy hidden somewhere inside of it. Someone just has to find it.
Of course, the market is perfectly efficient, so who knows if that's true.
Oh well. I'm just spewing my thoughts on to paper (keyboard?).

I put some of the trading club resources in the microsoft teams chat today. 
Hopefully people appreciate them/ find benefit from them. I need to read 
through some of them myself in order to figure out what on earth is going on
with this VIP hehe.

I also started my notebook today. You are reading it right now lol. Found a 
cheat sheet that's pretty helpful. [Here](https://www.markdownguide.org/cheat-sheet/)
There's also this useful tool for testing markdown locally [here](https://github.com/joeyespo/grip).
Pretty easy to work with.

**Total hours today: 3**
