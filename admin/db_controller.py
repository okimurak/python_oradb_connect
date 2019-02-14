#!/usr/bin/env python
#!coding: utf-8

"""
DBへ操作するためのモジュール

DBへ接続して、SQLを発行する

作成： okimura

"""

import cx_Oracle, os, configparser

# 自作モジュール読み込み
import create_sql
import common_util as common

def setEnv():
    """
    環境変数の設定を行う

    Returns
    -----------------
    config : ConfigParser
    設定オブジェクト
    """
    # 扱う文字コードの設定
    os.environ["NLS_LANG"] = "Japanese_Japan.UTF8"

    config = configparser.ConfigParser()
    config.read('setting.ini')

    return config

def connect_oracle():
    """
    OracleDBに接続する

    Returns
    -----------------
    conn : Connection
        DBのコネクション

    Exception
    -----------------
    cx_Oracle.DatabaseError
        DBに接続できなかった際にスローされる
    """
    # 環境変数設定
    config = setEnv()
    setting = 'Oracle'

    try: 
        tns = cx_Oracle.makedsn(config.get(setting, 'host'), config.get(setting, 'port'), config.get(setting, 'servicename'))
        conn = cx_Oracle.connect(config.get(setting, 'user'), config.get(setting, 'password'), tns)
        return conn

    except(cx_Oracle.DatabaseError) as ex:
        error, = ex.args
        print(error.message)

def send_select(conn, table_name):
    """
    指定した表にSELECT文を実行し
    結果をヘッダー付きで返す

    Parameters
    ---------------
    conn : Connection
        DBのコネクション
    
    table_name： str
        表名

    Returns
    -----------------
    row : list of list of str
        SELECT文を実行した結果(ヘッダー付)

    Exception
    -----------------
    cx_Oracle.DatabaseError
        DBに接続できなかった際にスローされる
    """
    # SELECT文を発行
    try:
        cur = conn.cursor()
        cur.execute(create_sql.get_select_sql(table_name))
        rows = cur.fetchall()                    
        # Noneの変換処理
        rows = common.convertNoneToBlank(rows)
        # datetime.datetimeの変換処理
        rows = common.convertDateTimeToString(rows)
        # ヘッダーの取得
        header = [i[0] for i in cur.description]

        cur.close()

        return rows, header

    except(cx_Oracle.DatabaseError) as ex:
        error, = ex.args
        print(error.message)
