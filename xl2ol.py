import pandas as pd
import win32com.client as win32

# Excelファイルのパスとシート名を指定
excel_file = r'C:\Users\mikus\finance\data\Book2.xlsx'
sheet_name = 'Sheet1'

# Excelファイルを読み込む
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# companyごとにソートして新しいシートに書き込む
sorted_sheets = {}
for company, group in df.groupby('company'):
    sorted_sheets[company] = group.sort_values(by='company')

# Excelファイルに新しいシートを追加して各シートを書き込む
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
    for company, sheet in sorted_sheets.items():
        sheet.to_excel(writer, sheet_name=company, index=False)

# Outlookオブジェクトを作成
outlook = win32.Dispatch('Outlook.Application')

# シートごとにメールの下書きを作成
for company, sheet in sorted_sheets.items():
    recipients = sheet['email'].tolist()
    subject = 'Important Information'.format(company)
    body = 'Dear {},\n\nPlease find the attached information for todays report.'.format(company)

    mail = outlook.CreateItem(0)  # 0はメールを表す定数
    mail.Subject = subject
    mail.Body = body
    mail.To = ';'.join(recipients)

    # Excelファイルを添付
    attachment = excel_file
    mail.Attachments.Add(attachment)

    # メールの下書きを表示
    mail.Display()

# Outlookを終了
outlook.Quit()
