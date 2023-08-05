import joblib

import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)

X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
X_train = np.round(X_train, 3)

clf = IsolationForest(n_estimators=50, max_samples=500, random_state=rng, contamination=0.01)
clf.fit(X_train)

joblib.dump(clf, './model.joblib')
