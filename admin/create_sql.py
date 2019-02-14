#!/usr/bin/env python
#!coding: utf-8

"""
SQLを作成するスクリプトモジュール
SQLファイルに記述するINSERTとDELETE分を生成するスクリプト
各表のSQL文はここに書く

作成： okimura
"""
import datetime

def get_now_date_list():
    """
    SQLデータに挿入する日付データを生成する
    REGISTER_DATEとUPDATE_DATEに入れる日付データを生成する

    Returns
    -----------------
    list : list of str
        日付データのリスト
        例) [2018/11/11,2018/11/11]
    """
    list = []
    now = datetime.datetime.now()
    list.insert(0,"{0:%Y/%m/%d}".format(now))
    list.insert(0,"{0:%Y/%m/%d}".format(now))
    return list

def get_select_sql(table_name):
    """
    テーブルを取得するSQLを返す
    使用する側でarg1に変数を入れること

    Parameters
    ---------
    table_name : str
        表名

    Returns
    --------
    str : str
        構成物状態を取得するSQL
    """
    return "SELECT * FROM {arg}".format(arg=table_name)


def get_insert_constituent_state_sql(data):
    """
    構成物状態を挿入するSQLを返す

    Parameters
    ----------
    data : list of str
        構成物ID、登録日、更新日を含む一覧
        例）["314901382401", 2017/01/01, 2017/01/01]

    Returns
    ------
    str : str
        構成物状態表に挿入するSQLの一レコード
    """
    return "insert into constituent_state(CONSTITUENT_ID,LEVEL_ID,STATE,VERSION,OBSERVE_STATE,REGISTER_USER_ID,REGISTER_DATE,UPDATE_USER_ID,UPDATE_DATE)"\
           "values('{0}','0','1','','1','system','{1}','system','{2}');\n".format(*data)

def get_delete_constituent_state_sql(data):
    """
    構成物状態を削除するSQLを返す

    Parameters
    ----------
    data : str
        構成物ID

    Returns
    ------
    str : str
        構成物状態表から削除するSQLの一レコード
    """
    return "delete from constituent_state where constituent_id = '{0}';\n".format(*data)

def get_insert_error_code_sql(data):
    """
    エラーコードを挿入するSQLを返す

    Parameters
    ----------
    data : str
        エラーコード、対処方法、登録日、更新日を含む一覧
        例）["TERMINAL001", "すぐに連絡してください", 2017/01/01, 2017/01/01]

    Returns
    ------
    str : str
        エラーコードに挿入するSQLの一レコード
    """
    return "insert into error_code(ERROR_CODE,DEAL_METHOD,REGISTER_USER_ID,REGISTER_DATE,UPDATE_USER_ID,UPDATE_DATE)"\
           "values('{0}','{1}','system','{2}','system','{3}');\n".format(*data)

def get_delete_error_code_sql(data):
    """
    エラーコードを削除するSQLを返す

    Parameters
    ----------
    data : str
        エラーコード

    Returns
    ------
    str : str
        エラーコードを削除するSQLの一レコード
    """
    return "delete from error_code where ERROR_CODE = '{0}';\n".format(*data)

def create_insert(table_name, data):
    """
    指定した表からINSERT文を生成する

    Parameters
    ----------
    table_name : str
        表名
    data : list of str
        挿入するデータ

    Returns
    ------
    str : str
        指定した表にデータを挿入するINSERT文
        ※ 列名は指定していないので注意
    """
    return ''.join([
    'INSERT INTO ' + table_name + ' VALUES (',
    ', '.join('\'' + str(k) + '\'' for k in data),
    ');\n'])

def create_all_delete(table_name):
    """
    指定した表からINSERT文を生成する

    Parameters
    ----------
    table_name : str
        表名

    Returns
    ------
    str : str
        表をすべて削除するDELETE文
    """
    return "DELETE from {arg}".format(arg=table_name)