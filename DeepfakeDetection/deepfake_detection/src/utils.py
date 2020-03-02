import os
import os.path as osp
import requests
from tqdm import tqdm

def parse_cookie(cookie_txt_path):
    '''parse cookie text into dict of {name: value}'''
    cookies = []
    for line in open(cookie_txt_path):
        if line.startswith('#'):
            continue
        cookies.append([item.strip() for item in line.split()])

    res = {cookie[-2]: cookie[-1] for cookie in cookies}
    return res

def download_data(cookie_txt_path, data_idx, out_dir):
    '''download training data from deepface detection competition page
    
    Args:
        cookie_txt_path: path to cookie text
        target_idx: specify which training data to download
        out_dir: output directory
    '''
    url = 'https://www.kaggle.com/c/16880/datadownload/dfdc_train_part_{IDX:02d}.zip'.format(IDX=data_idx)
    data_file = 'dfdc_train_part_{IDX}.zip'.format(IDX=data_idx)
    cookies = parse_cookie(cookie_txt_path)

    response = requests.get(url, cookies=cookies, stream=True)
    file_size = int(response.headers["Content-Length"])

    pbar = tqdm(total=file_size, unit="B", unit_scale=True)
    os.makedirs(out_dir, exist_ok=True)
    with open(osp.join(out_dir, data_file), 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
            pbar.update(len(chunk))
        pbar.close()
