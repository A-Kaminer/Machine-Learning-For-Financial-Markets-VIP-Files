# Week 3 (January 23 - January 29)

## 1/24/23

[This](https://github.com/gabors-data-analysis/da-coding-python) seems
very helpful. I think I'll spend some time with it to pick up some of
the ML and stats that I'm missing.

### Poking Around Research Topics and Papers (5 hours)

Looking at the power point from last week's presentation, and a lot of
the possible directions look like they have very obvious answers, as
long as you are fast enough. For instance, when an analyst forecast
changes, obviously the price will change to reflect that. That's 
pretty obvious. You just have to be fast enough to take advantage,
which is pretty impossible because of the HFT firms and insider 
trading.

**Possible Research Topics:**
- Hedge Fund Trading
- CEO Changes
- Share Repurchase
- IPO
- Operational Risk
- Cybersecurity
- Supply Chain Disruption
- Reaction to Monetary Policy

These are the topics that stick out the most to me as both interesting
and not too over-explored (hopefully).

**[Hedge Fund Activism, Corporate Governance, and Firm Performance](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.2008.01373.x)**

- Suggest that mutual and pension funds fail in activist investing
- Hedge Funds succeed in generating benefits for shareholders through
activist investing
- Hedge fund managers are better able to act as informed monitors
- Target value firms (low market cap relative to assets)
- Targets usually have high institutional ownership
- Market reacts favorably to activism
- Schedule 13D must be filed within 10 days of acquiring >= 5% voting stake
- significant positive response to targeting sale of company or 
changes in business strategy
- no positive response to structure-related and governance activism
- higher returns from hedge funds with history of activism & with 
funds that initiate with aggressive tactics
- activist hedge funds hold for a median of 20 months
- hedge fund activism is not kind to senior management
- increases CEO turnover rate by 10%
- decreases CEO salary by 1 million
- the authors think it is fine and doesn't need aggressive regulation
- activist institutional investing originated in the 80s
- any institution availbable to the public can't do it
- **Collected data by:**
    - Buying a list of all 13D filers from 2001 to 2006
    - Manually filtered down to hedge funds
    - Exclude events where
        1. The primary purpose is to deal with bankruptcy
        2. The primary purpose is M&A related risk arbitrage (idk)
        3. The target is a closed-end fund or other irregular 
        corporation
    - Reduces down to 236 hedge funds with 1032 events total
    - Conduct manual news searches in Factiva to find motives
    - To add in non 13D activism (on large caps), they used news sources
- End up with 236 activist funds with 1059 fund-target pairs involving
882 unique target companies.
- **Examples of Activist Events**
    - MLF and Alloy, Inc
        - 2003
        - MLF Investments acquires 5.8% of Alloy, Inc
        - MLF wanted to support restructuring and wanted to split the 
        company in 2.
        - They talked to management and the Board of Directors
        - After a year Alloy appointed the managing partner of MLF to
        the board
        - The fund smoothly exited in 2007
        - Not hostile
    - Pirate Capital and James River Coal
        - Acquired 8% stake in 2006
        - Hostile to management
        - Demanded that the board retain an investment banking firm to
        be in charge of strategy and they redeem the shareholder 
        rights plan
        - Management hired Morgan Stanley
        - Stock price rose 10% in a day
        - Basically a takeover
- **Typical Stated Activist Fund Objectives**
    1. Fund believes company is undervalued and that the fund can help
    management maximize shareholder value. (48.3% of sample, 
    nonagro, nonspecific)
    2. Activism targeting firms' payout policy and capital structure.
    Subgroups:
        1. Fund proposes changes geared toward the reduction of 
        excess cash, increase in firm leverage, or dividends/stock
        repurchases. (Why would they want to increase leverage??)
        2. Equity issuance (reducing seasoned equity offerings or 
        debt restructuring)
    3. Activism targeting business strategy. Subgroups:
        1. General operational efficiency
        2. Spin off divisions or refocus business strategy
        3. Messing with pending merger/acquisition
        4. May make proposals for the target to better pursue growth
        strategy
    4. Activism urging sale of target
        - Fund attempts to force a sale of a target
        - Usually to a third party but sometimes to the fund itself
    5. Activism targeting governance. Subgroups:
        1. Rescind takeover defense (declassify boards or 
        rescind poison pills)
        2. Oust CEO/chairman
        3. Challenge board independence/fair representation
        4. To demand more information disclosure and question 
        potential fraud
        5. Challenge executive comp
- The success rate of activism across objectives varies alot
- Aggregated, 40.6% achieve success and 25.8% achieve partial success
- 21.4% of the time, the fund fails
- ISS often recommends a vote in favor of hedge funds
- Fund should only resort to aggressive tactics when benefit of 
activism is higher
- About 20% of the time, unafilliated hedge funds file as a group
- "wolf pack"
- There is often a cascade of outside investors coming to freeload
- Multiple fund filing groups usually take larger stakes in the target
 and are more likely to employ hostile tactics
- Companies accomodate activists 30% of the time
- Negotiate 30% of the time
- Fight 40% of the time
- Hostile interventions usually take more stake than not hostile
- Can't find exit info for ~half of the sample.

This is where I ended the day (page 23). Holy moly this stuff is dense. I think
I'm learning things though, and after reading this paper I think I know what I
want to do. If a model could predict with a reasonable degree of accuracy what
companies are likely to be targeted by activist investors in the near future,
they could take long positions on those companies and make outsized(probably not)
returns. The paper talked about probit models, which seems like the way to go
with this, as being targeted is a binary thing.

## 1/25/23

### Research Proposal (1.5 hours)
I haven't finished the research paper yet, but I think I have enough of an idea
of what I want to do on my research proposal. My idea is to somehow model and
predict whether or not a firm will become a target of activist investing. 
There should be all sorts of quantitative and qualitative factors to suggest
that. I wrestled with LaTeX for a little while, but I think I'm content with
the proposal. The research paper can be found [here.](../Assignment-0/Kaminer-Predicting-Activist-Investing.pdf)
I'm glad to have a working proposal done. I just need to get the actual coding
project done.

### Coding Assignment (1 hour)
I finally got back around to the coding assignment, now that I could look at
some people's questions. Turns out the output that I thought was nonsense using
numpy was actually right rip. Oh well. I ended up using statsmodels api. It was
actually very easy. The code can be found [here.](../Assignment-0)

### Answering Questions (.5 hours)
I answered a couple of people's questions over teams, and it felt great to 
actually be able to contribute something. It also made me much more confident
in my ability to survive and thrive in this VIP.

### Things I want to do in the near future:
- [x] Go through some of the modules in the data analysis python course (Multiple done)
- [ ] Finish the research paper I was reading

## 1/27/23

### Meeting with Chan Woo Kim Notes (.75 hours)
Meeting went well. Talked about all sorts of things related to the VIP and 
fintech but also just classes in general. Networking is always good.

### PACE Session (4 hours)
The session was very boring, but I got it over with. I learned a little bit 
about git, but the stuff I wanted to learn about was at the very end of the
lecture and we had to rush through it. The lecturer dropped his cheat sheet.
Very helpful: [Cheat Sheet](https://github.com/shahagam4/technical-notes/blob/main/git_cheatsheet.md). 
He also dropped his slides. [Slides](https://gtvault-my.sharepoint.com/personal/rrahaman6_gatech_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Frrahaman6%5Fgatech%5Fedu%2FDocuments%2FDocuments%2Fgit%5Fbootcamp%5Fspring%5F2022%2FMS%20QCF%20Git%20101%20Summer%202022%2Epdf&parent=%2Fpersonal%2Frrahaman6%5Fgatech%5Fedu%2FDocuments%2FDocuments%2Fgit%5Fbootcamp%5Fspring%5F2022&ga=1)

Going back up his github tree I can see a whole folder of technical notes [here.](https://github.com/shahagam4/technical-notes)

**Things to Learn More About:**
- [ ] Git branches and all of that junk
- [ ] All of the fancy git log parameters
- [ ] Pull requests

