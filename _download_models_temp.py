from huggingface_hub import snapshot_download
for name in ['unsloth/meta-llama-3.1-8b-unsloth-bnb-4bit', 'unsloth/llama-3.2-1b-bnb-4bit']:
    print('[다운로드]', name)
    snapshot_download(repo_id=name)
    print('[완료]', name)
print('전체 다운로드 완료.')
