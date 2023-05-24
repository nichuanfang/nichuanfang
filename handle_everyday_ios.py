# 处理每日图片更新_ios

from imagekitio import ImageKit
import requests
from requests import Response
import base64
from PIL import Image
from io import BytesIO
import random
import sys

def save_url_image(img_url:str,height,width):
    """url保存

    Args:
        img_url (str): 图片url
        img_path (str): 保存的图片路径 
    """
    res:Response = requests.get(img_url)
    base64_data = base64.b64encode(res.content).decode()
    imgdata = base64.b64decode(base64_data)
    im = Image.open(BytesIO(imgdata))
    # im.thumbnail((height,width), Image.Resampling.LANCZOS ) #重新设置图片大小
    im.save('ios_everyday.jpg')

# imagekit公钥
public_key = sys.argv[1]
# imagekit私钥
private_key = sys.argv[2]

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
        new_file_list.append(file)

if new_file_list is None or len(new_file_list)==0:
    raise RuntimeError('imagekit的ios分类下没有图片!')

index = random.randint(0,len(new_file_list)-1)
save_url_image(new_file_list[index].url,new_file_list[index].height,new_file_list[index].width)