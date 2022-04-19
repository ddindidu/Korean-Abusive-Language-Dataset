# Korean-Abusive-Language-Dataset

각 데이터마다 컬럼이 달라서 두 개 만듦
1. origin_*: 일반 데이터 번역하고 각기 다른 컬럼
2. model_*: 모델에 돌리는 용 (총 5 컬럼: ['Dataset', 'Id', 'Context', 'Comment', 'Target']) ~ Target은 Abusive or Not임

***따라서 cls 모델에는 model_*.csv 파일 쓰면 됨

===AbuseEval / CADD===
origin_train, origin_valid, origin_test, model_train, model_valid, model_test
다 있음

===Davidson / Waseem ===
셋으로 안 나뉘어져 있음. 필요시 나눠서 쓸 것.
