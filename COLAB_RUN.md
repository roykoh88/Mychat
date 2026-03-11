# Colab에서 실행하기

레포 클론 후 아래 셀을 **순서대로** 실행하세요.

---

## 0) 부분 폴더만 가져오기 (선택)

전체 클론 대신 **특정 폴더만** 받고 싶을 때 사용.

### 방법 A: Git Sparse Checkout (Git 2.25+)

```python
# 1) 빈 클론
!git clone --filter=blob:none --sparse https://github.com/USERNAME/mychat.git
%cd mychat

# 2) 가져올 폴더만 지정 (여러 개 가능)
!git sparse-checkout set script
# 예: script + 루트 파일만
# !git sparse-checkout set script requirements.txt _download_models_temp.py

# 3) 해당 폴더만 채워짐
!ls -la
```

### 방법 B: SVN으로 폴더만 체크아웃

```python
# script 폴더만 받기 (trunk = 기본 브랜치)
!svn export https://github.com/USERNAME/mychat/trunk/script ./script
# 루트 파일이 필요하면 추가
# !svn export https://github.com/USERNAME/mychat/trunk/requirements.txt ./
```

### 방법 C: Hugging Face Hub에서 **지정한 파일만** (py 없이, 노트북에 붙여넣기)

```python
# 셀에 그대로 붙여넣기. 추가한 파일만 받음 (전체 레포 X)
from huggingface_hub import hf_hub_download
import os

REPO = "roykoh88/mychat"  # 본인 레포
FILES = ["finetuning_data/company_rules_qa_ko.csv"]  # 받을 파일만
LOCAL = "/content/mychat"  # 저장할 폴더 (없으면 생성)

for path in FILES:
    dest = os.path.join(LOCAL, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    hf_hub_download(repo_id=REPO, filename=path, local_dir=LOCAL, local_dir_use_symlinks=False)
    print("[OK]", path)
```

- 비공개 레포면 `hf_hub_download(..., token=os.environ.get("HF_TOKEN"))` 추가.

### 방법 D: GitHub raw로 단일 파일

```python
# 단일 파일 (raw URL)
!wget -q https://raw.githubusercontent.com/USERNAME/mychat/main/script/download_models.py -O download_models.py
```

- **공개 레포**: 위에서 `USERNAME`만 본인 계정으로 바꾸면 됨.  
- **비공개**: A는 토큰 포함 URL, B/C는 인증이 필요해 제한적일 수 있음.

---

## 1) 런타임 설정 (모델 다운로드/학습 시)

- **런타임 → 런타임 유형 변경 → GPU** 선택 후 저장

---

## 2) 레포 이동 (이미 클론했다면)

```python
%cd /content/mychat   # 클론한 폴더 이름이 다르면 그에 맞게 수정
```

---

## 3) 패키지 설치

```python
!pip install -q -r requirements.txt
```

(모델만 미리 받고 싶을 때는 `huggingface_hub`만 있어도 됨:  
`!pip install -q huggingface_hub`)

---

## 4-A) 모델만 미리 다운로드 (가벼운 방법)

```python
!python _download_models_temp.py
```

---

## 4-B) Unsloth로 베이스 모델 다운로드 (GPU 필요, 나중에 학습용)

```python
!python script/download_models.py
```

---

## 5) 모델/어댑터 경로 확인 (선택)

```python
!python script/check_models.py
```

---

## 6) 웹 앱 실행

- 앱 코드가 있으면 로컬에서 `uvicorn <모듈>:app --reload` 로 실행.
- Colab에서 서버를 띄우면 **ngrok** 등 터널링이 필요합니다.
