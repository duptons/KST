# *-- coding: utf-8 --*
# Liebe, 2015-10-31
import os, sys
from pprint import pprint
import re
import ast

"""
setting:
    字段  名称   处理函数   被处理表达式   结果要求
    rns  NAME  DP_NUMBER   EVAL_EXPR   PARAM_LIST
"""
data_collection = {
    'd_src': 'ifind',
    'd_pre': {
        'sql': 'SELECT * A a WHERE a.a1 = a.a2'
    },
    'd_list': [
        {'r1s': ('NAME1', 'DP_NUMBER', 'r1s*50', ['ROUND'])},
        {'r2s': ('NAME2', 'DP_STRING', 'r2s+":->"+rs1', ['UPPER'])},
        {'r3s': ('NAME3', 'DP_DATE'  , 'r3s', ['FORMAT=>YYYY年 m-dd号'])},
        {'r4s': ('NAME4', 'DP_NUMBER', 'r4s*100', [])},
    
        {'r5s': ('NAME5', 'DP_NUMBER', 'r1s/r4s', ['PERCENT', 'FLOAT=>3', ''])},
        {'r6s': ('NAME6', 'DP_NUMBER', 'r5s/(r4s+180)', [])},
        {'r7s': ('NAME7', 'DP_NUMBER', 'r5s+r6s-r1s', ['FLOAT=>2'])},
        {'r8s': ('NAME8', 'DP_NUMBER', '(r1s + r4s + r5s + r6s + r7s)/5', ['FLOAT=>1'])}
    ]
}
    
def DP_FUN(dict_exist, dp_data):
    for key, val in dict_exist.items():
        if isNum(val):
            exec(key + ' = ' + str(val))
    if dp_data[0] == 'DP_NUMBER':
        try:
            expr_val = eval(dp_data[1])
            if str(type(dp_data[2]))=="<type 'list'>":
                for param in dp_data[2]:
                    (flag, resv) = DP_FUN_PARAM(dp_data[0], expr_val, param)
                    if flag == True:
                        expr_val = resv
                    else:
                        return (False, 'FUN: DP_NUMBER\n' +  'FUN_PARAM: ' + param + '\nRESV: ' + resv)
            if isNum(expr_val) == True:
                return (True, expr_val)
        except:
            return (False, 'FUN: DP_NUMBER')
    elif dp_data[0] == 'DP_STRING':
        return (True, 'DP_STRING')
    elif dp_data[0] == 'DP_DATE':
        return (True, 'DP_DATE')
    else:
        return (True, 'UNEXPECTED')

def DP_FUN_PARAM(dp_fun, dp_expr, dp_param):
    if dp_fun == 'DP_NUMBER' and isNum(dp_expr):
        res_expr = ''
        if len(dp_param) <= 0:
            res_expr = dp_expr
            return (True, res_expr)
        if dp_param == 'ROUND':
            res_expr = round(dp_expr)
            return (True, res_expr)
        f_type = re.compile('FLOAT=>([\d]+)').findall(dp_param)
        if len(f_type) > 0:
            res_expr = float(('%.'+f_type[0]+'f') % dp_expr)
            return (True, res_expr)
        if dp_param == 'PERCENT':
            res_expr = dp_expr * 100
            return (True, res_expr)

def isNum(resv):
    try:
        resv + 1
    except:
        return False
    else:
        return True

def process():
    (old_dict, new_dict) = ({}, {})
    if data_collection['d_src'] == 'ifind':
        old_dict = {
            'r1s': -123.45,
            'r2s': 'fuck U',
            'r3s': '2015-11-01',
            'r4s': -80.00
        }
    else:
        return (False, 'DATA SOURCE ERROE!')
    if len(old_dict) > 0:
        new_dict = old_dict
    else:
        return (False, 'GET NO DATA!')

    for each_data in data_collection['d_list']:
        (key, val) = each_data.items()[0]
        val = list(val)[1:]
        (flag, resv) = DP_FUN(new_dict, val)
        if flag == True:
            new_dict[key] = resv
        else:
            continue
    return (True, new_dict)

# yunxin
pprint(process())
