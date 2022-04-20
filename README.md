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
...희제가 7:1:2로 나눠서 씀
...Davidson은 셔플 안 하고 나눴고
...Waseem은 셔플(아마 seed=42)하고 중복제거 한 뒤에 7:1:2


# origin_* 에 대한 설명
# 모든 데이터의 앞 5개 컬럼은 다 같음. (데이터명, 아이디, context, comment(대상), target(폭력성 0/1)

# 'abuse'는 3 classes (NOTABU: 비폭력, EXP: 명시적 폭력, IMP: 암묵적 폭력)
AbuseEval = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'abuse']

# 'L
CADD = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'L.Type', 'L.Abusive', 'lAttack', 'L.Dem', 'L.Implicit', 'L.Profanity', 'lenComment', 'lenContext']

# 'class'는 3 classes (0: hate speech, 1: offensive language, 2: neither)
Davidson = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'hate_speech', 'offensive_language', 'neither', 'class']

# 'Annotation'은 3 classes (sexism, racism, neither)
Waseem = ['Dataset', 'Id', 'Context', 'Comment', 'Target', 'Annotation']
