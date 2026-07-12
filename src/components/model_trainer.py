import os 
import sys 
from dataclasses import dataclass 

from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
) 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor 

from src.components.exception import customException
from src.components.logger import logging 
from src.components.utils import save_object,evaluate_model 

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
                logging.info("Splitling training and test input data")
                X_train,Y_train,X_test,Y_test=(
                    train_array[:,:-1],
                    train_array[:,-1],
                    test_array[:,:-1],
                    test_array[:,-1]
                )
                models = {
                 "Random Forest":RandomForestRegressor(),
                 "Decision Tree": DecisionTreeRegressor(),
                 "Gradient Boosting":GradientBoostingRegressor(),
                 "k-Neighbors Classifier":KNeighborsRegressor(),
                 "XGBClassifier":XGBRegressor(),
                 "CatBoosting Classifier":CatBoostRegressor(verbose=False),
                 "AdaBoost Classifier":AdaBoostRegressor(),   
                }


                model_report:dict=evaluate_model(X_train=X_train,Y_train=Y_train,X_test=X_test,Y_test=Y_test,models=models)

                #To get best model score from dict
                best_model_score=max(sorted(model_report.values()))

                #to get best model name

                best_model_name =list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                    ]
                best_model=models[best_model_name]
                if best_model_score<0.6:
                    raise customException("No best model found")
                logging.info(f"Best model found both on trained and test data")

                save_object(
                    file_path=self.model_trainer_config.trained_model_file_path,
                    obj=best_model 
                )

                predicted=best_model.predict(X_test)
                r2_sQore=r2_score(Y_test,predicted)
                return r2_sQore
                re 
        except Exception as e:
                raise customException(e,sys)


