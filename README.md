OracleDBデータリリースツール
====
## Overview
OracleDBにリリースするためのSQLを生成するツール
DBからバックアップを取得して、マスタを上書き更新するSQLを作成します。

## Description
・フォルダ構成
 - admin
	  ├ create_import_for_master.py      … マスタをリリースするためのSQLを発行するスクリプト、DBからのバックアップも取得する
	  ├ common_util.py                   … 共通的なユーティリティモジュール
	  ├ create_sql.py                    … SQLを生成するモジュール
	  ├ create_csv.py                    … CSVを生成するモジュール
	  ├ db_controller.py                 … DB接続するモジュール
	  ├ setting.ini                      … DB接続設定ファイル
	  ├ /output                          … 出力したSQLファイルを格納するディレクトリ
	  ├ /backup                          … バックアップしたSQLファイルを格納するディレクトリ
	  └ /data                            … CSVをインポートするためのディレクトリ
 - sample_table_sql                       … 動作確認用SQL格納ディレクトリ
 - README.md                              … 本ドキュメント

## Requirement
・動作環境
   - Windows10 Pro（他OSは未検証）
   - Python v3.6
   - Oracle DB 12.2c（他Verは未検証）
   - Oracle Client(Oracle Database 12.2c対応)
   - Microsoft Visual C++ Redistributable for Visual Studio 2017

・必要なPythonプラグイン
   - [Pandas](https://pypi.org/project/pandas/)
   - [numpy](https://pypi.org/project/numpy/)
   - [pytz](https://pypi.org/project/pytz/)
   - [six](https://pypi.org/project/six/)
   - [cx_Oracle](https://pypi.org/project/cx-Oracle/)
   - [python-dateutil](https://pypi.org/project/python-dateutil/)
   
・入力するCSVの制約
   - ヘッダーなし
   - 囲い文字無し
   - ファイル名はテーブル名

## Usage
1 adminフォルダ上で、エクスプローラーで開きます。

2 dataフォルダに、リリースするためのCSVファイルを配置します。

3 「create_import_for_master.py」をダブルクリックします。

## Author
Okimura(okimurak0901@gmail.com)

## Sample
sample_table_sqlフォルダにテーブルの作成SQLと、入力データ例を配置しておきます。