# Illinois Fighting Illini Men's Basketball: Statistical Modeling
Statistical modeling of Illinois Fighting Illini Men's Basketball statistics in the 2019-20 season. This project analyzes individual players' contribution to the game results, and the relation of their recruiting rating and actual performance, for the purpose of finding the optimal strategy (statitically!) of winning games, and predict the performance of the newly recruited freshmen. The methods used in this project include `correlation analysis`, `regression analysis`, and `statistical modeling`.

## Background
Illinois Fighting Illini men's basketball (Fighting Illini hereinafter) has done a brilliant job in the 2019-2020 season - after not being able to make it into the NCAA tournament for six seasons, there is no doubt at all that we were going to have our first tournament appearance after the 2012-2013 season, if it hasn't been cancelled because of the coronavirus pandemic. With 21 games won and 10 games lost, we ranked the 4th in the Big Ten conference, and the 21st in the final Associated Press college basketball poll among all 350 Division I colleges. As head coach Brad Underwood noted:
> "Such an abrupt ending to this long journey led to one of the most difficult conversations I've had with a team in my 33 years of coaching...  They worked their tails off and accomplished what they set out to do; bring Illinois Basketball back to national prominence and the NCAA Tournament."

And we are moving forward. To many Fighting Illini fans' surprise, despite being invited to the NBA combine, two of our best players, Ayo Dosunmu and Kofi Cockburn, have just withdrawn from NBA draft and returned to the program. Although some key players are either graduated or transferred, the return of Ayo and Kofi, as well as the recruition of new talented freshmen, especially Adam Miller and Andre Curbelo, makes us a `title contending team` in the coming season. We rank 6th in the College Basketball Rankings, and we can certainly do more than that. What Ayo Dosunmu wrote in the Twitter spoke of:
![](https://pbs.twimg.com/media/EeTI7bDWkAYcztJ?format=jpg&name=medium)

There are still months to go before the new season comes, but it certainly doesn't hurt to do some statistical modeling, as the NBA data analysts always do, to analyze who were our most important players last season, how could we expect our freshmen, and what should be our "optimal" strategy to win games, contend for the national championship, and MAKE HISTORY.

## Data
There are four dataframes from three data sources used in this project. `Game Results` (showing the points of the Fighting Illini and opponents, point difference and W/L of each game) and `Game Statistics` (showing the statistics of each player in each game) are collected from [The official website of Fighting Illini](https://fightingillini.com/sports/mens-basketball/stats), `Recruiting Information` (showing the recruiting rating and ranking of each player) is collected from [247sports](https://247sports.com/college/illinois/Season/2020-Basketball/Commits/), while `Advanced Statistics` (showing the high-level statistics of each player in the entire season) is collected from [Sports Reference](https://www.sports-reference.com/cbb/schools/illinois/2020.html).

## Hypotheses and Results
Hypothesis 1: Players' positive statistics (points, rebounds, assists, etc.) are positively related to the point differences in each game, while players' negative statistics (turnovers, fouls, etc.) are negative related to it.

Hypothesis 2: For the starting lineups and key players, the relationships in hypothesis 1 would be stronger in the close games (defined as |point difference| <=7).

![](https://github.com/charlemagne1996/Final_Projects_Su2020/blob/master/Images/Result1.png) 
![](https://github.com/charlemagne1996/Final_Projects_Su2020/blob/master/Images/Result2.png)  

Hypothesis 3: If we predictive model the game results with stats, by iteratively removing the player's stats that contribute least to the model accuracy in each round, the key players will be kept at last.

    In round 1, player Tevian Jones is least effective in predicting game results and is removed from the model
    In round 2, player Jermaine Hamlin is least effective in predicting game results and is removed from the model
    In round 3, player Kipper Nichols is least effective in predicting game results and is removed from the model
    In round 4, player Benjamin Bosmans-Verdonk is least effective in predicting game results and is removed from the model
    In round 4, player Samson Oladimeji is least effective in predicting game results and is removed from the model
    In round 5, player Trent Frazier is least effective in predicting game results and is removed from the model
    In round 5, player Tyler Underwood is least effective in predicting game results and is removed from the model
    In round 5, player Zach Griffith is least effective in predicting game results and is removed from the model
    In round 6, player Alan Griffin is least effective in predicting game results and is removed from the model
    In round 7, player Da'Monte Williams is least effective in predicting game results and is removed from the model
    In round 8, player Andres Feliz is least effective in predicting game results and is removed from the model
    In round 9, player Kofi Cockburn is least effective in predicting game results and is removed from the model
    In round 10, player Ayo Dosunmu is least effective in predicting game results and is removed from the model
    Player Giorgi Bezhanishvili is the most effective in predicting game results

Hypothesis 4: The performance of a player (measured by EFF (individual player efficiency) value and PER (player efficiency rating) value) is positively correlated to his recruiting rating at the point of commitment, which is based on his performance in high school.

![](https://github.com/charlemagne1996/Final_Projects_Su2020/blob/master/Images/Result3.png) 
![](https://github.com/charlemagne1996/Final_Projects_Su2020/blob/master/Images/Result4.png)  
![](https://github.com/charlemagne1996/Final_Projects_Su2020/blob/master/Images/Result5.png) 
![](https://github.com/charlemagne1996/Final_Projects_Su2020/blob/master/Images/Result6.png)  

## Conclusions

The results are supportive to hypotheses 1, 2, and 3, but not supportive to hypothesis 4.

For hypothesis 1, in most cases, players' positive statistic are positively related to the point differences in each game, while players' negative statistics are negative related to it. However, there are some outliers. For example, Tevian Jones' statistics do not really follow this rule, implicating that his leave may not be a significant loss for the program.

For hypothesis 2, if we only keep the close games, only key players' positive statistic are positively related to the point differences in each game and their negative statistics are negative related to it. Our two NBA-level players, Ayo Dosunmu and Kofi Cockburn appeared to have contributed most.

For hypothesis 3, in predictive modeling, the players that are kept at last in the model are basically the most important players (last five players kept are all regular lineups). And interestingly, Ayo Dosunmu and Kofi Cockburn rank 2nd and 3rd, and 1st is Giorgi Bezhanishvili, showing his importance may be underestimated.

For hypothesis 4, neither does player's EFF value or his PER value has a "statistically significant" postive relationship with the recruiting rating of him (although both correlation coefficients are positive). This indicates that better talent does not directly yield better performance: Adam Miller and Andrew Curbelo have to work hard, and lower rated rookies do have chance!

    Please refer to Project.ipynb for the detailed process of analysis
