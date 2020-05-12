# PROJECT 3: Understanding Student Success

<p align="center"> <img src= "/static/img/hero-bg.jpg"> </p>

## Project Goal
Use survey data gathered by the National Center for Education Statistics (NCES) to develop a model that predicts student success in high school. More specifically, the input parameters to the model are the responses to a series of questions posed to the student (e.g., student's demographics, socioeconomic status, habits, and goals), and the model result is the student's anticipated range of grade point average (GPA). For our project, student success is measured by the student's predicted high school grade point average (GPA).

## Machine Learning Model
To determine the most suitable model for our dataset, we tested and trained logistic regression, decision tree classifier, random forest classifer, and multi-layer perceptron classifer models with multiple imbalanced under/over sampling and imbalanced learn classifiers. Although the models did not yield a higher degree of correlation between the input parameters and the results, they did perform reasonably better than the null model. The final model selected was a **Random Forest Classifier with Imbalanced Learn Random Over Sampling** along with an iterative imputer to fill in missing values in the data. An excerpt of our code along with the imblanced learn classification report is provided below.

<p align="center"> <img src= "/static/img/model.png"> </p>

## Data Source for Model
As mentioned, our model is based on data provided by the NCES; the longitudianl study that we selected to obtain data for our model is the **[Education Longitudinal Study of 2002 (ELS, 2002)](https://nces.ed.gov/surveys/els2002/)**. ELS (2002) is the fourth study in a series of school-based longitudinal studies by NCES. ELS (2002) is a nationally representative, longitudinal study of 10th graders in 2002 and 12th graders in 2004. The goal of the study is to follow the students' trajectories from the beginning of high school into postsecondary education, the workforce, and beyond. Within the NCES dataset, our model focuses on high school statistics. After cleaning the NCES dataset, our model training dataset contained almost 15,000 rows (i.e., students) with 32 columns (i.e., 31 input parameters and one result parameter (i.e., GPA)). This cleaned dataset can be accessed via our web app (see below). [Note: the dataset also contains two more columns, one indicating if student graduated or was on track to graduate high school (or equivalent) and another indicating if the student ever dropped out of high school].

## Predictive Questionnaire
As part of the NCES studies, student's are asked to answer a very broad range and extensive list of questions. We reviewed the survey and selected 31 questions the we deemed most likely to be correlated with a student's final high school GPA. Our app reproduces these questions, serves the responses to a model, and then returns a prediction of the student's final high school GPA range (as well as the equilvalent letter grade) and the prediction probability of that GPA range.

<p align="center"> <img src="https://media.giphy.com/media/MAoXnyKgffhB7VdPek/giphy.gif"> </p>

## App Deployment
The Student Success web app is deployed online. It can be found [here](https://student-success-yvlxbmh5cq-uc.a.run.app/)!

## Final Thoughts
Ultimately, there are a multitude of factors that can contribute to a student's success in high school and their final GPA. In selecting 31 parameters that we deemed most likely to affect a student's over final GPA range, our hope was to develop a more accurate model. However, there are clearly a lot more factors that affect a student's GPA that are not captured in our model's dataset and in the NCES dataset.