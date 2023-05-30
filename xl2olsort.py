import pandas as pd
import win32com.client as win32

# Excelファイルのパス
file_path = r'C:\Users\mikus\finance\data\Book2.xlsx'

# Excelファイルの読み込み
df = pd.read_excel(file_path, sheet_name='Sheet1')

# companyごとにデータをソートしてファイル作成
for company in df['company'].unique():
    # companyごとにデータを抽出
    company_data = df[df['company'] == company]
    
    # 新しいファイル名の生成
    new_file_path = r'C:\Users\mikus\finance\output\report_{}.xlsx'.format(company)
    
    # データを新しいファイルに保存
    company_data.to_excel(new_file_path, index=False)
    
    # Outlookの準備
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    
    # メールの設定
    mail.Subject = f"Report for {company}"
    mail.Body = "Please find the attached report."
    
    # メールの宛先アドレスを設定
    recipients = company_data['email'].tolist()
    mail.To = ";".join(recipients)
    
    # ファイルを添付
    mail.Attachments.Add(new_file_path)
    
    # メールを下書きとして保存
    mail.Save()
