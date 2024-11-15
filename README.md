
# Lights, Camera, Success: What Makes a Movie Shine at the Box Office?
## Abstract
Welcome to the movie lab, where we believe movies are like chemical reactions, a blend of elements that can either explode into blockbuster magic or fizzle into obscurity. Today, data lets us break down these cinematic "potions" to understand what makes them tick. From budgets and genres to audience sentiment and box office numbers, each element plays a role in the volatile recipe of success. Our project investigates these factors by analyzing how they interact to create hits—or misses. First, we’ll quantify relationships between variables like star power, storytelling, and timing. Then, we’ll test how these “ingredients” combine to shape a film’s performance. This approach could reveal the alchemy behind the movies we love, offering new insights into how audiences connect with cinema. Understanding these dynamics might even help creators brew the perfect mix for the next cultural phenomenon. By approaching cinema through the lens of data, we aim to decode the magic of storytelling and shed light on what truly resonates with audiences. This could open new doors for filmmakers looking to craft their next unforgettable experience.

## Research questions we will aim to answer
1) How interconnected are global film industries through shared actors, directors, and production collaborations?
2) Which countries or regions have gained significant influence in the global cinema landscape in recent years?
3) What metrics define a successful acting career, and how do collaborations with high-profile individuals impact it?
4) Which character tropes and gender pairings are most frequently associated with box office and critical success?
5) Does a high budget guarantee commercial success, or are other factors more influential?
6) What is the relationship between a movie's box office-to-budget ratio and its overall performance?
7) When is the optimal time to release a movie to maximize audience reception and revenue?
8) How do seasonal and cultural trends influence the success of specific genres or sequels?



### How to use the library
Tell us how the code is arranged, any explanations goes here.

### Datasets
Kaggle Links:

Oscars Data: https://www.kaggle.com/datasets/unanimad/the-oscar-award

Metacritic Movie Data: https://www.kaggle.com/datasets/patkle/metacritic-scores-for-games-movies-tv-and-music

IMDB Data: https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset

## Main project sections

### Section 1: Global Influence in Cinema  
The global cinema landscape reflects the dominance of certain countries and languages in shaping the film industry. To be more specific, we plan to analyze our data to identify the top countries and languages in the film industry. Additionally, we examined how these factors relate to critical metrics such as budget and revenue, offering insights into their impact on global cinematic success. This approach provides a straightforward yet valuable perspective on the key players and their contributions to the entertainment ecosystem.

### Section 2: Blueprint of Success in Acting 
In the movie lab, an actor's journey to stardom is a critical ingredient in our cinematic formula. Actors reach their breakthrough moments at different stages—at what age do they typically "ignite," and is there a critical mass of roles that triggers success, or can one iconic role act as a catalyst for fame? Does this trajectory vary between men and women? To analyze this, we also use our *Oscar Score*, a weighted metric reflecting actors' achievements through Oscar wins and nominations, to uncover trends in performance, box office revenue, audience ratings, and age, shedding light on the paths actors take to rise to prominence.

 
### Section 3: Tropes and their influence on Movie Success
Character tropes are central to storytelling, but which ones consistently lead to success on the big screen? In this section, we will explore how different character archetypes and gender pairings impact a film’s performance, from box office revenue to critics’ and audience ratings. By analyzing patterns in successful movies, we aim to uncover which tropes resonate most with viewers and whether certain dynamics—such as the pairing of leads by gender or genre-specific archetypes—play a significant role. This study seeks to provide insights into the storytelling elements that drive both commercial and critical acclaim, offering a deeper understanding of how character dynamics shape the overall success of a movie. 


### Section 4: Budget and Success Correlation 
Does a high budget truly guarantee commercial success, or are other factors more influential in determining a movie’s performance? In this section, we will examine the relationship between budget size and success by analyzing box office-to-budget ratios and comparing the relative "custom rating" performance of the highest-budget films each year. Beyond sheer financial investment, we’ll investigate the role of high-profile collaborations, such as A-list actors and directors, in shaping outcomes. This analysis aims to uncover whether bigger budgets consistently lead to better results or if success depends on a more nuanced combination of resources, talent, and strategic execution.


### Section 5: Timing and Audience Reception
Timing can make or break a movie’s success, but when is the optimal moment to release a film? This section explores the influence of seasonal and holiday periods on audience reception and box office revenue. By segmenting the year into distinct timeframes, we will analyze how factors such as genre, sequel status, and prevailing cultural moods align with release strategies. This investigation aims to identify patterns in audience behavior and uncover strategies that filmmakers and studios can use to maximize both reception and financial performance. Understanding the timing sweet spot could provide valuable insights into the art and science of film release planning.


### Side note about "Towards Inclusivity Section"
This section was initially intended to explore how gender and age representation impact commercial success across genres and regions, as well as whether the movie industry is evolving toward inclusivity in terms of gender, race, and age. However, after careful consideration, we decided to remove this idea from our analysis.


The concept was intriguing but too vague and lacked sufficient data for meaningful analysis. So pursuing this risked producing unreliable conclusions.


### Improvements for Milestone 3 
The biggest challenge we faced in this milestone was the significant amount of missing data, particularly in critical columns like box office revenue and total revenue, which are essential for answering questions about what defines a movie's success. Dropping these entries or filling them with the column mean would result in unreliable analysis.


To address this, we incorporated as many supplementary datasets as possible. While this improved the situation slightly, gaps remain. For the final milestone, we propose using the *OMDB API*. One team member purchased access and tested it on a subset of our dataset, successfully filling some of the missing values for box office revenue, runtime, and other key metrics. However, with over 80,000 entries in our dataset and the API's limit of ~500 calls per minute, it would take at least three hours to complete. We would like to confirm with our TA if using the API at this scale is acceptable.


Additionally, if we can retrieve more revenue and box office data, we propose adjusting monetary values for inflation. Since our dataset spans movies from the 20th to the 21st century, accounting for inflation would provide a more accurate representation of financial success across decades. We would also like to confirm with our TA if this approach is advisable.



### Conclusion: Insights on Cinema’s Key to Success
In summary, our exploration of cinema’s key to success reveals the growing interconnectedness of global film industries, the influence of character tropes and representation diversity, and the nuanced impact of budget and timing on a movie’s performance. While high-profile collaborations and well-timed releases play crucial roles, audience reception and cultural relevance remain pivotal. These findings provide valuable insights for filmmakers seeking to navigate evolving industry trends and craft films that resonate both critically and commercially.



## Project Structure

The directory structure of new project looks like this:

```
├── data                        <- Project data files
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── tests                       <- Tests of any kind
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md
```

