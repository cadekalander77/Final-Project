# Machine Learning
UFC Fight Prediction Models

## Description of data preprocessing
 * Used find and replace to change the winners from strings to numeric
 * Removed unnecessary columns
 * Used VBA to separate winners and losers into their own columns
 * Used Copy and Paste series to create unique IDs for each fighter
 * Used VLOOKUP to match fights with their camps, locations, and county from our other data set
 * Use PgAdmin to SELECT * DISTINCT to gather all fight camps together from the fight list including all fighters as well

## Description of feature engineering and the feature selection

We started with features that we thought would be the most effective at predicting the outcome of each fight. After running multiple models and a feature importance calculation we adjusted the features to the ones that were the most impactful and gave us the most accurate results.
	
  * avg_opp_SIG_STR_pct
  * avg_SIG_STR_pct
  * avg_opp_CTRL_time_seconds
  * avg_CTRL_time_seconds
  * avg_opp_TOTAL_STR_landed
  * avg_TOTAL_STR_landed
  * avg_SIG_STR_landed
  * avg_opp_HEAD_landed
  * avg_HEAD_landed
  * avg_opp_TOTAL_STR_att

## Description of how data was split into training and testing sets

Since we mainly used Logistic Regression type models for the data set, we use the "Results" Column as our y and the rest as our X. We used the default of 75/25 to split the data into training and testing sets.

## Explanation of models

We ran several different models to find the best results. LinearRegression models would not work for this as we were looking for binary choice. We decided on LogisticRegression models for our fights data set. We ran several models including Simple Logistic Regression, Simple Logistic Scaled, SVM, Decision Tree, Random Forrest, Random Forrest with boosting, encoding, SMOTE, and finally a neural network build. At this time we couldn't find any benefit in running this data with an unsupervised learning model for the neural network build, we tried several different combinations of units, activations, and input_dimensions to get the best results.

As of now, the best we were able to attain is 61% from a Random Forrest Model.

![image](https://user-images.githubusercontent.com/108442512/205197181-93733229-1cf6-4b2e-a811-3d7e5e1eb156.png)

## Next Steps
Now that we feel like we have the best results from the fight data set we are going to process the fighter data set. We will run some LinearRegression models to see how well we can predict results from that data set as well. We will link both databases together in PgAdmin using our unique IDs keys.
