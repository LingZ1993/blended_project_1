# Risk Factors for Cardiovascular disease

## Group Members: 
Nick Guild, Cedric Larue, Ling Zhang, and Teale Foster

## Communication Protocols
Group members uses Slack and messages for communications and also using Zoom for group meetings. 

## Tools
SQL, Python and using Tableau for Data visualizations

## Presentation
https://docs.google.com/presentation/d/1CLn6aMWFkfWZ_EBmw5tNoQWBXpHDvC8jLaq04usb684/edit?usp=sharing

## Dashboard
https://docs.google.com/presentation/d/1dkKnMS9PdWOnYIQ0ZZtfbRx3UqNOwxuxdaFpwCcaJWw/edit?usp=sharing

## Data Source
Our dataset was taken from a Kaggle dataset with 70,000 plus data points that was uploaded a little less than two years ago. It contains thirteen columns (12 feature columns and the outcome column, cardio).  The original uploader is a researcher named Svetlana Ulianova.

## Summary of the Project
The research topic we chose was an exploration of cardiovascular disease, and the factors (features) that can lead to its occurrence.

Heart disease is a serious world issue that affects every country to a varying degree. We hope after performing this analysis we will have a better understanding (at least on a personal level) of what leads to these dreadful conditions and what measures may be taken in order to try to stop them.

The dataset used contains data for cardiovascular disease patients. The data in the file used contains information on a patient’s age, gender, height, weight, cholesterol levels, glucose levels, BMI, whether they smoked, used alcohol, or their level of physical activity. These metrics all play a deciding factor in whether a person develops cardiovascular disease. There were no potential outliers found in the dataset, also no metric involved has been proven to any other statistically. Any missing values were removed to prevent errors in results.

With the use of machine learning models, the future of medicine could very well be far more preventive than reactive.  This would mean not only a dramatic increase in the ability to save lives before they’re at risk, but also reduce the enormous financial burdens that cardiovascular disease brings with it.

Our exploratory data analysis started off with some difficulty.  Our data, which was in a .csv file, had “ ; ” as the deliminators instead of “ , “ which was odd to say the least.  In order to fix this, we went into VS code and used the find/replace method to change all instances of semicolons to commas.  Once that was complete, we were able to begin working with the data. 

Firstly, we established that there we were no null values.  After considering the features that we had, we realized that we could create another feature column that very well could hold predictive value- BMI, or body mass index.  The formula of which is simply: mass, in kg divided by meters squared.  The only change we had to make was to consider that our subjects have their height listed in centimeters, instead of meters.  So we ran the following script to account for that: cardio_df["BMI"] = cardio_df["weight"]/ (cardio_df["height"]/100)**2.

We then rounded the BMI values to two decimal points again using pandas.  Once we had that column neat and tidy, we changed some of the other column names so they were easier to to understand (what was ap_lo became diastolic_bp and ap_hi became systolic_bp, for example) at a quick glance.  
After that, we split the dataframe into two (that we’d later join in postgres SQL).
Once we finished the rest of the cleaning, we exported the two dataframes as .csv files and used Postgres SQL along with PySpark to work with them from there.
