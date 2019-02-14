#!/usr/bin/env python
#!coding: utf-8

"""
CSVからDBのリリースするためのINSERT文を生成するスクリプト
作成： okimura

使用前に、README.mdを参照してください。

・IGNORE_MASTER_LISTに含まれるCSVは読み込みません。
  変更する場合には、IGNORE_MASTER_LISTを編集してください
"""
import sys, math, glob, os
import pandas as pd
import numpy as np
# 自作モジュール
import common_util as common
import db_controller as dbcon
import create_sql
import create_csv

# 文字コード
CHAR_CODE='UTF-8'
# 読み込むディレクトリ
INPORT_RELEASE_PATH = './data/'
# 出力するディレクトリ
INSERT_SQL_PATH = "./output/"
# 例外マスタ名
IGNORE_MASTER_LIST = ["ITEM", "ERROR_CODE"]

# デバッグ用
DEBUG = False

def write_sql(file, write_list, table_name):
    """
    SQLファイルに書き込む
    
    Paramater
    --------
    file : str
        出力するSQLファイルのパス
    write_list : list of str
        構成物IDの一覧
    table_name : str
        表名
    """
    with open(file, "wt", encoding=CHAR_CODE) as fw:
        fw.write(create_sql.create_all_delete(table_name))
        for item in write_list:
            # 要素が複数あるのでリストをそのまま使う
            list = item
            # 小数を丸める(小数含むマスタができたら終わるな
            list = [round(i) if isinstance(i,float) else i for i in list]

            if(DEBUG):
                print(list)

            fw.write(create_sql.create_insert(table_name, list))

def export_sql(df, export_path, table_name):
    """
    挿入するSQLを生成する
    
    Paramater
    --------
    df : dataFrame
        ファイル名(拡張子付)
    export_path : str
        SQLを出力するパス
    table_name : str
        表名
    """
    if(common.isEmpty(df)):
        print("挿入するデータはありません")
    else:
        # リストに変換
        sql_list = df.values.tolist()
        ## SQLに書き込み
        write_sql(export_path, sql_list,table_name)


def read_master(filename):
    """
    CSVを読み込んでIMSERT文を出力する

    Paramater
    --------
    filename : str
        ファイル名(拡張子付)
    """
    # CSV読み込み
    path = INPORT_RELEASE_PATH + filename + ".csv"
    df = pd.read_csv(path,encoding=CHAR_CODE, header=None, dtype=str)

    if(DEBUG):
        print('読み込んだCSVデータ')
        print(df.head())

    # nanを処理
    df = df.fillna('')

    # 出力先生成
    export_path = INSERT_SQL_PATH + filename + ".sql"
    print("出力先：" + export_path)

    # 出力
    export_sql(df, export_path, filename)


def main():
    """
    メイン処理
    """

    # ファイル一覧を取得
    filelist = [os.path.splitext(os.path.basename(r))[0] for r in glob.glob(INPORT_RELEASE_PATH + "*.csv")]

    print("dataフォルダ")
    print(filelist)

    # 例外リストに部分一致するファイルをファイル一覧から削除する
    for ignore in IGNORE_MASTER_LIST:
        filelist = [item for item in filelist if ignore not in item]

    print("出力対象")
    print(filelist)

    # DBからCSVにバックアップをとる
    for item in filelist:
        conn = dbcon.connect_oracle()
        result = dbcon.send_select(conn, item)
        create_csv.output_csv(INPORT_RELEASE_PATH, item, result[0], result[1])
        conn.close()

    # csvからIMSERT文を生成
    for item in filelist:
        read_master(item)

if __name__ == '__main__':
    # メイン処理を実行
    main()
