
# This script was generated by the train.py script in EHA's private eval-scripts
# repository.

import numpy as np
from numpy import array, int32
base_classifier = {'C': 1.0,
 'class_weight': None,
 'classes_': array([False,  True], dtype=bool),
 'coef_': array([[ 0.39530969,  0.01060297, -0.03141362,  0.39494371,  0.67073634,
         0.34905983, -0.61796757, -1.77360302, -2.91882867,  0.0228208 ,
        -0.00338034, -1.59774783, -1.33141784,  0.06533717, -1.82860319,
         0.08991445,  0.        ,  0.        ,  0.        ,  0.        ]]),
 'dual': False,
 'fit_intercept': True,
 'intercept_': array([-4.69243169]),
 'intercept_scaling': 1,
 'max_iter': 100,
 'multi_class': 'ovr',
 'n_iter_': 39,
 'penalty': 'l2',
 'random_state': None,
 'solver': 'liblinear',
 'tol': 0.0001,
 'verbose': 0}
HIGH_CONFIDENCE_THRESHOLD = 0.5
GEONAME_SCORE_THRESHOLD = 0.2
contextual_classifier = {'C': 1.0,
 'class_weight': None,
 'classes_': array([False,  True], dtype=bool),
 'coef_': array([[ 0.29834424,  0.01332741,  0.00838   ,  0.31499272,  0.29337092,
         0.12605664, -0.13240105, -1.30371734, -2.43522754, -0.03879782,
        -0.00255487, -1.24089784, -1.1968154 ,  0.28878839, -1.59002003,
         0.18128809,  0.8498247 ,  0.11828297,  0.70952814,  1.37533143]]),
 'dual': False,
 'fit_intercept': True,
 'intercept_': array([-3.73894488]),
 'intercept_scaling': 1,
 'max_iter': 100,
 'multi_class': 'ovr',
 'n_iter_': 36,
 'penalty': 'l2',
 'random_state': None,
 'solver': 'liblinear',
 'tol': 0.0001,
 'verbose': 0}
# Logistic regression code from scipy
def predict_proba(X, classifier):
    """Probability estimation for OvR logistic regression.
    Positive class probabilities are computed as
    1. / (1. + np.exp(-classifier.decision_function(X)));
    multiclass is handled by normalizing that over all classes.
    """
    prob = np.dot(X, classifier['coef_'].T) + classifier['intercept_']
    prob = prob.ravel() if prob.shape[1] == 1 else prob
    prob *= -1
    np.exp(prob, prob)
    prob += 1
    np.reciprocal(prob, prob)
    if prob.ndim == 1:
        return np.vstack([1 - prob, prob]).T
    else:
        # OvR normalization, like LibLinear's predict_probability
        prob /= prob.sum(axis=1).reshape((prob.shape[0], -1))
        return prob
def predict_proba_base(X):
    return predict_proba(X, base_classifier)
def predict_proba_contextual(X):
    return predict_proba(X, contextual_classifier)
