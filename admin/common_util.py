#!/usr/bin/env python
#!coding: utf-8

"""
共通的なユーティリティを提供するモジュール
作成： okimura
"""

import datetime

def isEmpty(df):
    """
    データフレームが空かどうか

    Parameter
    ---------
    df : dataFrame
        データフレーム

    Returns
    -----------------
    boolean : boolean
        true:dfが空 false:dfは空ではない
    """
    return len(df.index) == 0

def convertNoneToBlank(rows):
    """
    DBテーブルのような二次元配列をに含まれるNoneをブランク文字に変換する

    Parameter
    ---------
    rows : rows
        2次元配列

    Returns
    -----------------
    rows : rows
        Noneを""に変換した2次元配列
    """
    for i in range(len(rows)):
        rows[i] = ['' if x is None else x for x in rows[i]]
    return rows

def convertDateTimeToString(rows):
    """
    DBテーブルのような二次元配列をに含まれるNoneをブランク文字に変換する

    Parameter
    ---------
    rows : rows
        2次元配列

    Returns
    -----------------
    rows : rows
        datetime.datetimeを文字列に変換した2次元配列
    """
    for i in range(len(rows)):
        rows[i] = [y.strftime('%y-%m-%d') if isinstance(y, datetime.datetime) else y for y in rows[i]]
    return rows