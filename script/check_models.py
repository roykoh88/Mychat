"""
모델(어댑터) 경로와 설정 확인.

실행: 프로젝트 루트에서
  python scripts/check_models.py
"""
import json
import os

# config 없이 경로만 사용 (루트 기준)
BOT_CONFIG = {
    "education": "사내교육QA",
    "manual": "yjkoh/a",
}

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    print("모델(어댑터) 확인\n")
    for bot_id, path in BOT_CONFIG.items():
        full = os.path.join(root, path)
        config_path = os.path.join(full, "adapter_config.json")
        adapter_path = os.path.join(full, "adapter_model.safetensors")

        exists = os.path.isdir(full)
        has_config = os.path.isfile(config_path)
        has_adapter = os.path.isfile(adapter_path)

        print(f"[{bot_id}] {path}")
        print(f"  디렉터리: {'있음' if exists else '없음'}")
        print(f"  adapter_config.json: {'있음' if has_config else '없음'}")
        print(f"  adapter_model.safetensors: {'있음' if has_adapter else '없음'}")

        if has_config:
            with open(config_path, encoding="utf-8") as f:
                cfg = json.load(f)
            base = cfg.get("base_model_name_or_path", "?")
            print(f"  베이스 모델: {base}")
        print()
    print("실제 로딩 확인은 앱 실행 후 질문 한 번 보내보면 됩니다.")

if __name__ == "__main__":
    main()
