# 处理每日图片更新_ios

from imagekitio import ImageKit
from imagekitio.client import ImageKitRequest
from imagekitio.models.MoveFileRequestOptions import MoveFileRequestOptions
import requests
from requests import Response
import random
import sys

# imagekit公钥
public_key = sys.argv[1]
# imagekit私钥
private_key = sys.argv[2]

def save_url_image(img_url:str,ik_request:ImageKitRequest):
    """url保存

    Args:
        img_url (str): 图片url
        img_path (str): 保存的图片路径 
    """
    # 组装请求
    header = ik_request.create_headers()
    res:Response = requests.get(img_url,headers=header,stream=True)
    with open('dist/ios_everyday.jpg', 'wb') as f:
        f.write(res.content) 

imagekit =ImageKit(
    private_key=f'{private_key}',
    public_key=f'{public_key}',
    url_endpoint='https://ik.imagekit.io/fgro7ei9m'
)
file_list = imagekit.list_files().list

if file_list is None or len(file_list)==0:
    raise RuntimeError('imagekit没有图片!')

new_file_list = []

for file in file_list:
    if file.file_path.startswith('/ios'):
        if file.height<file.width:
            # move
            options = MoveFileRequestOptions(file.file_path,'/nichuanfang')
            imagekit.move_file(options)
        file_name:str = file.name # type: ignore
        if file_name.split('.')[0].endswith('副本') or file_name.split('.')[0].endswith('_1_'):
            imagekit.delete_file(file.file_id) # type: ignore
            continue
        new_file_list.append(file)

if new_file_list is None or len(new_file_list)==0:
    raise RuntimeError('imagekit的ios分类下没有图片!')

index = random.randint(0,len(new_file_list)-1)

# https://imagekit.io/api/v1/files/646deda206370748f2327eee/download?fileName=zq-lee-_FkDmO8oYjg-unsplash.png
# 组装url
download_url = f'https://imagekit.io/api/v1/files/{new_file_list[index].file_id}/download?fileName={new_file_list[index].name}'
save_url_image(download_url,imagekit.ik_request)