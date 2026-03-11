"""
파인튜닝용 데이터 준비: CSV → JSONL.

실행: 프로젝트 루트에서
  python script/prepare_data.py
"""
import csv
import json
import os

# 경로 (루트 기준)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_CSV = os.path.join(ROOT, "finetuning_data", "company_rules_qa_ko.csv")
DST_JSONL = os.path.join(ROOT, "finetuning_data", "company_rules_qa_ko.jsonl")


def main():
    os.chdir(ROOT)
    if not os.path.isfile(SRC_CSV):
        print(f"파일 없음: {SRC_CSV}")
        return

    count = 0
    with open(SRC_CSV, newline="", encoding="utf-8") as f_in, open(
        DST_JSONL, "w", encoding="utf-8"
    ) as f_out:
        reader = csv.DictReader(f_in)
        for row in reader:
            item = {
                "instruction": row["question"],
                "input": "",
                "output": row["answer"],
                "rule": row["rule"],
                "category": row["category"],
            }
            f_out.write(json.dumps(item, ensure_ascii=False) + "\n")
            count += 1

    print(f"완료: {count}건 → {DST_JSONL}")


if __name__ == "__main__":
    main()
