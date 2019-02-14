#!/usr/bin/env python
#!coding: utf-8

"""
CSVへ出力するモジュール

作成： okimura

"""
import csv

def output_csv(output_path, table_name, rows, header):
    """
    CSVへの出力を行う

    Parameters
    ---------------
    output_path : str
        出力先ディレクトリ
    table_name : str
        表名
    rows : rows
        2次元配列
    header : list of str
        DBのカーソル
    """
    with open(output_path + "BACKUP." + table_name + ".csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)# 改行コードと囲み文字を指定
        csv_writer.writerow(header) # ヘッダーを追加
        csv_writer.writerows(rows) 