#coding=gbk

import os
import zipfile


import os
import zipfile


def zip_dir(dir_path, zip_path):
    '''

    :param dir_path: Ŀ���ļ���·��
    :param zip_path: ѹ������ļ���·��
    :return:
    '''
    zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')  # ȥ����·����ֻ��Ŀ���ļ����µ��ļ����ļ��н���ѹ��
        # ѭ����һ�����ļ���
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
    zip.close()


