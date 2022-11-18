![image](Other/Images/ufc_logo.jpg)
# Final Project: UFC Prediction Model
## Project Background
As a group we decided to create a model that will predict the outcome of a given UFC fight, based on the statistics we deem most correlated to the final restult. We selected this topic for the reasoning that we are all fans of mixed martial arts, while at the same time being interested in the determining factors of a fight. We found an all inclusive data set on kaggle.com that provided sigificant statistics of every UFC fight from 1993 to 2021. These statistics include fight outcomes, in fight damage, as well as fighter attributes. Our goal with this project is to utilize the data set to determine if a UFC fight can be predicted, to a degree, based on certain statistics.
## Communication Protocols
As a collective we decided that the Square Role (Git Hub) was going to be headed by Cade, the Triangle Role (Machine Learning) was going to be led by Joey, the Circle Role (Database) was going to be managed by Charles, and The X Role (Technology Tools) was going to be guided by Kohle. With these distinct roles in place, our team has an outline of who is in charge of what. However, our group intends on working together amoungst all necesary duties by utilizing the team's slack group chat for live communication and delgation.
## Machine Learning
I combined all the fighters into one data set with their stats aligned correctly (All_Fighters_aligned) so I could begin machine testing. There are also seperate data sets for Red Fighters, Blue Fighters, as well as another set seperating just winners and losers. There are two sets of Machine learning models that I built to get us started. I used the complete data set to run a decisiosn tree model and a randomforest model. They both performed better than expected. With the randomforest model I was able to generate a list of fields that have the heaviset impact on our predicitons. This will help us pick features that will give us the most improved results. Next step will be to run the same model with our modified data that we chose and then again with the "important" features generated by the machine learning importance report.


## Decision Tree

![image](https://user-images.githubusercontent.com/108442512/202004934-4ca3d078-5939-49b7-a744-b6636a80414f.png)

## RandomForest

![image](https://user-images.githubusercontent.com/108442512/202005053-9b090762-e04c-490a-9e5b-f582278e0eac.png)

## RandomForest with gradient boosting

![image](https://user-images.githubusercontent.com/108442512/202005165-39ce4916-6ffa-467c-9b65-1d2f7717f8fb.png)
