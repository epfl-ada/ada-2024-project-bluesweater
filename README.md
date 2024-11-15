
# Lights, Camera, Success: What Makes a Movie Shine at the Box Office?
## Abstract
Welcome to the movie lab, where we believe movies are like chemical reactions, a blend of elements that can either explode into blockbuster magic or fizzle into obscurity. Today, data lets us break down these cinematic "potions" to understand what makes them tick. From budgets and genres to audience sentiment and box office numbers, each element plays a role in the volatile recipe of success. Our project investigates these factors by analyzing how they interact to create hits—or misses. First, we’ll quantify relationships between variables like star power, storytelling, and timing. Then, we’ll test how these “ingredients” combine to shape a film’s performance. This approach could reveal the alchemy behind the movies we love, offering new insights into how audiences connect with cinema. Understanding these dynamics might even help creators brew the perfect mix for the next cultural phenomenon. By approaching cinema through the lens of data, we aim to decode the magic of storytelling and shed light on what truly resonates with audiences. This could open new doors for filmmakers looking to craft their next unforgettable experience.

## Research questions we will aim to answer
1) Which countries or regions have gained significant influence in the global cinema landscape in recent years?
2) What metrics define a successful acting career, and how do collaborations with high-profile individuals impact it?
3) Which character tropes and gender pairings are most frequently associated with box office and critical success?
4) Does a high budget guarantee commercial success, or are other factors more influential?
5) What is the relationship between a movie's box office-to-budget ratio and its overall performance?
6) When is the optimal time to release a movie to maximize audience reception and revenue?
7) How do seasonal and cultural trends influence the success of specific genres or sequels?

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


## Helper Datasets

The biggest challenge we faced during this project was the missing data in key columns, such as Box Office and Revenue. To address these gaps, we utilized the following datasets:

### TMDB Data
The TMDB dataset provides valuable movie information, including box office revenue, popularity, and release data. By integrating this dataset, we were able to fill in a few gaps for missing box office and revenue information, helping us better assess the financial success of the films in our analysis. You can access the dataset [here](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates).

### IMDB Data
The IMDB dataset offers a comprehensive collection of movie ratings, genres, and detailed film information. This dataset helped us fill in missing ratings and genres, enhancing our ability to assess movie success across different metrics. The dataset can be found [here](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset).

### Oscars Data
The Oscars dataset includes information about nominations, wins, and other key statistics related to the Academy Awards. This dataset was crucial in assessing the influence of awards on a movie's success and allowed us to integrate data regarding Oscar wins and nominations to refine our analysis of movie success. You can access the dataset [here](https://www.kaggle.com/datasets/unanimad/the-oscar-award).

### Metacritic Movie Data
The Metacritic dataset offers aggregated reviews and scores from critics, providing insights into how the industry and critics view movies. By incorporating this data, we were able to analyze the impact of critical reception on a movie's overall success and reputation. The dataset is available [here](https://www.kaggle.com/datasets/patkle/metacritic-scores-for-games-movies-tv-and-music).


## General Methods

### Initial Pickle Creation 
To streamline our workflow and ensure efficient data handling, we created pickle files for each of the datasets we used in the project. This includes pickles for the CMU movies dataset, various helper datasets, and a master table that contained movie scores along with their corresponding names. These pickles are stored in the "pickles" directory, and the Jupyter notebooks used to generate them can be found in the "pipelines" directory. This approach allowed us to preprocess the data once and reuse it across different stages of analysis.


### Section Division 
To enhance collaboration and productivity, we divided the tasks across our team members, assigning each of us specific sections to work on. These sections were organized in individual notebooks located in the "src/sections" folder. By splitting the work, each team member could focus on specific aspects of the data analysis and cleaning, ensuring thorough attention to each section.



### Data Exploration 
Before diving into the data cleaning process, we performed an initial exploration of the data. This involved reviewing the types of variables, their distributions, and any apparent patterns. This exploratory phase allowed us to tailor our data cleaning techniques to the specific characteristics of each dataset, ensuring that we addressed issues effectively, such as identifying categorical versus continuous variables, and understanding missing data.


### Data Cleaning 
Throughout each section, we carried out thorough data cleaning processes. This included:

- Standardizing formats such as date-time conversion, ensuring consistency across the dataset.
- Removing insignificant null values (e.g., for variables that had less than 5% missing data) to avoid skewing results.
- Standardizing ratings across multiple sources (e.g., IMDb, Metacritic) to have a consistent metric for evaluating movie performance.

Our goal was to make the data consistent, accurate, and ready for analysis. This step was crucial to ensure that we could draw valid conclusions and insights from the data.


### Data Enrichment 
Wherever possible, we tried to enrich our datasets with additional information that could improve our analysis. This included:

- We merged data from the TMDB dataset to fill in as many gaps for missing box office and revenue as possible. 

- We used weighted averages to calculate movie success scores by incorporating metrics like Oscar wins, where movies with multiple awards received a higher weight in the score calculation.

- We created a new column called avg_score, which took the average rating from three platforms, as well as from the professional and general public critic scores.


This enrichment helped us create a more complete and robust dataset, enhancing the overall quality of our analysis.


### Data Visualization
To explore and communicate the relationships between different variables, we built several visualizations. For example:

- Bar charts were used to visualize the top 20 countries by movie production count, box office, revenue, etc. 

- Scatter plots to examine the relationship between budget and box office revenue, revenue with average rating, etc. 

- We used box plots to visualize the distribution of tropes in films, highlighting the most prominent ones and comparing the male-to-female character ratio. Additionally, we examined how these distributions relate to the films' average scores.

. These included plots that helped us uncover trends and patterns related to movie success. We also added regression lines to some of the visualizations to better illustrate potential correlations and offer insights into the factors that may influence a movie’s performance.


### Analysis Proposition  
Once all the sections were completed and the data was cleaned and enriched, we brought everything together in the "results.ipynb" notebook. In this notebook, we started with the original CMU movie dataset and incorporated the enriched data step by step. As we progressed, we highlighted the importance of each section in relation to our primary research questions. We also documented any key relationships we observed and provided evidence to support our claims, ensuring that our analysis was grounded in solid data and thorough exploration.



## How to use the library

As mentioned previously, our code is organized into the following directories and files:

- pickles directory contains the pd versions of the datasets we used in the project. These pickled files allow for quick access during analysis, eliminating the need to reload raw data multiple times.

- src/sections directory contains individual notebooks that focus on specific parts of the analysis. 

- results.ipynb contains the entire workflow from all sections into one comprehensive notebook. Here, you'll find a full explanation of our analysis, results, and insights, eliminating the need to look through the individual section notebooks. It is much more streamlined and easier to follow here.

- readme (this file) provides an overview of the project and a brief explanation of how the work in results.ipynb is structured. 


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

## Appendix 

### Questions asked during first TA meeting


### Questions asked during second TA meeting

