#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:25:31 2019

@author: hcb
"""
import os


class Config:
    # for data_process.py
    #root = r'D:\ECG'
    root = r'/home/hcb/桌面/ecg_pytorch-master'
    train_dir = os.path.join(root, 'hf_round2_train')
#    test_dir = os.path.join(root, 'testA')
    train_label = os.path.join(root, 'hf_round2_train.txt')
#    test_label = os.path.join(root, 'hf_round1_subA.txt')
    test_dir = '/tcdata/hf_round2_testB'
    test_label = '/tcdata/hf_round2_subB.txt'
    arrythmia = os.path.join('hf_round2_arrythmia.txt')
    train_data = 'path/train'

    # for train
    #训练的模型名称
    model_name = 'myecgnet'
    #在第几个epoch进行到下一个state,调整lr
    stage_epoch = [5, 10, 15, 20, 25, 30]
    #训练时的batch大小
    batch_size = 32
    #label的类别数
    num_classes = 34
    #最大训练多少个epoch
    max_epoch = 35
    #目标的采样长度
    target_point_num = 5000
    #保存模型的文件夹
    ckpt = '../train/ckpt1'
    
    ckpt2 = '../train/ckpt2'
    #保存提交文件的文件夹
    sub_dir = 'submit'
    #初始的学习率
    lr = 1e-4 * 4
    #保存模型当前epoch的权重
    current_w = 'current_w.pth'
    #保存最佳的权重
    best_w = 'best_w.pth'
    # 学习率衰减 lr/=lr_decay
    lr_decay = 1.32

    #for test
    temp_dir = os.path.join(root, 'temp')


config = Config()
