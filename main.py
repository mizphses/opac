from psycopg2 import connect
from werkzeug.security import generate_password_hash, check_password_hash

menu = input("業務メニューを選択: [S]登録番号から書誌情報を表示, [U]利用者情報メニュー, [R]貸出・返却, [X]終了")
if menu == "S":
    bib_id = input("登録番号を入力してください")
    conn = connect("dbname=mopac user=MOPAC password=mopac")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bibs WHERE bib_id = %s", (bib_id,))
    bib = cur.fetchone()
    print(bib)
elif menu == "U":
    print("利用者情報メニュー")
    user = {}
    user["name"] = input("登録者氏名を入力")
    user["password"] = generate_password_hash(input("パスワードを入力"), method="sha512", salt_length=30)
    user["email"] = input("メールアドレスを入力")
    user["tel"] = input("電話番号を入力")
    user["address"] = input("住所を入力")
    user["birthdate"] = input("生年月日を入力")
    user["tags"] = []
    user["card_number"] = input("カード番号をスキャンまたは入力")
    print(user)
    print("以上の情報で登録しますか？")
    print("登録するにはYを入力")
    print("登録をやり直すにはNを入力")
    print("メニューに戻るにはMを入力")
    confirm = input("Y/N/M")
    if confirm == "Y":
        conn = connect("dbname=mopac user=mopac password=mopac")
        cur = conn.cursor()
        cur.execute("INSERT INTO users (userName, password_hash, email, telephone_number, address, birthdate, card_number) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
            user["name"], user["password"], user["email"], user["tel"], user["address"], user["birthdate"], user["card_number"]))
        conn.commit()
        print("登録が完了しました")
    elif confirm == "M":
        print("メニューに戻ります")
elif menu == "R":
    print("貸出・返却")
elif menu == "X":
    print("終了するにはCtrl+Cを操作")
else:
    print("不正な入力です")