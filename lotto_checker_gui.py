import tkinter as tk
import requests

def get_lotto_numbers(draw_no):
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    response = requests.get(url)
    data = response.json()

    lotto_numbers = [data[f"drwtNo{i}"] for i in range(1, 7)]
    bonus_number = data["bnusNo"]

    return lotto_numbers, bonus_number

def show_lotto_numbers():
    draw_no = entry.get()  # 입력된 회차 번호 가져오기
    if draw_no.isdigit():
        lotto_numbers, bonus_number = get_lotto_numbers(draw_no)
        result_text.set(f"로또 {draw_no}회차 당첨 번호: {', '.join(map(str, lotto_numbers))}, 보너스 번호: {bonus_number}")
    else:
        result_text.set("올바른 회차 번호를 입력하세요.")

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("로또 번호 조회기")

# 회차 번호 입력란과 버튼 추가
tk.Label(window, text="조회할 회차 번호를 입력하세요:").pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="조회", command=show_lotto_numbers)
button.pack()

# 결과 출력 레이블
result_text = tk.StringVar()
tk.Label(window, textvariable=result_text).pack()

# Tkinter 이벤트 루프 실행
window.mainloop()
