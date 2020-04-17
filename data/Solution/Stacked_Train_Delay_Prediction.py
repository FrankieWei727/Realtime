import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')
import warnings
def ignore_warn(*args,**kwargs):
    pass
warnings.warn = ignore_warn

from scipy import stats
from scipy.stats import norm,skew #for some statistics

#limitting floats output to 3 decimal points
pd.set_option('display.float_format',lambda x : '{:.3f}'.format(x))

from subprocess import check_output
#check the file available in the directory
print(check_output(['ls','data']).decode('utf8'))


#import and put the train and test datasets

train = pd.read_csv('data/bnkdata_1.csv')
test = pd.read_csv('data/bnkdata_2.csv')

#there are too more than 600 thousands data, it's more computation cost.so I just analysis one stop
train = train.loc[train['stop_id'] == 2000340]
test = test.loc[test['stop_id'] == 2000340]
train.head(5)


#check the number of sample and feature
print('The train data size before dropping Id feature is : {}'.format(train.shape))
print('The test data size before fropping Id feature is: {}'.format(test.shape))

#save the 'timestamp' columns
train_ID = train['timestamp']
test_ID = test['timestamp']

#Now drop the 'timestamp' column sine it's unnecessory for the prediction process
train.drop('timestamp',axis=1,inplace=True)
test.drop('timestamp',axis=1,inplace=True)

#check again the data size after dropping the Id variable
print('\nThe train data size after dropping Id feature is : {}'.format(train.shape))
print('\nThe test data size after dropping Id feature is : {}'.format(test.shape))

#Data Processing
#Outlier
fig, ax = plt.subplots()
ax.scatter(x = train['departure_delay'], y = train['arrival_delay'])
plt.ylabel('arrival_delay', fontsize=13)
plt.xlabel('departure_delay', fontsize=13)
plt.show()

#Deleting outliers
train = train.drop(train[(train['departure_delay']>2500) & (train['arrival_delay']<0)].index)

fig, ax = plt.subplots()
ax.scatter(x = train['departure_delay'], y = train['arrival_delay'])
plt.ylabel('arrival_delay', fontsize=13)
plt.xlabel('departure_delay', fontsize=13)
plt.show()


#Target Variable
#arrival delay is the variable we need to predict. So let's do some analysis on this variable first

sns.distplot(train['arrival_delay'],fit=norm)

#Get the fitted parameters used by the function
(mu,sigma) = norm.fit(train['arrival_delay'])
print('\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu,sigma))

#now plot the distribution
plt.legend(['Normal dist. ($\mu=${:.2f} and $\sigma=${:.2f})'.format(mu,sigma)],loc='best')

plt.ylabel('Frequency')
plt.title('arrival_delay distribution')

#Get also the QQ_plot
fig = plt.figure()
res = stats.probplot(train['arrival_delay'],plot=plt)
plt.show()

#Log transformation of target variable

#we use the numpy function log1p which applies log(1+x) to all elements of the columns
#train = train.drop(train[(train['arrival_delay'] == None)].index)
train['arrival_delay'] = np.log1p(train['arrival_delay'])

#Check the new distribution
sns.distplot(train['arrival_delay'],fit=norm)

#Get the fitted parameters used by the function
(mu,sigma) = norm.fit(train['arrival_delay'])
print('\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu,sigma))

#Now plot the distribution
plt.legend(['Normal dist. ($mu=$ {:.2f} and $\sigma=$ {:.2f})'.format(mu,sigma)],loc='best')
plt.ylabel('Frequency')
plt.title('arrival_delay distribution')

#Get the QQ-plot
#Quantile-Quantile or q-q plot is an exploratory graphical device used to check the validity of
# a distributional assumption for a data set
fig = plt.figure()
res = stats.probplot(train['arrival_delay'],plot=plt)
plt.show()


#Feature engineering
#let's first concatenate the train and test data in the same dataframe
ntrain = train.shape[0]
ntest = test.shape[0]
y_train = train.arrival_delay.values
all_data = pd.concat((train,test)).reset_index(drop=True)
all_data.drop(['arrival_delay'],axis=1,inplace=True)
print('all_data size is : {}'.format(all_data.shape))


# Missing Data
all_data_na = (all_data.isnull().sum() / len(all_data)) * 100
all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)[:30]
missing_data = pd.DataFrame({'Missing Ratio': all_data_na})
missing_data.head(20)

#Data correlation
#Correlation map to see hwo features are correlated with SalePrice
corrmat = train.corr()
plt.subplots(figsize=(12,9))
sns.heatmap(corrmat,vmax=0.9,square=True)


#due to all of the location_type value is null,so we can delete it
all_data = all_data.drop(['location_type'], axis=1)

#check  remaining missing values if any
all_data_na = (all_data.isnull().sum() / len(all_data)) * 100
all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)
missing_data = pd.DataFrame({'Missing Ratio' :all_data_na})
missing_data.head(10)

# Label Encoding some categorical variables that may contain information in their ordering set
from sklearn.preprocessing import LabelEncoder

cols = ('vehicle_id', 'departure_delay', 'wheelchair_boarding', 'platform_code')

# process columns, apply LabelEncoder to categorical features
for c in cols:
    lbl = LabelEncoder()
    lbl.fit(list(all_data[c].values))
    all_data[c] = lbl.transform(list(all_data[c].values))

# shape
print('Shape all_data: {}'.format(all_data.shape))

#skewed feature
numeric_feats = all_data.dtypes[all_data.dtypes != 'object'].index

#Check the skew of all numerical feature
skewed_feats = all_data[numeric_feats].apply(lambda x : skew(x.dropna())).sort_values(ascending=False)
print('\nSkew in numerical features: \n')
skewness = pd.DataFrame({'Skew':skewed_feats})
skewness.head(10)


#Box Cox Transformation of (highly) skewed features

skewness = skewness[abs(skewness) > 0.75]
print('There are {} skewed numerical features to Box Cox tranformation'.format(skewness.shape[0]))

from scipy.special import boxcox1p

skewed_features = skewness.index
lam = 0.15
for feat in skewed_features:
    # all data[feat] += 1
    all_data[feat] = boxcox1p(all_data[feat], lam)

# all_data[skewed_features] = np.log1p(all_data[skewed_features])

#Getting dummy categorical features
all_data = pd.get_dummies(all_data)
print(all_data.shape)

#getting the new train and test sets
train = all_data[:ntrain]
test = all_data[ntrain:]


train = train.drop(['stop_lat'],axis=1)
test = test.drop(['stop_lat'], axis=1)


from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import lightgbm as lgb


#Define cross validation strategy

#validation function
n_folds = 5
def rmsle_cv(model):
    kf = KFold(n_folds,shuffle=True,random_state=42).get_n_splits(train.values)
    rmse = np.sqrt(-cross_val_score(model,train.values,y_train,scoring='neg_mean_squared_error',cv=kf))
    return rmse

#Lasso Regression
lasso = make_pipeline(RobustScaler(),Lasso(alpha = 0.0005,random_state=1))

score_lasso = rmsle_cv(lasso)
print('\nLasso score: {:.4f} ({:.4f})\n'.format(score_lasso.mean(),score_lasso.std()))

#Elastic Net Regression
ENet = make_pipeline(RobustScaler(), ElasticNet(alpha=0.0005, l1_ratio=.9, random_state=3))
score_ENet = rmsle_cv(ENet)
print('\nENet score: {:.4f} ({:.4f})\n'.format(score_ENet.mean(),score_ENet.std()))


#Kernal Ridge Regression
KRR = KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5)
score_KRR = rmsle_cv(KRR)
print('\nKRR score: {:.4f} ({:.4f})\n'.format(score_KRR.mean(),score_KRR.std()))

#Gradient Boosting Regression
GBoost = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10,
                                   loss='huber', random_state =5)
score_GBoost = rmsle_cv(GBoost)
print('\nGBoost score: {:.4f} ({:.4f})\n'.format(score_GBoost.mean(),score_GBoost.std()))

#XGBoost
model_xgb = xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468,
                             learning_rate=0.05, max_depth=3,
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)
score_xgb = rmsle_cv(model_xgb)
print('\nXGBoost score: {:.4f} ({:.4f})\n'.format(score_xgb.mean(),score_xgb.std()))


#LightGBM
model_lgb = lgb.LGBMRegressor(objective='regression',num_leaves=5,
                              learning_rate=0.05, n_estimators=720,
                              max_bin = 55, bagging_fraction = 0.8,
                              bagging_freq = 5, feature_fraction = 0.2319,
                              feature_fraction_seed=9, bagging_seed=9,
                              min_data_in_leaf =6, min_sum_hessian_in_leaf = 11)
score_lgb = rmsle_cv(model_lgb)
print('\nLightGBM score: {:.4f} ({:.4f})\n'.format(score_lgb.mean(),score_lgb.std()))

#Stacking models

class AveragingModels(BaseEstimator, RegressorMixin, TransformerMixin):
    def __init__(self, models):
        self.models = models

    # we define clones of the original models to fit the data in
    def fit(self, X, y):
        self.models_ = [clone(x) for x in self.models]

        # Train cloned base models
        for model in self.models_:
            model.fit(X, y)

        return self

    # Now we do the predictions for cloned models and average them
    def predict(self, X):
        predictions = np.column_stack([
            model.predict(X) for model in self.models_
        ])
        return np.mean(predictions, axis=1)

averaged_models = AveragingModels(models = (ENet, GBoost, KRR, lasso))

score = rmsle_cv(averaged_models)
print(" Averaged base models score: {:.4f} ({:.4f})\n".format(score.mean(), score.std()))

#Adding a Meta-model

class StackingAveragedModels(BaseEstimator, RegressorMixin, TransformerMixin):
    def __init__(self, base_models, meta_model, n_folds=5):
        self.base_models = base_models
        self.meta_model = meta_model
        self.n_folds = n_folds

    # We again fit the data on clones of the original models
    def fit(self, X, y):
        self.base_models_ = [list() for x in self.base_models]
        self.meta_model_ = clone(self.meta_model)
        kfold = KFold(n_splits=self.n_folds, shuffle=True, random_state=156)

        # Train cloned base models then create out-of-fold predictions
        # that are needed to train the cloned meta-model
        out_of_fold_predictions = np.zeros((X.shape[0], len(self.base_models)))
        for i, model in enumerate(self.base_models):
            for train_index, holdout_index in kfold.split(X, y):
                instance = clone(model)
                self.base_models_[i].append(instance)
                instance.fit(X[train_index], y[train_index])
                y_pred = instance.predict(X[holdout_index])
                out_of_fold_predictions[holdout_index, i] = y_pred

        # Now train the cloned  meta-model using the out-of-fold predictions as new feature
        self.meta_model_.fit(out_of_fold_predictions, y)
        return self

    # Do the predictions of all base models on the test data and use the averaged predictions as
    # meta-features for the final prediction which is done by the meta-model
    def predict(self, X):
        meta_features = np.column_stack([
            np.column_stack([model.predict(X) for model in base_models]).mean(axis=1)
            for base_models in self.base_models_])
        return self.meta_model_.predict(meta_features)

stacked_averaged_models = StackingAveragedModels(base_models = (ENet, GBoost, KRR),
                                                 meta_model = lasso)

score = rmsle_cv(stacked_averaged_models)
print("Stacking Averaged models score: {:.4f} ({:.4f})".format(score.mean(), score.std()))

#Ensembling StackedRegressor, XGBoost and LightGBM
def rmsle(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

#Final training and prediction
stacked_averaged_models.fit(train.values, y_train)
stacked_train_pred = stacked_averaged_models.predict(train.values)
stacked_pred = np.expm1(stacked_averaged_models.predict(test.values))
print(rmsle(y_train, stacked_train_pred))

#XGBoost
model_xgb.fit(train, y_train)
xgb_train_pred = model_xgb.predict(train)
xgb_pred = np.expm1(model_xgb.predict(test))
print(rmsle(y_train, xgb_train_pred))

#LightGBM
model_lgb.fit(train, y_train)
lgb_train_pred = model_lgb.predict(train)
lgb_pred = np.expm1(model_lgb.predict(test.values))
print(rmsle(y_train, lgb_train_pred))

'''RMSE on the entire Train data when averaging'''

print('RMSLE score on train data:')
print(rmsle(y_train,stacked_train_pred*0.70 +
               xgb_train_pred*0.15 + lgb_train_pred*0.15 ))

#Esemble prediction
ensemble = stacked_pred*0.70 + xgb_pred*0.15 + lgb_pred*0.15

sub = pd.DataFrame()
sub['timestamp'] = test_ID
sub['arrival_delay'] = ensemble
sub.to_csv('data/train_delay_submission.csv',index=False)
