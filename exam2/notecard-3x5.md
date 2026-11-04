# Exam 2 notecard (one side, 3×5)

Handwrite this. Put your name on the card. Portrait: 5-inch side vertical.
31 lines, no blank lines. About 4 mm per line. If your writing is taller,
drop lines from the bottom: PCA/NB, then kNN/SVM, then the slope line.

```
NAME
DS=program+stats+domain -> insight from data
1biz 2collect 3clean 4EDA 5model 6report 7deploy
arange(10,5001,10) zeros((r,c)) ones_like .shape
slice=VIEW (.copy) a[:,-1] a[2:,1:2] keeps col
a[1]=0 fills block. a+b and a>b on whole array
.loc=label, end IN. .iloc=position, end OUT
idx 1,3,5: loc[1]=a  iloc[1:3]=b,c  s>'b' -> c
df['c']=Series df[['a','b']] df[df.c>=18]
isin([])  df['n']=v aligns index  del df['c']
bar=cat counts. hist/box/density=one number
scatter=two nums. line=time. pie=share of whole
heatmap/pairplot=corrs. same stats can differ
r: -1..1, 0=none, ~±1 strong. correlation≠cause
OLS mins residuals. formula: y ~ x1 + x2
params[0]=b then slopes. y=b+m1*x1+m2*x2
m = change in y per +1 x, other x fixed
underfit=too simple/big k. overfit=wiggly/tiny k
polyfit(x,y,deg)->poly1d. dummy drops 1 level
concat([a,b])=rows axis=1=cols ignore_index
merge: inner=both how=left/right/outer
left_on/right_on if key names differ
NaN: empty,merge,reindex,math. mean skips NaN
fillna ffill bfill interpolate dropna
drop_duplicates. tidy: row=obs col=variable
long=for analysis. to_datetime ISO=YYYY-MM-DD
X=features y=label. sup=predict unsup=transform
import init X,y fit predict score. acc=right/n
logistic=class, sigmoid, cutoff 0.5
kNN=majority of k. SVM=max margin. kmeans=centers
PCA.fit(X) no y. NB: features treated independent
```
