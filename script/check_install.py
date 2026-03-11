"""
설치된 라이브러리(requirements.txt 기준) 확인.

실행: 프로젝트 루트에서
  python script/check_install.py
"""
PACKAGES = [
    "fastapi",
    "uvicorn",
    "jinja2",
    "unsloth",
    "huggingface_hub",
]

def main():
    print("설치된 라이브러리 확인\n")
    for name in PACKAGES:
        try:
            mod = __import__(name.replace("-", "_"))
            ver = getattr(mod, "__version__", "?")
            print(f"  {name}: {ver}")
        except ImportError:
            print(f"  {name}: (미설치)")
    print("\n전체 목록: pip list | grep -E 'fastapi|uvicorn|jinja|unsloth|huggingface'")

if __name__ == "__main__":
    main()
