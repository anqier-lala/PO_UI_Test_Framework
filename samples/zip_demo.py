#coding=gbk
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

current_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join( current_path , '..' , 'reports/�����Զ������Ա���V1.0')

zip_dir( dri_path , dri_path+'/../�����Զ������Ա���.zip')
