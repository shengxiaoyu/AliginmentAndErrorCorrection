#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'

#肯定/否定词集
NEGATION = {}
NEGATION['NEGATIVE'] = ['捏造','诬陷','猜疑','诬告','有误','不','未','无','没']
NEGATION['POSITIVE'] = ['合适','属实','确定','确认','确实','确有','认定','认可','事实','是','有的','一致','承认','有','证明','准确']


#初婚/再婚词集
REMARRY = {}
REMARRY['REMARRY'] = ['第二次结婚','二婚','复婚','结过婚','均是离异','离异','两人离婚后走到一起','已结婚、离婚多次','再婚','在婚']
REMARRY['FIRST_MARRY'] = ['初次结婚','初婚','第一次结婚']

FAMILY_CONFLICT_POSITIVE=['对原告百般挑剔甚至动手的事实不属实','有共同语言','感情尚未破裂','感情一直很好','我对公婆是非常尊重的','不存在夫妻生活不和谐','双方关系尚好','感情一直很好',
                          '感情来看都是很好的','感情一直很好','感情没有破裂','感情是好的','感情尚好','感情没有破裂','感情并未破裂']

GENDER = {}
GENDER['M'] = ['男','子']
GENDER['F'] =  ['女']

UP_TO_DATE = ['至今']

if __name__ == '__main__':
    pass