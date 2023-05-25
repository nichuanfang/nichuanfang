import requests
import json
import sys

# github密钥
github_token = sys.argv[1]
# github用户名
github_username = sys.argv[2]
# github项目名
github_project = sys.argv[3]
# github工作流id    workflowId可以通过https://api.github.com/repos/用户名/仓库名称/actions/workflows 查看
github_workflow_id = sys.argv[4]

def run():
        payload = json.dumps({"ref": "main"})
        header = {'Authorization': github_token,
                  "Accept": "application/vnd.github.v3+json"}
        response_decoded_json = requests.post(
            f'https://api.github.com/repos/{github_username}/{github_project}/actions/workflows/{github_workflow_id}/dispatches',
            data=payload, headers=header)

# 云函数入口
def main_handler(event, context):
    return run()
