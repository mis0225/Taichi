"""

 クリックされた配信先とクリックされなかった配信先を配信中の全データから分割するプログラムです

"""

import pandas as pd

# rawdata_file：配信中の全データ(※’’内を指定のパスに置き換えてください)
rawdata_file = r'C:\Users\齊藤未来\xlautomate\data\rawdata.xlsx'

# clickdata_file：クリックされた配信先データ(※’’内を指定のパスに置き換えてください)
clickdata_file = r'C:\Users\齊藤未来\xlautomate\data\clickdata.xlsx'

# output_folder：出力する新規ファイルを格納するフォルダ(※’’内を指定のパスに置き換えてください)
output_folder = r'C:\Users\齊藤未来\xlautomate\output'

# 重複のないメールアドレスと対応する行の情報を格納するリスト
result_data = []

# rawdata.xlsxのデータを読み込み
rawdata_df = pd.read_excel(rawdata_file)
rawdata_emails = rawdata_df['E-Mail'].tolist()  # 項目名：E-Mailのデータをリストとして取得（※任意の項目名に置き換えてください）

# clickdata.xlsxのデータを読み込み
clickdata_df = pd.read_excel(clickdata_file)
clickdata_emails = clickdata_df['E-Mail'].tolist()  # 項目名：E-Mailのデータをリストとして取得（※任意の項目名に置き換えてください）

# rawdata.xlsxにあってclickdata.xlsxにないメールアドレスを抽出
for email, row in zip(rawdata_emails, rawdata_df.iterrows()):
    if email not in clickdata_emails:
        result_data.append(row[1].tolist())  # その行の情報をリストとしてresult_dataに追加

# 結果を新しいExcelファイルに保存
result_df = pd.DataFrame(result_data, columns=rawdata_df.columns)
output_file = os.path.join(output_folder, 'noclickdata.xlsx') # ファイル名を指定(※_日付 を加えるなどして差別化してください)
result_df.to_excel(output_file, index=False)
