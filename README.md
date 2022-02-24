# Income-Prediction-App-With-Django
For this project I made an income prediction app that predicts if a person has an income greater than or less than 50,000. The features that are used to make this prediction are a person’s age, how many years of education they completed, how many hours per week they work, what sector they work in, their marital status, their family relationships, their race, and their sex. The model that is used to make this classification is a simple logistic regression model. The attached notebook file, income_model.ipynb, shows the model training process. A logistic regression model was chosen due to its better performance compared to the other models. The data that was used to train the model was found on Kaggle.com and the dataset can be found in the files for this repository. 
Django was used to create the graphical user interface. The website that was created allows a user to input the necessary features and click the submit button. Once the submit button is pressed the corresponding classification is shown. The features that the user input as well as the classification the model gave are then stored in a database that can be viewed by the user by either clicking on DB at the top of the page or by clicking on View DB after clicking submit. 
