# Colab에서 실행하기

레포 클론 후 아래 셀을 **순서대로** 실행하세요.

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
