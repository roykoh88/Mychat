"""
Colab에서 Git push 하려면 연결(인증) 필요.
- Author identity unknown → user.email, user.name 설정
- could not read Username → remote URL에 토큰 넣기

한 번만: python script/colab_git.py connect --email 이메일 --name 이름 --token GitHub토큰
"""
import os
import subprocess
import argparse

REPO_DIR = os.environ.get("REPO_DIR", "/content/mychat")
BRANCH = os.environ.get("BRANCH", "main")
REPO = os.environ.get("GITHUB_REPO", "roykoh88/mychat")


def run(cmd, cwd=REPO_DIR):
    subprocess.run(cmd, shell=True, cwd=cwd)


def set_user(email: str, name: str):
    run(f"git config --global user.email \"{email}\"", cwd=None)
    run(f"git config --global user.name \"{name}\"", cwd=None)


def set_remote_token(token: str):
    run(f"git remote set-url origin https://{token}@github.com/{REPO}.git")


def connect(email: str, name: str, token: str = ""):
    set_user(email, name)
    if token:
        set_remote_token(token)


def pull():
    run(f"git pull origin {BRANCH}")


def push(msg: str = "update"):
    run("git add .")
    run(f"git commit -m \"{msg}\"")
    run(f"git push origin {BRANCH}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["connect", "set-user", "pull", "push", "set-token"])
    p.add_argument("--email", default="")
    p.add_argument("--name", default="")
    p.add_argument("--token", default="")
    p.add_argument("-m", "--message", default="update")
    args = p.parse_args()

    if args.action == "connect":
        connect(
            args.email or os.environ.get("GIT_EMAIL", "you@example.com"),
            args.name or os.environ.get("GIT_NAME", "Your Name"),
            args.token or os.environ.get("GITHUB_TOKEN", ""),
        )
    elif args.action == "set-user":
        set_user(args.email or "you@example.com", args.name or "Your Name")
    elif args.action == "pull":
        pull()
    elif args.action == "push":
        push(args.message)
    elif args.action == "set-token":
        set_remote_token(args.token or os.environ.get("GITHUB_TOKEN", ""))
