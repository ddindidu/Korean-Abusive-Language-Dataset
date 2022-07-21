# Korean Abusive Language Dataset

This is the abusive language datasets (AbuseEval, CADD, Davidson, Waseem) translated into Korean.

We share two types for each dataset because each dataset has different columns.
1. origin_*.csv: a Korean version of an original dataset (Preserve columns of the original datasets)
> All datasets have following columns.
>> 'Dataset': the name of dataset
>> 
>> 'Id'     : the Id of text data from the original dataset
>> 
>> 'Context': context texts; If there is no context text in original data, data is "".
>> 
>> 'Comment': texts to be classified
>> 
>> 'Target' : binary labels that we refined original labels in our work {abusive (1), not abusive (0)}
>> 
>> their original labels: refer their papers
>
> AbuseEval = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'abuse']
> 
> CADD = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'L.Type', 'L.Abusive', 'lAttack', 'L.Dem', 'L.Implicit', 'L.Profanity', 'lenComment', 'lenContext']
> 
> Davidson = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'hate_speech', 'offensive_language', 'neither', 'class']
> 
> Waseem = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'Annotation']

2. model_*.csv: a dataset for training and testing a model
> (consisting of 5 columns: ['Dataset', 'Id', 'Context', 'Comment', 'Target'])

#### If you want to train your model with original labels, use 'origin_*.csv' files.
#### If you want to train your model with {abusive, not abusive} labels, use 'model_*.csv' files.
We explain how we adjust the labels (origin labels -> binary labels) in our paper (please see the reference below).


For AbuseEval and CADD, there are 'origin_{train, valid, test}.csv' and 'model_{train, valid, test}.csv'.

For Davidson and Waseem, they are not divided into {train, valid, test} sets.
You can split the data depending on the ratio you want, if you need to.
In our paper, we set the ratio as 7(train):1(valid):2(test).
For Waseem, we divided the data after shuffling it. 


# References
Korean Abusive Language Dataset (Ours): 신지수, 송호윤, 이희제, 박종철. (2022). 기계번역을 활용한 한국어 언어폭력 데이터셋의 구축. 한국정보과학회 학술발표논문집. (Jisu Shin, Hoyun Song, Huije Lee, Jong C. Park, Constructing Korean Abusive Language Dataset using Machine Translation, Proceedings of the Korea Computer Congress, 2022.

AbuseEval: I Feel Offended, Don’t Be Abusive! Implicit/Explicit Messages in Offensive and Abusive Language (Caselli et al., LREC 2020) (https://aclanthology.org/2020.lrec-1.760/), Predicting the Type and Target of Offensive Posts in Social Media (Zampieri et al., NAACL 2019) (https://aclanthology.org/N19-1144/)

CADD: A Large-scale Comprehensive Abusiveness Detection Dataset with Multifaceted Labels from Reddit (Song et al., CoNLL 2021) (https://aclanthology.org/2021.conll-1.43/)

Davidson: Automated Hate Speech Detection and the Problem of Offensive Language (Davidson et al., ICWSM 2017) (https://ojs.aaai.org/index.php/ICWSM/article/view/14955)

Waseem: Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter (Waseem & Hovy, NAACL 2016) (https://aclanthology.org/N16-2013/)
