# INF3104: Data Science Foundations (Fall 2026)

- Instructor: Rohan Alexander, rohan.alexander@utoronto.ca
- Class: Fridays, 10am to 1pm
- Class repo: https://github.com/RohanAlexander/inf3104

## Overview

Quantitative approaches have a common concern: how can others be confident that our statistical models have been brought to bear on appropriate datasets? This course focuses on the "data" of data science. It develops an appreciation for the many ways in which dealing with a dataset can get out of hand, and establishes approaches to ensure data science is conducted in ways that engender trusted findings. It touches on statistical modeling, but focuses on everything that comes before and after modeling, and in doing so ensures that modeling and analysis are placed on a firmer foundation.

The 12-week semester is broken into three parts, each of four weeks.
So the normal cadence of class is three weeks of learning and then in the fourth week you will submit an assignment on the Wednesday, and complete an in-class exam on the Friday.

- Part 1 (Weeks 1-4): Foundations: *You will set up a reproducible workflow and use it to write a short paper from real data. We will use this motivation to learn to use uv, Python, R, Git and GitHub, GitHub Actions, and Quarto, to make graphs and tables, and to write clearly.*
- Part 2 (Weeks 5-8): Data: *You will either take a government-run survey apart, or turn a table in a scanned PDF into a tested, documented, dataset, and then write a paper about it. We will use this motivation to learn about measurement, censuses, and sampling; to gather data from APIs, websites, and PDFs; to run experiments and surveys; and to clean, test, document, store, and share a dataset.*
- Part 3 (Weeks 9-12): Exploring and modeling: *You will write an original paper that uses a model to tell a story with data. We will use this motivation to learn exploratory data analysis, linear and generalized linear models, and how to turn model estimates into quantities that a reader can understand.*

You are welcome to use R, Python, or a combination throughout.

## Assessment

| Component | Weight |
|:---|---:|
| Part 1: Donaldson paper and oral defence about the paper I | 25+5 |
| Part 2: Data paper and oral defence about the paper II | 25+5 |
| Part 3: Final paper and oral defence III | 25+5 |
| Classic paper in-class presentation | 10 |

### Notes

- Your mark for each Part is the sum of your paper and your defence mark.
- Most weeks with a lecture begin with a quiz on the previous week's readings and class.
- Due dates:
    - Part 1: Assignment due Wednesday 7 October and then we'll use some of class time on Friday 9 October for the defence.
    - Part 2: Assignment due Wednesday 4 November and then we'll use some of class time on Friday 9 October for the defence.
    - Part 3: Assignment due Wednesday 9 December and then we'll arrange orals on 11 December.
    - Classic paper: Make a PR to the class repo (https://github.com/RohanAlexander/inf3104) by EOD Wednesday before class in the week of your paper (Week 3, 5, 6, or 7).
- Team size:
    - For Assignment I please work individually.
    - For Assignment II, please work in teams of one to four.
    - For Assignment III, please work individually.
    - Classic paper presentations: Please work individually.
- Details:
    - Assignment I is the [Donaldson paper](https://tellingstorieswithdata.com/25-papers.html#sec-paper-one).
    - For Assignment II you can pick one of two papers depending on your interest:
        - The [Howrah paper](https://tellingstorieswithdata.com/25-papers.html#sec-paper-three).
        - The [Dysart paper](https://tellingstorieswithdata.com/25-papers.html#sec-paper-four).
    - Assignment III is the [Final paper](https://tellingstorieswithdata.com/25-papers.html#sec-final-paper).
    - For the classic paper presentation please make 20 minutes of content on the assigned reading (Donoho, 2017; Neyman, 1934, Sections I, III, and V; Fisher, 1935, Chapter 2; Wickham, 2014). You should create slides using Quarto.


## Schedule

### Part 1: Foundations

#### Week 1 (starts Monday 7 September)

*Telling stories with data; the plan, simulate, acquire, explore, share workflow; Python set-up with uv; version control with Git and GitHub; and GitHub Actions.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, Chapters [1](https://tellingstorieswithdata.com/01-introduction.html), [2](https://tellingstorieswithdata.com/02-drinking_from_a_fire_hose.html), and [3](https://tellingstorieswithdata.com/03-workflow.html).
    - De Angelis, Inessa, 2026, "Using GitHub Actions for Computational Communication Research", [10.31235/osf.io/uqf6n_v1](https://doi.org/10.31235/osf.io/uqf6n_v1).
    - Bryan, Jennifer, 2018, "Excuse Me, Do You Have a Moment to Talk About Version Control?", *The American Statistician*, [10.1080/00031305.2017.1399928](https://doi.org/10.1080/00031305.2017.1399928).
    - Wilson, Greg, et al., 2017, "Good enough practices in scientific computing", *PLOS Computational Biology*, [10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510).
- Class (Friday 11 September)
    - (Housekeeping) Set up uv, Python, R, RStudio, VS Code, and GitHub.
    - (Lecture) Workflow and version control.
    - (Demonstration) Simulate, download, clean, and explore the Toronto shelter data; set up and run GitHub Actions daily to gather it.
    - (Worksheet) Git and GitHub; a PR to the class repo.

#### Week 2 (starts Monday 14 September)

*Using Quarto to make papers, slides, and websites; making graphs and tables with R; deploying with GitHub Pages; reading and cleaning data with polars; reading and writing Parquet files; version control in groups: PRs, reviews, conflicts.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, [Chapter 5](https://tellingstorieswithdata.com/05-graphs_tables_maps.html).
    - Healy, Kieran, 2026, *Data Visualization: A Practical Introduction*, [Chapter 1](https://socviz.co).
    - Timbers, Tiffany A., Joel Ostblom, Florencia D'Andrea, Rodolfo Lourenzutti, and Daniel Chen, 2025, *Reproducible and Trustworthy Workflows for Data Science*, (the version control chapters), https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/.
- Class (Friday 18 September)
    - (Quiz) Week 1 readings and class.
    - (Lecture) What makes a graph bad: taste, data, perception.
    - (Demonstration) Quarto; polars and Parquet on the shelter data; ggplot2 and tinytable.
    - (Worksheet) Build a website with Quarto and deploy it with GitHub Pages.

#### Week 3 (starts Monday 21 September)

*Writing papers.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, [Chapter 4](https://tellingstorieswithdata.com/04-writing_research.html).
    - King, Stephen, 2000, *On Writing*, pp. 111-137.
    - Zinsser, William, 1976, *On Writing Well*, pp. 6-32 and 169-177.
    - King, Gary, 2006, "Publication, Publication", *PS: Political Science & Politics*, [10.1017/S1049096506060252](https://doi.org/10.1017/S1049096506060252).
    - Mensh, Brett, and Konrad Kording, 2017, "Ten simple rules for structuring papers", *PLOS Computational Biology*, [10.1371/journal.pcbi.1005619](https://doi.org/10.1371/journal.pcbi.1005619).
- Class (Friday 25 September)
    - (Housekeeping) Pick classic papers and dates.
    - (Quiz) Weeks 1 and 2 readings and class, and what the Donaldson paper expects.
    - (Lecture) Features of good writing by section: title, abstract, introduction, data, model, results, discussion.
    - (Worksheet) Draft a paper from three sets of results and then edit three drafts.
    - (Worksheet, 30 min) Referee one of the example Donaldson papers: is it any good, and how do you know?
    - Donaldson paper questions.

#### Week 4 (starts Monday 28 September)

- No class

### Part 2: Data

#### Week 5 (starts Monday 5 October)

*Measurement: instruments, units, validity, reliability, and measurement error; missing data; data are not neutral; censuses and other official statistics; sampling: target population, frame, and sample; simple random, systematic, stratified, and cluster sampling; non-probability samples; simulating a sampling design to see what it does.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, [Chapter 6](https://tellingstorieswithdata.com/06-farm.html).
    - Statistics Canada, 2023, *Guide to the Census of Population, 2021*, Chapter 9, https://www12.statcan.gc.ca/census-recensement/2021/ref/98-304/98-304-x2021001-eng.pdf.
    - Bowley, Arthur Lyon, 1913, "Working-Class Households in Reading", *Journal of the Royal Statistical Society*, [10.2307/2339708](https://doi.org/10.2307/2339708).
    - (Classic) Neyman, Jerzy, 1934, "On the Two Different Aspects of the Representative Method: The Method of Stratified Sampling and the Method of Purposive Selection", *Journal of the Royal Statistical Society*, [10.2307/2342192](https://doi.org/10.2307/2342192). Sections I, III, and V only (pp. 558-561, 567-573, and 585-589).
    - (Classic) Donoho, David, 2017, "50 Years of Data Science", *Journal of Computational and Graphical Statistics*, [10.1080/10618600.2017.1384734](https://doi.org/10.1080/10618600.2017.1384734).
- Class (Friday 9 October)
    - 10-11: Defences.
    - (Classic paper) Donoho (2017).
    - (Classic paper) Neyman (1934), Sections I, III, and V.
    - (Lecture) Measurement, censuses, and sampling.
    - (Demonstration) Simulate a population, sample it five ways (simple random, systematic, stratified, cluster, and convenience), and compare the estimates and their spread.
    - (Worksheet) Population, frame, and sample for three real surveys; what Bowley did in Reading and what he could and could not claim.
    - Form Assignment II teams and pick Howrah or Dysart.

#### Week 6 (starts Monday 12 October)

*Gathering data: APIs, directly and through packages; semi-structured data (JSON and XML); web scraping, and when it is reasonable; parsing and OCRing PDFs. Hunting data: randomization, treatment and control, and average treatment effects; internal and external validity; informed consent and equipoise; A/B testing; designing and implementing surveys.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, Chapters [7](https://tellingstorieswithdata.com/07-gather.html) and [8](https://tellingstorieswithdata.com/08-hunt.html).
    - Salganik, Matthew, 2018, *Bit by Bit: Social Research in the Digital Age*, [Chapter 4 "Running experiments"](https://www.bitbybitbook.com/en/1st-ed/running-experiments/).
    - (Classic) Fisher, Ronald, 1935, *The Design of Experiments*, Chapter 2 "The principles of experimentation, illustrated by a psycho-physical experiment" (the lady tasting tea).
- Class (Friday 16 October)
    - (Quiz) Week 5 readings and class, including Neyman (1934).
    - (Classic paper) Fisher (1935).
    - (Lecture) Gathering data that exist, and creating data that do not, with experiments and surveys.
    - (Demonstration) Get data from an API with credentials in environment variables; scrape a table politely; parse a table out of a PDF.
    - (Worksheet) Tea tasting, run in class and then simulated; write five survey questions and have another team break them.

#### Week 7 (starts Monday 19 October)

*Cleaning and preparing: plan an endpoint, simulate it, start small, iterate; tests for data: class, range, uniqueness, and content; names; tidy data. Storing and sharing: FAIR; documentation, codebooks, and datasheets; personally identifying information, hashing, and simulation; Parquet. Data management: file and variable names, folder layout, linking tables.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, Chapters [9](https://tellingstorieswithdata.com/09-clean_and_prepare.html) and [10](https://tellingstorieswithdata.com/10-store_and_share.html).
    - Lewis, Crystal, 2024, *Data Management in Large-Scale Education Research*, Chapters 3, 4, 5, and 9, https://datamgmtinedresearch.com.
    - Gebru, Timnit, et al., 2021, "Datasheets for Datasets", *Communications of the ACM*, [10.1145/3458723](https://doi.org/10.1145/3458723).
    - Wilkinson, Mark, et al., 2016, "The FAIR Guiding Principles for scientific data management and stewardship", *Scientific Data*, [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).
    - Quartz, "Bad Data Guide", https://github.com/Quartz/bad-data-guide.
    - (Classic) Wickham, Hadley, 2014, "Tidy Data", *Journal of Statistical Software*, [10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10).
- Class (Friday 23 October)
    - (Quiz) Week 6 readings and class, including Fisher (1935).
    - (Classic paper) Wickham (2014).
    - (Lecture) Data organization, documentation, and style, following Lewis.
    - (Demonstration) Clean a messy extract with a simulated endpoint and tests written first; write the data dictionary and the first page of a datasheet.
    - (Worksheet) Bad data, tests, tidy data, and sharing; then the data dictionary, datasheet, and folder layout for your own Assignment II.

#### Reading Week (26-30 October)

#### Week 8 (starts Monday 2 November): Assignment II and in-class exam II

- Wednesday 4 November: Howrah or Dysart paper due EOD.
- Friday 6 November: In-class exam II.

### Part 3: Exploring and modeling

#### Week 9 (starts Monday 9 November)

*Exploratory data analysis: each variable by itself, each variable in the context of the others, and the data that are not there; distributions, outliers, and missing values; how EDA changes what you do next. What a model is for: explanation, prediction, and description; the two cultures. Linear models: simple and multiple linear regression; which assumptions matter. Generalized linear models: logistic regression for binary outcomes and Poisson and negative binomial regression for counts. Simulating before fitting. Interpreting and communicating models; predictions, comparisons, and slopes; marginal effects; writing the model and results sections.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, Chapters [11](https://tellingstorieswithdata.com/11-eda.html), [12](https://tellingstorieswithdata.com/12-ijalm.html), and [13](https://tellingstorieswithdata.com/13-ijaglm.html).
    - Anscombe, F. J., 1973, "Graphs in Statistical Analysis", *The American Statistician*, [10.1080/00031305.1973.10478966](https://doi.org/10.1080/00031305.1973.10478966).
    - Shmueli, Galit, 2010, "To Explain or to Predict?", *Statistical Science*, [10.1214/10-STS330](https://doi.org/10.1214/10-STS330).
    - Arel-Bundock, Vincent, 2025, *Model to Meaning: How to Interpret Statistical Models with marginaleffects for R and Python*, Part I, https://marginaleffects.com.
    - Rohrer, Julia M., and Vincent Arel-Bundock, 2025, "Models as Prediction Machines: How to Convert Confusing Coefficients into Clear Quantities", https://osf.io/preprints/psyarxiv/g4s2a_v1.
    - Tukey, John, 1977, *Exploratory Data Analysis*, excerpt provided.
    - Breiman, Leo, 2001, "Statistical Modeling: The Two Cultures", *Statistical Science*, [10.1214/ss/1009213726](https://doi.org/10.1214/ss/1009213726). (Read at least one of the comments and the rejoinder.)
- Class (Friday 13 November)
    - (Lecture) What EDA is for, and what a model is for.
    - (Lecture) Linear and generalized linear models; asking the model for predictions and comparisons.
    - (Demonstrations) EDA of the raw shelter file, which has a row for each program on each night, with the decisions written down as we make them; simulate data with known parameters, fit the model, and check that we get them back, and then fit the same models to real data; marginal effects tables and graphs for those models.
    - (Worksheets) EDA of your Final paper dataset; write the model section for three fitted models; write the results section for the same three.
    - (Housekeeping) There is a draft swap sheet in the folder to use with someone else in the class before you submit.

#### Week 10 (starts Monday 16 November)

- Class (Friday 20 November)
    - Please feel free to use this time to work on your Final paper.

#### Week 11 (starts Monday 23 November)

- Class (Friday 27 November)
    - Please feel free to use this time to work on your Final paper.

#### Week 12 (starts Monday 30 November): Assignment III and in-class exam III

- Wednesday 2 December: Final paper due EOD.
- Friday 4 December: In-class exam III.

#### Exam period

(Optional) Final exam, all three parts.

