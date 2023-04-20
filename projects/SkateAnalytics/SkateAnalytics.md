---
title: Skate Analytics
summary: Towards a way of recording, analyzing, and visualizing data about skateboarding trick attempts and a skateboarder's likelihood of landing a trick. Progression (or regression), visualized!
---

Towards a way of recording, analyzing, and visualizing data about skateboarding trick attempts and a skateboarder's likelihood of landing a trick. Progression (or regression), visualized!

# Current Status
Disorganized: Lots of disparate notes that need to compiled and ironed out, some code and visuals

Could likely benefit from compiling everything in one place and being more structured in how it's presented or different concerns are sufficiently separated out

# History
Originally I was interested in how you might be able to bet on and against yourself as a way of estimating the probability of doing a trick. (So the prior data came first.) I got this idea while reading *Bayesian Statistics the Fun Way*, which showed me how similar data can be used to estimate probabilities.

I started to collect the Outcome data after I realized that I'd want to be able to check the accuracy of my bets against data that was kinda more real/less open to interpretation (especially as my understanding of this domain of statistics was so shaky).

---

One thing to remember when analyzing this data is always that the analyses pertain to the tricks that have been recorded. Not all tricks get recorded, and, so long as trick attempts aren't selectively recorded, that's OK.

# Data Viz
- Add a column for prior probability (treat blank odds as null), average this by Trick and/time periods, convert average to nearest 1/N and get the fraction for this - use the numerator and the denominator to get `a` and `b` for the beta dist from `a = numerator` and `b = denominator - numerator` - and plug those into the beta function to produce the posterior dist (we can aggregate the outcomes to make the `a` and `b` values)
- A good reference for working with Beta dist in R; use the ggplot2 geom_density with the function dbeta to show perfect functions on a single time period (though you could facet on time periods and have it stack vertically) — for the ridge plots it will have to use rbeta, which randomly samples from the beta dist and generates a lumpy distribution unless you have a high sample rate https://www.causact.com/the-beta-distribution.html
- A good general reference for the various beta functions: https://www.geeksforgeeks.org/compute-beta-distribution-in-r-programming-dbeta-pbeta-qbeta-and-rbeta-functions/

- [ ] Ridge plot for skating distributions https://www.datanovia.com/en/blog/elegant-visualization-of-density-distribution-in-r-using-ridgeline/
	- [ ] The Y value is the value to split the distributions by (across different lines, like the group value in regular plots), while the X value contains the probability readings that we took when sampling from each distribution
	- [ ] look into how to group dates by week / month
		- [ ] how might you fill in lines for weeks / months that are missing (gaps in the data)?
	- [ ] For each week/time period, produce an rbeta set of data points and append them to a variable (dataset) with the relevant values as metadata (trick name, time period)
	- [ ] Group by Trick, then Date (Week/Month)
		- [ ] Reformat date as Week, with `lubridate`: https://community.rstudio.com/t/visualize-by-week-number-and-year/9248/4
	- [ ] Facet wrap on Trick to see ridge plots side by side for each trick
	- [ ] http://cran.nexr.com/web/packages/ggridges/vignettes/introduction.html
- Gallery: https://cran.r-project.org/web/packages/ggridges/vignettes/gallery.html
	- The second dist on each layer seems to be determined when you set an aesthetic property equal to the variable that you want to split out
		- the dist data would need to be in the same x variable for all instances we'd want to break into separate dists; we just keep track of which one it is via another variable, like Political Party

# Metadata
[[SkateAnalytics]]: trick modifiers like Fakie, Switch, and 360. Fakie and Switch are mutually exclusive, but Fakie and 360 are not. At the basic level, adding these modifiers can be like assigning qualities to a beer in Untappd.
- People that are interested in what is essential to do this and to do it themselves.
- Runs are a string of tricks. FS 5050, FS 180 out = FS 5050 followed by a FS 180 off of a grind object (ledge, rail, bench - categories of things that have a weight-bearing platform (bench or ledge) or do not have them (rail, chain)).
	- Sessions are a set of tricks (and runs, which are themselves sets of tricks) that are usually restricted to a certain time frame, location, and obstacle or set of obstacles.
		- To what degree is the flat ground an obstacle? I guess it is since we tend to talk about "flatground" tricks, but often enough I've thought about it as the default position, a baseline against which all else is compared, a 0 to all others' -1 or +1.
		- Can one "use" the (flat)ground? I imagine that within a run you could jump from one ledge to the ground and use it in some determined way before jumping onto the next ledge. Very stylistic and betraying a thought process, a presence of decisions and determination.
- Most people likely wouldn't be interested in the theory behind the project, and that's ok, but it's sort of a key motivator for me.
- [ ] A way to save an attempt and then quickly fill out another attempt for the same trick (maybe have it default to the same odds, but allow them to be edited).
- [ ] Interface to retroactively assign formal names to tricks, as doing so in the moment is slow and tedious.
- [ ] Ridgeline plots


# compared to other offerings
The app for the Fitbit for Skateboards: competitive inclination

# Possible features
- Bets (Success & Fail, which are the odds in favor)
- Direct Probability estimates (instead of via Bets)
- outcome

# Research Directions
Test whether Bets or Direct Probability (I no longer remember what I meant by this latter term; was it a relabelling of the first term, Bets, or something different?) surveys provide more accurate estimates of [[Trick Success Probability]].

https://www.causact.com/the-beta-distribution.html

For the priors,
Test whether averaging a trick's `a` and `b` values and then directly plugging those into the Beta dist functions seems more accurate than the process of converting each record to a probability, averaging that, then turning it into N-based a and b values that get plugged in to the beta dist function.

Look at how bets tend to move slowly from an initial bet (initial bet being like 1/3 and only gradually moving to more confidence like 2/3). Figure out what one should expect. (This is a bit more noticable when there's been a gap in entries --- due to either not recording at all and/or not doing that trick (either could cause this if one hasn't been thinking in terms of the priors for a trick while skating and not recording (not recording would prompt one to think of the priors/bets) or by not doing the trick in a while one's confidence positively or negatively might have disappeared (in terms of the steepness of their prior dist, their degree of confidence))).