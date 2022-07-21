# Korean-Abusive-Language-Dataset

This is the abusive language datasets (AbuseEval, CADD, Davidson, Waseem) translated into Korean.

We share two types for each dataset because each dataset has different columns.
1. origin_*.csv: a Korean version of an original dataset (Preserve columns of the original datasets)
2. model_*.csv: a dataset for training and testing a model (consisting of 5 columns: ['Dataset', 'Id', 'Context', 'Comment', 'Target']) ~ Target is the label, {abusive, not abusive}
### If you want to train your model with original labels, use 'origin_*.csv' files.
### If you want to train your model with {abusive, not abusive} labels, use 'model_*.csv' files.
We explain how we adjust the labels (origin labels -> binary labels) in our paper (please see the reference below).


For AbuseEval and CADD, there are 'origin_{train, valid, test}.csv' and 'model_{train, valid, test}.csv'.

For Davidson and Waseem, they are not divided into {train, valid, test} sets.
You can split the data depending on the ratio you want, if you need to.
In our paper, we set the ratio as 7(train):1(valid):2(test).
For Waseem, we divided the data after shuffling it. 


### origin_* 에 대한 설명
#### 모든 데이터의 앞 5개 컬럼은 다 같음. (데이터명, 아이디, context, comment(대상), target(폭력성 0/1)

#### 'abuse'는 3 classes (NOTABU: 비폭력, EXP: 명시적 폭력, IMP: 암묵적 폭력)
AbuseEval = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'abuse']

#### 'L
CADD = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'L.Type', 'L.Abusive', 'lAttack', 'L.Dem', 'L.Implicit', 'L.Profanity', 'lenComment', 'lenContext']

#### 'class'는 3 classes (0: hate speech, 1: offensive language, 2: neither)
Davidson = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'hate_speech', 'offensive_language', 'neither', 'class']

#### 'Annotation'은 3 classes (sexism, racism, neither)
Waseem = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'Annotation']


# Reference
