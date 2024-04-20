# импортируем библиотеку tkinter
from tkinter import *
# создаём класс для калькулятора
class LoanCalculator:
    # инициализируем класс
    def __init__(self):
        # стартуем tkinter, чтобы создать окно графического интерфейса
        root=Tk()
        # задаём размеры окна
        root.geometry("500x300")
        # задаём название окна калькулятора
        root.title("Кредитный калькулятор")
        # задаём цвет окна калькулятора, например пыльно-серый
        root.config(bg='#a39ea0')
        # задаём расположение, стиль шрифта и пояснительный текст для поля годовой процентной ставки
        Label(root,text="Годовая ставка, %", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=10)
        # задаём расположение, стиль шрифта и пояснительный текст для поля срока кредита
        Label(root, text="Срок, лет", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=50)
        # задаём расположение, стиль шрифта и пояснительный текст для поля суммы кредита
        Label(root, text="Сумма кредита", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=90)
        # задаём расположение, стиль шрифта и пояснительный текст для вывода ежемесячного платежа
        Label(root, text="Ежемесячный платёж:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=150)
        # задаём расположение, стиль шрифта и пояснительный текст для вывода общей суммы выплаты
        Label(root, text="Общая сумма выплаты:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=190)
        # добавляем поле для ввода годовой процентной ставки
        self.annualinterestVar=StringVar()
        Entry(root, textvariable=self.annualinterestVar,font=('Arial,15,bold')).place(x=220,y=10)
        # добавляем поле для ввода количества лет кредит
        self.numberofyearsVar=StringVar()
        Entry(root, textvariable=self.numberofyearsVar,font=('Arial,15,bold')).place(x=220,y=50)
        # добавляем поле для ввода суммы кредита
        self.loanamountVar=StringVar()
        Entry(root, textvariable=self.loanamountVar,font=('Arial,15,bold')).place(x=220,y=90)
        # добавляем строку вывода расчёта ежемесячного платежа
        self.monthlypaymentVar=StringVar()
        Label(root, textvariable=self.monthlypaymentVar,font=('Arial,15,bold'),bg='#a39ea0').place(x=220,y=150)
        # добавляем строку вывода расчёта общей суммы выплаты
        self.totalpaymentVar=StringVar()
        Label(root, textvariable=self.totalpaymentVar,font=('Arial,15,bold'),bg='#a39ea0').place(x=220,y=190)
        # добавляем кнопку, задаём её расположение, надпись и стиль шрифта
        Button(root, text="Рассчитать",font=('Arial,15,bold'),command=self.calculateloan).place(x=180,y=240)
        # запускаем окно
        root.mainloop()
    # определяем функцию расчёта общей суммы выплаты
    def calculateloan(self):
        # определяем формулу, по которой будет рассчитываться ежемесячный платёж по кредиту
        monthlypayment=self.getmonthlypayment
        (float(self.loanamountVar.get()),float(self.annualinterestVar.get()) / 1200, int(self.numberofyearsVar.get()))
        self.monthlypaymentVar.set(format(monthlypayment, '10.2f'))
        # определяем формулу, по которой будет рассчитываться общая сумма выплаты по кредиту
        totalpayment=float(self.monthlypaymentVar.get()) * 12 * int(self.numberofyearsVar.get())
        self.totalpaymentVar.set(format(totalpayment, '10.2f'))
    # определяем функцию расчёта ежемесячного платежа
    def getmonthlypayment(self,loanamount,monthlyinterestrate,numberofyears):
        # определяем формулу, по которой будет рассчитываться ежемесячный платёж
        monthlypayment=loanamount * monthlyinterestrate / (1-1 / (1 + monthlyinterestrate) ** (numberofyears * 12))
        return monthlypayment
# вызываем класс калькулятора, чтобы запустить программу
LoanCalculator()