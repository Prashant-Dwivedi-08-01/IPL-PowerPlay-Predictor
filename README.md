# IPL-PowerPlay-Predictor
Know the IPL PowerPlay Score here!
<img src="assets/p1.jpg">
-------------------------------------------------------------------------------------------------------
**Setup**
1. Clone the repository
2. Install Django
3. Intall the required machine learning depenencies
 > pandas
 
 > numpy
 
 > sklearn
4. Open the terminal in the folder with manage.py file and run the commmand "python manage.py runserver"

-------------------------------------------------------------------------------------------------------
**Data Preprocessing part**

	1. A completely different dataset has been prepared so that it can suit the problem and give the best 
	   possible prediction. Point to note is that, the same dataset of ball by ball run is used to do so, 
	   no different dataset is used.

	2. All together 6 different features were prepared in the Feature Engineering Part of preprocessing.
	   Some of this feature includes 
		1. Venue
		2. Innings
		3. Batting team
		4. Bowling team
		5. Number of batsmen in Powerplay

	3.  Vennue, bowling team and batting team are the categorical features which were encoded to numerical
	    value. The technique followed to do the encoding was ORDINAL ENCODING with order set manually 
            depending upon the present performance of the teams.
--------------------------------------------------------------------------------------------------------
**Algorithm Part**

	Various different algorithms were used to do the prediction. After trying a large number of algorithms
	and techniques the final ML Algorithm was selected.


	Various Models Tested:
		1. Simple Linear Regression Model
		2. Ridge Regression Model with GridSearch Cross Validation
		3. Lasso Regression Model
		4. Random Forest Model
	Selected Model:
		1. Ridge Regression Model with GridSearch Cross Validation.
			Model Parameters and info:
				CV value = 5
				Alpha = 10
			Various Metric Scores:
				MAE: 8.075499181611894
				MSE: 110.25393587587322
				RMSE: 10.500187420987933
				Squared Error on Test Dataset : 28004.4997124718
