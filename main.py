#11-misol
def tekshirish(matn):
    if matn[0].isupper() and matn[-1] == ".":
        return "To'g'ri gap"
    else:
        return "Xato farmat"

res = tekshirish("Nozila.")
print(res)

#12-misol
def email_qabul(email):
    if "@" and "." in email:
        return "Email to'g'ri"
    else:
        return "Email not'g'ri"

res = email_qabul("@jksjs.")
print(res)

#13-misol
def qabul(ism):
    if len(ism) < 3:
        return "Juda qisqa"
    elif len(ism) >= 3 and len(ism) <= 10:
        return "Norm"
    else:
        return "Juda uzun"

res = qabul("NozilaSevinchDilnura")
print(res)

#14-misol
def qabul(son):
    if son > 100 and son % 2 == 0:
        return "Katta juft"
    else:
        return "Shartga mos emas"

res = qabul(998)
print(res)

#15-misol
def qabul(matn):
    for belgi in matn:
        if not (belgi.isalpha() or belgi == " "):
            return "Ortiqcha belgilar bor"
    return "Toza matn"


res = qabul("shhsja q")
print(res)

#16-misol
def qabul(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return "Ikkalasi juft"
    elif a % 2 != 0 and b % 2 != 0:
        return "Ikkalasi toq"
    else:
        return "Aralash"


res = qabul(7, 8)
print(res)

#17-misol
def qabul(raqam):
    if len(raqam) == 9:
        return "To'g'ri raqam"
    else:
        return "Noto'g'ri raqam"


res = qabul("989876678")
print(res)

#18-misol
def qabul(a):
    if a == a[::-1] and len(a) >= 5:
        return "Katta palindrom"
    else:
        return "Oddiy yoki palindrom emas"


res = qabul("aziza")
print(res)

#19-misol
def qabul(son):
    if son > 0 and son < 50:
        return "Kichik musbat"
    elif son > 50:
        return "Katta musbat"
    else:
        return "Manfiy nol"


res = qabul(45)
print(res)

#20-misol
def qabul(nom, parol):
    if len(nom) == 6 and len(parol) == 6:
        return "Qabul qilindi"
    else:
        return "Malumot juda qisqa"


res = qabul("Nozila", "Login1")
print(res)
