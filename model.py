#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'
from enum import Enum
import datetime
class Entity(object):
    def __init__(self, id, type, begin, end, value):
        self.id = id.strip()
        self.type = type.strip()
        self.begin = int(begin)
        self.end = int(end)
        self.value = value.strip()

class Event(object):
    def __init__(self, id, type, trigger):
        self.id = id.strip()
        self.type = type
        self.trigger = trigger
        self.sentence = None
        self.begin_index = 0
        self.speaker = None
    def setArgu(self,argu_name,argu_value):
        setattr(self,argu_name,argu_value)
    def addSent(self,sent):
        if(self.sentence ==None):
            self.sentence = sent
        else:
            self.sentence += sent

    def __str__(self):
        res = 'id:'+self.id+', '
        if(self.type==None):
            print('Pause')
        res += 'type:'+self.type.value+', '
        if(hasattr(self,'Negation')):
            res+='Negation:'+self.Negation.value
        res += 'trigger:'+self.trigger.value+', '
        if(hasattr(self,'Time')):
            res += 'Time:'+self.Time.value+', '
        if(hasattr(self,'Participant')):
            res += 'Participant:'+self.Participant.value+', '
        if(hasattr(self,'ChildName')):
            res += 'ChildName:'+self.ChildName.value+', '
        if(hasattr(self,'DateOfBirth')):
            res += 'DateOfBirth:'+self.DateOfBirth.value+', '
        if(hasattr(self,'Gender')):
            res += 'Gender:'+self.Gender.value+', '
        if(hasattr(self,'Age')):
            res += 'Age:'+self.Age.value+', '
        if(hasattr(self,'Perpetrators')):
            res += 'Perpetrators:'+self.Perpetrators.value
        if(hasattr(self,'Victim')):
            res += 'Victim:'+self.Victim.value
        if(hasattr(self,'Derailer')):
            res += 'Derailer:'+self.Derailer.value+', '
        if(hasattr(self,'BeginTime')):
            res += 'BeginTime:'+self.BeginTime.value+', '
        if(hasattr(self,'EndTime')):
            res += 'EndTime:'+self.EndTime.value+', '
        if(hasattr(self,'Duration')):
            res += 'Duration:'+self.Duration.value+', '
        if(hasattr(self,'SueTime')):
            res += 'SueTime:'+self.SueTime.value+', '
        if(hasattr(self,'Initiator')):
            res += 'Initiator:'+self.Initiator.value+', '
        if(hasattr(self,'Court')):
            res += 'Court:'+self.Court.value+', '
        if(hasattr(self,'Result')):
            res += 'Result:'+self.Result.value+', '
        if(hasattr(self,'JudgeTime')):
            res += 'JudgeTime:'+self.JudgeTime.value+', '
        if(hasattr(self,'JudgeDocument')):
            res += 'JudgeDocument'+self.JudgeDocument.value+', '
        if(hasattr(self,'Value')):
            res += 'Value:'+self.Value.value+', '
        if(hasattr(self,'IsPersonal')):
            res += 'IsPersonal:'+self.IsPersonal.value+', '
        if(hasattr(self,'Whose')):
            res += 'Whose:'+self.Whose.value+', '
        if(hasattr(self,'IsCommon')):
            res += 'IsCommon:'+self.IsCommon.value+', '
        if(hasattr(self,'Creditor')):
            res += 'Creditor:'+self.Creditor.value+', '
        if(hasattr(self,'Debtor')):
            res += 'Debtor:'+self.Debtor.value+', '
        res =res.strip()
        if(res.endswith(',')):
            res = res[:-1]
        return res

class Relation(object):
    def __init__(self,id, type, arg1, arg2):
        self.id = id
        self.type = type

        #事件id，保证小id为arg1,大id为arg2
        id_index_1 = int(arg1.id[1:])
        id_index_2 = int(arg2.id[1:])

        if(id_index_1>id_index_2):
            self.arg1 = arg2
            self.arg2 = arg1
        else:
            self.arg1 = arg1
            self.arg2 = arg2

    def __eq__(self, other):
        if(other==None):
            return False
        if(self.arg1==other.arg1 and self.arg2==other.arg2):
            return True
        return False

class event_types(Enum):
    KNOW = 'Know'
    BE_IN_LOVE = 'BeInLove'
    MARRY = 'Marry'
    REMARRY = 'Remarry'
    BE_BORN = 'Bear'
    FAMILY_CONFLICT = 'FamilyConflict'
    DOMESTIC_VIOLENCE = 'DomesticViolence'
    BAD_HABIT = 'BadHabit'
    DERAILED = 'Derailed'
    SEPARATION = 'Separation'
    DIVORCE_LAWSUIT = 'DivorceLawsuit'
    WEALTH = 'Wealth'
    DEBT = 'Debt'
    CREDIT = 'Credit'

    def get_event_type(text):
        text = text.strip()
        for item in event_types:
            if(item.value==text):
                return item


class parties(Enum):
    '''原告'''
    PLAINTIFF = '原告'
    '''被告'''
    DEFENDANT = '被告'


class habit_types(Enum):
    GAMBLING = '赌博'
    WINE = '酗酒'
    DRUG = '吸毒'
    '''嫖娼'''
    SEXUAL = '嫖娼'
    '''传销'''
    MLM = '传销'
    '''网瘾'''
    NETWORK = '网瘾'
    '''偷抢'''
    THEFT = '偷抢'
    '''打架斗殴'''
    FIGHT = '斗殴'
    '''诈骗'''
    FRAUD = '诈骗'


class myDate(object):

    @staticmethod
    def getNow():
        now = datetime.datetime.now()
        return myDate(now.year,now.month,now.day)

    def __init__(self,year,month,day):
        self.year = None if year==None else int(year)
        self.month = None if month==None else int(month)
        self.day = None if day==None else int(day)

    '''时间的比较，如果可以相互蕴含则返回0，如果大返回1，小返回-1'''
    @staticmethod
    def compareTo(date_a, date_b):
        if(date_a==None or date_b==None):
            return 0
        if(date_a.year!=None and date_b.year!=None):
            if(date_a.year>date_b.year):
                return 1
            elif(date_a.year<date_b.year):
                return -1
        if(date_a.month!=None and date_b.month!=None):
            if(date_a.month>date_b.month):
                return 1
            elif(date_a.month<date_b.month):
                return -1
        if(date_a.day!=None and date_b.day!=None):
            if(date_a.day>date_b.day):
                return 1
            elif(date_a.day<date_b.day):
                return -1
        return 0

if __name__ == '__main__':
    var = event_types.get_event_type('Marry')
    print(var)