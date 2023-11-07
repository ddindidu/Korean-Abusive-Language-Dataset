Korean Abusive Language Dataset | 한국어 언어폭력 혐오표현 데이터셋
===============================

This is the abusive language datasets (AbuseEval, CADD, Davidson, Waseem) translated into Korean.   
*keyword: abusive language, hate speech, offensive language, reddit, social media, korean dataset*

For 4 benchmark datasets for abusive language detection, we translated and share them into Korean (You can access their papers through the references below.) .    
* AbuseEval (Caselli et al., 2020)   
* CADD (Song et al., 2021)   
* Davidson et al. (2017)   
* Waseem and Hovy (2016)   
 

The datasets have different formats, so we unified the data columns.     
We share **two types** for each dataset because each dataset has different columns. The description is below.    
## 1. origin_*.csv
> This is a Korean version of an original dataset. It preserves columns of the original datasets.
> 
> ### Here are the columns of datasets.
> * AbuseEval = {'Dataset', 'Id', 'Context', 'Comment', 'Target', 'abuse'}
> 
> * CADD = {'Dataset', 'Id', 'Context', 'Comment', 'Target', 'L.Type', 'L.Abusive', 'lAttack', 'L.Dem', 'L.Implicit', 'L.Profanity', 'lenComment', 'lenContext'}
> 
> * Davidson = {'Dataset', 'Id', 'Context', 'Comment', 'Target', 'hate_speech', 'offensive_language', 'neither', 'class'}
> 
> * Waseem = {'Dataset', 'Id', 'Context', 'Comment', 'Target', 'Annotation'}
>
> ### Details
> 5 columns which all datasets have.
> ```
> 'Dataset': the name of dataset
> 'Id'     : the Id of text data from the original dataset
> 'Context': context texts; If there is no context text in original data, data is "".
> 'Comment': texts to be classified
> 'Target' : binary labels that we refined original labels in our work {abusive (1), not abusive (0)}
> ```
> Other columns
> ```
> their original labels: refer their papers
> ```


## 2. model_*.csv
> This is a dataset for training and testing a classification model.   
> consisting of only 5 columns {'Dataset', 'Id', 'Context', 'Comment', 'Target'}


## Brief Tips🤗
### 1. Which file should I use?
#### If you want to train your model with *original labels*, use 'origin_*.csv' files.
#### If you want to train your model with *{abusive, not abusive} labels*, use 'model_*.csv' files.
We explain how we adjust the labels (origin labels -> binary labels) in our paper (please see the reference below).

### 2. How is the data divided (train / test)?
* For AbuseEval and CADD, there are 'origin_{train, valid, test}.csv' and 'model_{train, valid, test}.csv'.

* For Davidson and Waseem, they are not divided into {train, valid, test} sets in the original papers.   
You can split the data depending on the ratio you want, if you need to.   
In our paper, we set the ratio as 7(train):1(valid):2(test).   
For Waseem, we divided the data after shuffling it. 


References
==========
* Korean Abusive Language Dataset (Ours)
  ```
  # Kor
  신지수, 송호윤, 이희제, 박종철. (2022). [기계번역을 활용한 한국어 언어폭력 데이터셋의 구축](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11113351). 한국정보과학회 학술발표논문집.   

  # Eng
  @inproceedings{shin2022constructing,
   title = {Constructing Korean Abusive Language Dataset using Machine Translation},
   author = {Shin, Jisu and Song, Hoyun and Lee, Huije and Park, Jong C. Park},
   booktitle = {Proceedings of the Korea Computer Congress},
   year = {2022}
  }
  ```

* AbuseEval   
    - [I Feel Offended, Don’t Be Abusive! Implicit/Explicit Messages in Offensive and Abusive Language](https://aclanthology.org/2020.lrec-1.760) (Caselli et al., LREC 2020)
    - [Predicting the Type and Target of Offensive Posts in Social Media](https://aclanthology.org/N19-1144) (Zampieri et al., NAACL 2019)

* CADD   
    - [A Large-scale Comprehensive Abusiveness Detection Dataset with Multifaceted Labels from Reddit](https://aclanthology.org/2021.conll-1.43) (Song et al., CoNLL 2021)

* Davidson   
    - [Automated Hate Speech Detection and the Problem of Offensive Language](https://ojs.aaai.org/index.php/ICWSM/article/view/14955) (Davidson et al., ICWSM 2017) 

* Waseem   
    - [Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter](https://aclanthology.org/N16-2013) (Waseem & Hovy, NAACL 2016)
