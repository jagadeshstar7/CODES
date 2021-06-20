#perform a chi^2  test to the samples to retrieve only the two best features as follows:
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
iris = load_iris()
X, y = iris.data, iris.target
X.shape
X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
X_new.shape

#Select features according to a percentile of the highest scores.
from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectPercentile, chi2
X, y = load_digits(return_X_y=True)
X.shape

X_new = SelectPercentile(chi2, percentile=10).fit_transform(X, y)
X_new.shape

#using common univariate statistical tests for each feature: false positive rate
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectFpr, chi2
X, y = load_breast_cancer(return_X_y=True)
X.shape
X_new = SelectFpr(chi2, alpha=0.01).fit_transform(X, y)
X_new.shape

