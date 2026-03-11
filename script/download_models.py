"""
베이스 모델 미리 다운로드 (Hugging Face 캐시에 저장).

실행: 프로젝트 루트(mychat)에서
  python scripts/download_models.py
"""
from unsloth import FastLanguageModel

BASE_MODELS = [
    "unsloth/meta-llama-3.1-8b-unsloth-bnb-4bit",  # 교육 QA
    "unsloth/llama-3.2-1b-bnb-4bit",               # 사내 메뉴얼
]

if __name__ == "__main__":
    for name in BASE_MODELS:
        print(f"[다운로드] {name}")
        FastLanguageModel.from_pretrained(
            model_name=name,
            max_seq_length=2048,
            dtype=None,
            load_in_4bit=True,
        )
        print(f"[완료] {name}")
    print("전체 다운로드 완료.")
