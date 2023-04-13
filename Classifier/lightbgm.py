import numpy as np
import lightgbm as lgb
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

X = np.loadtxt('SampleFeature.csv', delimiter=',')

clf = lgb.LGBMClassifier(learning_rate=1)

skf = StratifiedKFold(n_splits=5)
precision_list = []
recall_list = []
f1_score_list = []
acc_list = []
mcc_list = []
tprs = []
aucs = []
pr_aucs = []
mean_fpr = np.linspace(0, 1, 100)
for train_idx, test_idx in skf.split(X, y):
    X_train, y_train = X[train_idx], y[train_idx]
    X_test, y_test = X[test_idx], y[test_idx]
    clf.fit(X_train, y_train)
    y_pred_prob = clf.predict_proba(X_test)[:, 1]
    threshold = 0.5
    y_pred = np.where(y_pred_prob > threshold, 1, 0)
    print(classification_report(y_test, y_pred))
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    aucs.append(roc_auc)
    tprs.append(np.interp(mean_fpr, fpr, tpr))
    tprs[-1][0] = 0.0
    np.save(f"Y_pre{len(precision_list)}.npy", y_pred_prob)
    np.save(f"Y_test{len(precision_list)}.npy", y_test)
    precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
    accuracy = accuracy_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_score_list.append(f1_score)
    acc_list.append(accuracy)
    mcc_list.append(mcc)

plt.figure()
for i in range(len(tprs)):
    plt.plot(mean_fpr, tprs[i], lw=1, alpha=.8,
             label='ROC fold %d (AUC = %0.2f)' % (i, aucs[i]))

plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
         label='Random', alpha=.8)

std_tpr = np.std(tprs, axis=0)
tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
                 label=r'$\pm$ 1 std. dev.')

plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()
