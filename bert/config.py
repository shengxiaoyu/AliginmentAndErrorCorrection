#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'
import os

#windows
base_dir = r'A:\研二2\Bi-LSTM+CRF\bert'
#linux
# base_dir ='/home/bert2/myBert'

# event_type='结婚'

data_dir=os.path.join(base_dir,'data')

task_name='similar'

bert_model_dir = os.path.join(base_dir,'chinese_L-12_H-768_A-12')
vocab_file=os.path.join(bert_model_dir,'bert_config.json')
bert_config_file=os.path.join(bert_model_dir,'bert_config.json')
init_checkpoint=os.path.join(bert_model_dir,'bert_model.ckpt')

#init_checkpoint=os.path.join(output_dir,'bert_model.ckpt')
output_dir = os.path.join(base_dir,'output')

do_train=True
do_dev=False
do_predict = True



if __name__ == '__main__':
    pass