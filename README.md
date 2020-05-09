# PROJECT 3: Understanding Student Success

<p align="center"> <img src= "/static/img/hero-bg.jpg"> </p>

## Goal of Project
To determine if there is a relationship between a student's success in high school based on the quality of their school, and the student's demographics, socioeconomic status, habits, and goals. For our project, student success is measured by the student's predicted high school grade point average (GPA).

## Machine Learning Model
To determine the most suitable model for our dataset, we tested and trained logistic regression, decision tree classifier, random forest classifer, and multi-layer perceptron classifer models with multiple imbalanced under/over sampling and imbalanced learn classifiers. Unfotunately, the models did not yield a truly meaningful correlation. However, one model did perform reasonably better than the null model. The final model used was a **Random Forest Classifier with Imbalanced Learn Random Over Sampler** along with an iterative imputer to fill in missing values in the data. 

<img src= "/static/img/model.png">

## Data Source for Model
Our model is based on data from the **[Education Longitudinal Study of 2002 (ELS: 2002)](https://nces.ed.gov/surveys/els2002/)**. The ELS: 2002 is the fourth study in the a series of school-based longitudinal studies by the National Center for Educaiton Statistics. The ELS: 2002 is a nationally representative, longitudinal study of 10th graders in 2002 and 12th graders in 2004. The goal of the study is to follow the students' trajectories from the beginning of high school into postsecondary educaiton, the workforce, and beyond.

## Predictive Questionnaire
We created a quesitonnaire to predict the user's high school GPA range on a scale of 0 - 3, the equilvalent letter grade, and the probability of the GPA range. After answering 31 simple questions, the user will be provided with their their predicitons.

<img src="https://media.giphy.com/media/MAoXnyKgffhB7VdPek/giphy.gif">

## Heroku Deployment
The Student Success web app is deployed via **Heroku**. It can be found [here](https://predict-student-success.herokuapp.com/)!

## Final Thoughts
Ultimately, there are a multitude of factors that can contribute to one's success in high school. Our original idea was to predict a student's GPA and determine whether the student would graduate or drop out of high school. Unfortunately, there is not a data source that captures all of the factors that can lead to a student dropping out or graduating high school, therefore, our models did not yield a meaningful correlaton for graduation and drop-out. This meant we had to narrow our the focus of our model to GPA only. However, we realize a student's success in high school is not solely determined by their GPA.
