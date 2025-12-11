# библитеки:
import random
import time
import pandas as pd
from colorama import *

from classes import Weapon

init()

# функции:
def chance():  # процент______________________________________________________________________________________________________
    ch1 = random.random()
    return ch1


def hilka():
    hil = random.randint(15, 30)
    return hil


def dopuron():
    dop = random.randint(10, 50)
    return dop


# переменые и масивы:
opt = 1
monet = 0
koltry = 0  # кол. пройденых раз леса
hilochka = 0  # сколько раз хилился
hp_med = 200  # хп медведя
status = "Новичёк"
over = False
naem_swap = True
bear = False
proig = False
skilet = False
answer12 = False  # для очивки интуиция
sogl = ["да", "конечно", "безусловно", "с удовольствием", "разумеется", "несомненно", "хорошо", "да, конечно",
        "договорились", "согласен", "пожалуй", "да, пожалуйста", "с радостью", "отлично", "идет", "без проблем",
        "не возражаю", "подтверждаю", "естественно", "можно"]
otr = ["нет", "к сожалению, нет", "не могу", "не сейчас", "отказываюсь", "это невозможно", "я пас", "не согласен",
       "ни за что", "ни в коем случае", "к сожалению, не получится", "вынужден отказаться", "не готов", "не хочу",
       "не буду", "не стоит", "не надо", "пожалуй, нет", "лучше не надо", "это не для меня"]
och = []  #
wolfe = [20, 15, 12]  # Волки  [ХП Урон Количиство]
hog = [40, 20]  #

print("_" * 150)
name = input(Fore.BLUE + "Введите своё имя: ")  # имя
print(Fore.BLUE + f"Здравствуй {name} ваш статус: {status}! Теперь выбери своё оружие: \n 1 - катана \n 2 - двуручный меч \n 3 - коса \n 4 - кинжал  \n 5 - копьё")  # обатиться по имени расказать о видах оружия и дать выбор
print("_" * 150)

# выбор оружия:

def weapon_choose():
    while True:
        weapon = input(Fore.YELLOW + "Введи название оружия: ")  # оружие
        # выбор оружия катана __________________________________________________________________________________________________________________________________________________________________
        if weapon == "катана":
            return Weapon(name = "Катана",
                            chup = 0.66,
                            dop_hp = 10,
                            uron = 20,
                            shans = 0.7,
                            kvfo = 2,
                            mag = random.randint(5, 15),
                            har = f"Катана - отличный выбор! Её урон = {20}, шанс попасть по врагу средний как и урон, даёт дополнительно хп {10} к основному. Катана - это баланс шанса попасть и урона!",
                            magiya = f"Катана загорелась черным огнём глаза потемнели и вы приобразились в тёмныое одеяние. В ту же секунду острё клинка пронзило его. Взмах копьём, но вы растворились во тьме и оказались по зади него",
                            mag_uron = 120
                            )
        # выбор оружия двуручный меч__________________________________________________________________________________________________________________________________________________________________
        elif weapon == "двуручный меч":
            return Weapon(name = "двуручный меч",
                            chup = 0.26,  # шанс увернуться
                            dop_hp = 110,
                            uron = 100,
                            shans = 0.25,
                            kvfo = 4,  # количесвто поражения врагов за раз
                            mag = 0,  # вотановление хп после удара
                            har = f"Двуручный меч - отличный выбор! Его урон = {100}, шанс попасть по врагу крайне низкий, а урон крайне Высокий, даёт дополнительно хп {110}, может ударить 4 врага одновремено! к основному. Двуручный меч - это баланс шанса попасть и урона!",
                            magiya = f"Вы загорелись черным пламенем, подняли свой огромный меч и резко опустили в низ дрож земли повалила скелета на змелю",
                            mag_uron = 300
                            )
            break
        # выбор оружия коса__________________________________________________________________________________________________________________________________________________________________
        elif weapon == "коса":
            return Weapon(name = "коса",
                            chup = 0.16,
                            dop_hp = 80,
                            uron = 60,
                            shans = 0.4,
                            kvfo = 3,
                            mag = random.randint(5, 40),
                            har = f"Коса - отличный выбор! Её урон = {60}, шанс попасть по врагу низкий, но урон высокий, даёт дополнительно хп {80} к основномуможет ударить 3 врага одновремено! Коса - это оружие с большим уроном но средним шансом попасть!",
                            magiya = f"Вы усмехнулись над системой затраты опыта и скелетом. Ничтожные костяшки. Взмах косы. Вы разрубили скелета пополам который правил этим лесом более 6000 лет одним взмахои",
                            mag_uron = 500
                          )
        # выбор оружия кинжал__________________________________________________________________________________________________________________________________________________________________
        elif weapon == "кинжал":
            return Weapon(name = "кинжал",
                            chup = 0.76,
                            dop_hp = 0,
                            uron = 10,
                            shans = 0.98,
                            kvfo = 1,
                            mag = random.randint(5, 10),
                            har = f"Кинжал - отличный выбор! Его урон = {10}, шанс попасть по врагу почти гарантирован но урон низкий, даёт дополнительно хп {0} к основному. Кинжал - это маленький урон но мгновеный удар!",
                            magiya = f"Кинжал загорелся и потускнел сва будто бы прозрачным во второй руке вы почувствовывали клинок, теперь их к вас два, ваш взгляд пронзил скелета и вы на несли 16 ударов нанеся 320 урона",
                            mag_uron = 320
                          )
        elif weapon == "копьё" or weapon == "копье":
            return Weapon(name = "Копьё",
                            chup = 0.7,  # шанс увернуться
                            dop_hp = 30,
                            uron = 80,
                            shans = 0.7,
                            kvfo = 1,  # количесвто поражения врагов за раз
                            mag = 30,  # вотановление хп после удара
                            har = f"Копьё - отличный выбор! Его урон = {80}, шанс попасть по врагу крайне средний, а урон крайне Высокий, даёт дополнительно хп {30}, может ударить 1 врага одновремено! к основному. Копьё - это огромный урон в одну цель",
                            magiya = f"Вы утихли и не произносоили не слова, как только скелет замохнулся вы подняли взгляд и мгновеным выпадом разорвали его голову своим копьём что бы не повредить его броню",
                            mag_uron = 500
                            )
            break
        # выбор оружия ошибка__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
        else:
            print(Fore.RED + "Пожалуйста введите существующий вид оружия: \n коса \n катана \n двуручный меч \n кинжал \n копьё")
weapon = weapon_choose()
print(weapon.har, "\n")
print("_" * 150)
opt = 1
hp = 100 + weapon.dop_hp
hps = hp
print(Fore.GREEN + f"оружие вашего персонажа: {weapon.name}, Характеристики: \n ХП = {hp} \n урон = {weapon.uron} \n шанс попадания = {weapon.shans}\n ваш опыт = {opt} ну что начнём приключение!")  # дать характреисику персанажа
time.sleep(0.5)
start = input(Fore.BLUE + 'Нажмите Enter!\n')

# сюжет _____________________________________________________________________________________________________________________________________________________________________________________
print(Fore.BLUE + "Сегодня на улице вы встретили человека, который рассказал вам про деревню. \n -'На днях в деревне пропали все жители и были разрушены дома, можете помочь разобраться с этой бедой?' ")
time.sleep(5)
print("_" * 150)
while True:
    answer1 = input(Fore.BLUE + "Вы готовы помоч ему?\n")
    if answer1 in sogl:
        print(Fore.BLUE + "-'Отлично значит сегодня и пойдёте, спасибо вам!'\n")
        time.sleep(0.5)
        break
    elif answer1 in otr:
        print(Fore.BLUE + "\n -'Но ведь тогда пострадают и другие деревни!' \n Что ж ничего не поделаешь, подумали вы и скрипя зубы сказали, что согласны\n")
        time.sleep(0.5)
        print(Fore.BLUE + "-'Отлично значит сегодня и пойдёте, спасибо вам!'\n")
        time.sleep(0.5)
        answer12 = True
        break
    else:
        print(Fore.RED + "он вас не понял, пожауйста введите ответ понятнее")
        time.sleep(0.5)
time.sleep(0.5)
print(Fore.BLUE + "Вы вышли из города и пошли в сторону деревни, в которой произошло несчастье. \n незнакомец окликнул вас и подозвал к себе, протянул банку с какой то жидкосью. \n -'Вот держи вдруг понадобится'\n С сегодняшнего дня вы искатель приключений!\n \n")  # закрутить сюжет
time.sleep(0.5)
print("_" * 150)
# лес:
while (hp > 0 and koltry <= 7) or not skilet :
    opt += 1000
    print("_" * 150)
    option = input(Fore.YELLOW + "Введите действие. идти, хилка: \n")  # вариант развития
    time.sleep(2)
    if option == "идти" or option == "вперёд" or option == "идти дальше":
        if koltry >= 3 and not skilet:
            wst = 0.5
        else:
            wst = chance()
        # Встреча Волков!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if wst < 0.3:
            print("_" * 150)
            print(Fore.CYAN + "вы встретили волков")
            time.sleep(0.5)
            hp_mob = wolfe[0]
            uron_mob = wolfe[1]
            contr_mob = wolfe[2]
            while contr_mob > 0 and hp > 0:
                print("__" * 20)
                ku = chance()  # шанс ульты если в руках катана или кинжал
                proc = chance()
                opt = opt + proc * opt
                atk = input(Fore.CYAN + "для удара нажмите Enter! ")
                ch = chance()
                chu = chance()
                if chu <= weapon.chup:
                    if ku <= 0.2 and (weapon.name == "кинжал" or weapon.name == "катана"):  # УЛЬТА
                        print("_" * 70)
                        print(Fore.MAGENTA + "Кажится вы смогли увернуться и есть шанс использовать магию!")
                        m = input(Fore.MAGENTA + "Использовать магию?")
                        if m in sogl:
                            print(Fore.MAGENTA + "тогда поехали!")
                            time.sleep(2)
                            print(Fore.MAGENTA + "В туже секунду вы сложили оружие в ножны. резко гробовая тишь тьма и резкий глубокий выдох")
                            time.sleep(5)
                            kol = random.randint(2, 6)
                            for i in range(kol):
                                print(Fore.MAGENTA + "Шиньк!")
                                time.sleep(0.25)
                            time.sleep(2.5)
                            print(Fore.MAGENTA + "тишина...")
                            time.sleep(2)
                            if kol <= contr_mob:
                                contr_mob -= kol
                                print(Fore.MAGENTA + f"вам удалось разрубить {kol} волков за пару секунд.")
                            elif kol > contr_mob:
                                contr_mob = 0
                                print(Fore.MAGENTA + f"вы добили последних {kol} волков идти дальше")
                            print(Fore.MAGENTA + "по тихоньку ваше оружие перестало полыхать черным огнём, вот эта сила подумали вы и снова взглянув на руку увидели черту, что же это...")
                        elif m in otr:
                            print(Fore.MAGENTA + "Вы взмохнули мечом и магия пропала, реши не рисковать и продолжить бой по старинке. но на руке появилась черта, от чего же...")
                        else:
                            print(Fore.MAGENTA + "Вы пытаись что то сделать но мечь погас и на вас снова бросились волки")
                            hp -= uron_mob
                        print("_" * 150)
                    elif weapon.shans >= ch:
                        hp_mob -= weapon.uron
                        if hp + weapon.mag < hps:
                            hp += weapon.mag
                        else:
                            hp = hps
                        if hp_mob <= 0:
                            contr_mob -= weapon.kvfo
                            hp_mob = wolfe[0]
                        # hp -= uron_mob
                        print(Fore.CYAN + f"удар, и вы восстановили немного хп за счёт магии оружия {hp}!, так как вы смогли увернуться. осталось волков {contr_mob}")
                        time.sleep(0.5)
                        time.sleep(1)
                    elif weapon.shans < ch:
                        # hp -= uron_mob
                        print(Fore.CYAN + f'Мимо! но и вы увернулись! Ваше хп {hp}')
                        time.sleep(0.5)
                    elif hp <= 0 or contr_mob <= 0:
                        break
                if chu > weapon.chup:
                    if weapon.shans >= ch:
                        hp_mob -= weapon.uron
                        if hp + weapon.mag < hps:
                            hp += weapon.mag
                        else:
                            hp = hps
                        if hp_mob <= 0:
                            contr_mob -= weapon.kvfo
                            hp_mob = wolfe[0]
                        hp -= uron_mob
                        print(Fore.CYAN + f"удар ваше хп {hp}. осталось волков {contr_mob}")
                        time.sleep(0.5)
                    elif weapon.shans < ch:
                        hp -= uron_mob
                        print(Fore.RED + f'Мимо! Ваше хп {hp}')
                        time.sleep(0.5)
                    elif hp <= 0 or contr_mob <= 0:
                        break
                if contr_mob <= 0:
                    print(Fore.GREEN + "Отлично вы победили волков и можете идти дальше!\n \n")
                    time.sleep(0.5)
                    koltry += 1
                    break
                if hp <= 0:
                    print(Fore.RED + Style.BRIGHT + "Вы проиграли\n")
                    time.sleep(0.5)
                    over = True
                    break
            print("_" * 150)
        elif 0.3 < wst < 0.45:
            print(Fore.CYAN + "вы встретили кабана")
            time.sleep(0.5)
            hp_mob = hog[0]
            uron_mob = hog[1]
            while True:
                print("__" * 20)
                proc = chance()
                opt = opt + proc * opt
                atk = input("Нажмите Enter для удара! ")
                ch = chance()
                chu = chance()
                if chu < weapon.chup:
                    if weapon.shans >= ch:
                        hp_mob -= weapon.uron
                        if hp + weapon.mag < hps:
                            hp += weapon.mag
                        else:
                            hp = hps
                        print(
                            f"удар, и вы восстановили немного хп за счёт магии оружия {hp}!, так как вы смогли увернуться!")
                        time.sleep(0.5)
                    elif weapon.shans < ch:
                        print(f'Мимо! но и вы увернулись! Ваше хп {hp}')
                        time.sleep(0.5)
                if chu >= weapon.chup:
                    if weapon.shans >= ch:
                        hp_mob -= weapon.uron
                        if hp + weapon.mag < hps:
                            hp += weapon.mag
                        else:
                            hp = hps
                        hp -= uron_mob
                        print(f"удар ваше хп {hp}")
                        time.sleep(0.5)
                    elif weapon.shans < ch:
                        hp -= uron_mob
                        print(f'Мимо! Ваше хп {hp}')
                        time.sleep(0.5)
                if hp_mob <= 0:
                    print(
                        f"вы смогли победить кабана, вы пожарили и съели его из-за чего восстановили всё хп {hps} \n \n")
                    time.sleep(0.5)
                    hp = hps
                    koltry += 1
                    break
                if hp <= 0:
                    print("Вы проиграли")
                    time.sleep(0.5)
                    over = True
                    break
            print("_" * 150)

        elif wst > 0.45 and wst < 0.8 and skilet == False:
            print(Fore.WHITE + "на вашем пути стоит скелет на коне, он облочён в доспехи, в руках он держит копьё, его вид внушает ужас до этого вам не приходилось испытывать такой страх")
            print("Вдруг он заговорил. Тихо, хрипло и угрожающи \n -'Путник, это мои владения... Я уничтожу тебя и не важно на что ты способен.'")
            skilet = True
            optd = opt
            hp_skelet = 300
            uron_skelet = 60
            print("Он взмахнул копьём и почти было вас рассёк, вы успели отскочить!")
            print(f"-'Бегать вечно ты не сможешь, твое оружие - {weapon.name}, это {weapon.name} тьмы, видно ты не прост путник.'")
            print(Fore.WHITE + Style.BRIGHT + f"ВНИМАНИЕ \n", Style.DIM + "есть шанс что скелет убьёт вас одним ударом, избежать битвы с ним невозможно, его сила велика. вот команды ввода: магия, удар/ударить, хилиться/хилка \n Будьте осторожны и удачи" + Style.RESET_ALL)
            while hp_skelet > 0 and hp > 0:
                ch = chance()
                if ch >= 0.99:
                    print(Fore.RED + "Это конец! *скелет взмахнул копьём и убил вас!* \n всё же вы недооценили врага..." + Style.RESET_ALL)
                    over = True
                    break
                zv = input("Выберите своё действие: Ударить, хилиться, использовать магию (магия): ")
                if zv == "магия":
                    iii = input("Вы уверенны вы отдадите 20% своего опыта взамено мощного удара ")
                    if iii in sogl:
                        print(f"Ваша рука и оружие загорелись... \n {weapon.magiya}")
                        hp_skelet -= weapon.mag_uron
                        opt -= (opt*(2/10))
                elif zv == "удар" or zv == "ударить":
                    print("удар по скелету прошёл лишь на половину. Логично что у него будут какие то резисты")
                    hp_skelet -= (weapon.uron//2)
                    hp -= uron_skelet
                elif option == "хилка" or option ==  "востановить здоровье" and hp > 0:
                    opt = opt - opt/1000
                    hilochka += 1
                    hil = hilka()
                    if hp <= hps-hil:
                        hp += hil
                        print(Fore.GREEN + f"Вы отхилили {hil}хп теперь ваше здоровье равно: {hp}хп \n")
                        time.sleep(0.5)
                    else:
                        hp = hps
                        print(Fore.GREEN + f"ваше здоровье = {hp}")
                        time.sleep(0.5)
            if hp > 0:
                print("-'Неужели я настолько жалок и смог проиграть такому ничтожному человечишки?......'")
                print(Fore.GREEN + "Вы одолели короля леса и тьмы и можете идти дальше, вы хотите надеть его броню и забрать его оружие?")
                z123 = input()
                if z123 in sogl:
                    status = "Повелитель тьмы"
                    weapon.name = "Посох повелителя тьмя"
                    weapon.chup = 0.99
                    weapon.dop_hp = 100
                    weapon.uron = 120
                    weapon.shans = 0.5
                    weapon.kvfo = 12
                    weapon.mag = random.randint(5, 15)
                    och.append("Победа над повелителем тьмы")
                    och.append("Забрать снаряжение")
                    koltry -= 3
                elif z123 in otr:
                    print("страный вы челик раз отказлись от халявы(")
                print(f"ваш опыт до сражения: {optd}, после сражения: {opt}, и вы потратели опыта: {optd - opt}")

        elif wst > 0.8 and wst < 0.9 and opt >= 1001:
            print(Fore.YELLOW + f"Вы встретили Даниила Савельева, торгавец от бога будьте осторожны, ваш опыт: {opt}")
            otv = input("Торговаться? ")
            if otv in sogl:
                print("отлично")
                print(Fore.CYAN + "вот что я могу предложить:")
                opt1 = int(opt)
                j = opt1 // 10
                coast = random.randint(j, opt1)
                hpc = random.randint(j, opt1)
                shops = {'Товар Даниила |': ['| 1 |', '| 2 |', '| 3 |', '| 4 |'],'товар или услуга |': ["Увеличить Атака |", "Увеличить хп |" , "сменить оружие |", "сменить имя |"],'цена |': [str(coast) + " |" , str(hpc) + " |", str(opt1) + " |", str(opt1//2) + " |"], "описание |": ["увеличите атаку на 5 |", "увеличите хп на 10 |", "Вы замените свое оружие |", "Вы замените свое Имя |"]}
                print(pd.DataFrame(shops))
                while True:
                    otv2 = input("(для выхода нажмите X или Z) напшите цифру услуги: ")
                    if otv2 == "1":
                        print("увеличение атаки")
                        if (opt - coast) > 0:
                            weapon.uron += 5
                            opt -= coast
                        else:
                            print("Кажеться Даниил заьрал уже всё(")
                    elif otv2 == "2":
                        if (opt - hpc) > 0:
                            print("увеличение хп")
                            hps += 10
                            hp = hps
                            opt -= hpc
                            och.append("билд танка?")
                        else:
                            print("Кажеться Даниил заьрал уже всё(")
                    elif otv2 == "3":
                        if opt - coast > 0:
                            print("смена оружия")
                            weapon_choose()
                            weapon = weapon_choose()
                            opt -= opt1
                            print(f"вы сменили своё оружие на {weapon.name}")
                            och.append("Променять своё оружие")
                            break
                        else:
                            print("деняк нет(")
                    elif otv2 == "4" and naem_swap:
                        print("Смена имени")
                        name = input('введите своё новое имя: ')
                        opt -= opt1//2
                        och.append(f"{name} - новое имя...")
                        naem_swap = False
                    elif otv2 == "X" or otv2 == "x" or otv2 == "Z" or otv2 == "z":
                        print("Вы попращались с торговцем и ушли")
                        och.append("Торговля с Даниилом")
                        break

            elif otv in otr:
                print("тогда вы можете идти дальше не смею вас задерживать")
        if over:
            break
        elif wst > 0.45 and wst < 0.8 and skilet == True:
            print(Fore.CYAN + "вы встретили Приспешника скелета, они увидели вас и набросились")
            time.sleep(0.5)
            hp_mob = 100
            uron_mob = 16
            contr_mob = 12
            while True:
                print("__" * 20)
                proc = chance()
                opt = opt + proc * opt
                atk = input("Нажмите Enter для удара! ")
                ch = chance()
                chu = chance()
                if chu < weapon.chup:
                    if weapon.shans >= ch:
                        hp_mob -= weapon.uron
                        if hp + weapon.mag < hps:
                            hp += weapon.mag
                        else:
                            hp = hps
                        print(f"удар, и вы восстановили немного хп за счёт магии оружия {hp}!, так как вы смогли увернуться!")
                        time.sleep(0.5)
                        contr_mob -= weapon.kvfo
                    elif weapon.shans < ch:
                        print(f'Мимо! но и вы увернулись! Ваше хп {hp}')
                        time.sleep(0.5)
                if chu >= weapon.chup:
                    if weapon.shans >= ch:
                        hp_mob -= weapon.uron
                        if hp + weapon.mag < hps:
                            hp += weapon.mag
                        else:
                            hp = hps
                        hp -= uron_mob
                        contr_mob -= weapon.kvfo
                        print(f"удар ваше хп {hp}")
                        time.sleep(0.5)
                    elif weapon.shans < ch:
                        hp -= uron_mob
                        print(f'Мимо! Ваше хп {hp}')
                        time.sleep(0.5)
                if hp_mob <= 0 and contr_mob <= 0:
                    print(
                        f"вы смогли победить скилетиков")
                    time.sleep(0.5)
                    koltry += 1
                    break
                if hp <= 0:
                    print("Вы проиграли")
                    time.sleep(0.5)
                    over = True
                    break
            print("_" * 150)
        else:
            print(Fore.GREEN + "вы смогли спокойно пройти \n \n")
            time.sleep(0.5)
            koltry += 1
            proc = chance()
            opt = opt + proc * opt


    if option == "хилка" or option ==  "востановить здоровье" and hp > 0:
        opt = opt - opt/1000
        hilochka += 1
        hil = hilka()
        if hp <= hps-hil:
            hp += hil
            print(Fore.GREEN + f"Вы отхилили {hil}хп теперь ваше здоровье равно: {hp}хп \n")
            time.sleep(0.5)
        else:
            hp = hps
            print(Fore.GREEN + f"ваше здоровье = {hp}")
            time.sleep(0.5)

koltry = 0
print("_" * 70)
# концовка
print("_" * 150)
if hp > 0:
    if opt >= 100000:
        while opt >= 1000000:
            opt //= 10
        och.append("Куча опыта!")
    print(Fore.GREEN + Style.BRIGHT + f"ваш опыт равен {int(opt)}! \n")
    time.sleep(0.5)

    och.append("Лес пройден")
    time.sleep(0.25)
    print("=" * 50)
    time.sleep(0.25)
    print(f"Имя: {name}")
    time.sleep(0.25)
    print(f"Оружие: {weapon.name}")
    time.sleep(0.25)
    print(f"Здоровье: {hp}/{hps}")
    time.sleep(0.25)
    print(f"Опыт: {opt}")
    time.sleep(0.25)
    print(f"Монеты: {monet}")
    time.sleep(0.25)
    print(f"Достижения: {', '.join(och)}")
    time.sleep(0.25)
    print("=" * 50)
    conv = random.randint(1, 25)
    print("_" * 150)
    print(Fore.GREEN + f"Вы встретили торговца и он готов купить весь ваш опыт по цене одна монета за {conv} опыта \n" + Style.RESET_ALL)
    time.sleep(0.5)
    answer = input(Fore.CYAN + 'вы согласны? \n')
    if answer in sogl:
        monet = opt // conv
        opt = int(opt % conv)
        print(Fore.CYAN + f"Вы получаете монетки в коичесвте: {monet} \n и остаток опыта: {opt} \n")
        time.sleep(0.5)
    elif answer in otr:
        print(Fore.CYAN + "вы оставили себе свой опыт и ушли \n")
        time.sleep(0.5)
    print("_" * 150)

    print(Fore.CYAN + "вы нашли деревню, о которой говорил незнакомец. \n Похоже будто она заброшена уже давно, но вам не просто так сказали про то что жители исчезли,\n значит в этом и вопрос что с ними произошло? \n хм...")
    time.sleep(0.5)
    print(Fore.CYAN + "возможно дело в том что о... \n !!! \n Неуспели вы договорить как на вас выпрыгнул медведь \n Но откуда я ведь давно вышел из леса! \n")
    time.sleep(0.5)
    print(Fore.CYAN + "Пора... \n вы решились использовать туз в рукаве. \п ВСПЫШКА! \n вдруг что то тихо прозвучало \n на вас нет ни царапины. вы решились использовать то исцеляющие зелье которое вам дал незнакомец")
    time.sleep(0.5)
    och.append(Fore.GREEN + "Использовать зелье")
    hp = hps
    z = input(Fore.CYAN + "СКОРЕЕ ОН ВОТ ВОТ УДАРИТ!")
    print("_" * 150)
    ch = chance()
    dop = dopuron()
    if ch >= weapon.chup:
        print(Fore.CYAN + "Отлично вы успели увернуться!")
        time.sleep(0.5)
        hp_med -= (weapon.uron * 2)
        print(Fore.CYAN + f"ударю незаметно пока он не успел очухаться! УДАР {weapon.uron * 2}. \n урон больше чем обычно из-за неожиданной атаки!")
        time.sleep(0.5)
    elif ch < weapon.chup:
        print(Fore.CYAN + "что ж раз не успею увернуться прему и ударю в ответ \n УДАР!!!")
        time.sleep(0.5)
        hp -= 40
        hp_med -= (weapon.uron + dop)
        print(Fore.CYAN + f"Кажится вы попали прямо по горлу урон был больше обычного {weapon.uron + dop}. \n Но это не конец!")
        time.sleep(0.5)
    print("_" * 150)
    print(Fore.CYAN + "Продолжим!")
    time.sleep(0.5)
    z2 = input(Fore.CYAN + "Ударить ещё раз! (Enter)")
    time.sleep(0.5)
    ch = chance()
    dop = dopuron()
    print("_" * 150)
    if ch >= weapon.chup:
        print(Fore.GREEN + "Отлично вы снова успели увернуться!")
        time.sleep(0.5)
        hp_med -= (weapon.uron * 2)
        print(Fore.CYAN + f"УДАР! УДАР! УДАР! УДАР! {weapon.uron * 4}. \n Кажится вы провели серию атак, а медведь ничего не смог ответить!")
        time.sleep(0.5)
        bear = True
    elif ch < weapon.chup:
        print(Fore.CYAN + "Пора снова бить, \n по вам тоже попали")
        time.sleep(0.5)
        hp -= 40
        hp_med -= (weapon.uron + dop)
        print(Fore.CYAN + f"Кажится что он уже на исдыхании {weapon.uron + dop}. \n Но это не конец!")
        time.sleep(0.5)
    hp = hps
    print("_" * 50, "\n")
    time.sleep(0.5)
    if bear:
        print(Fore.CYAN + "Ему уже конец, неужели это из-за его деревня пуста?... \n")
        time.sleep(0.5)
    else:
        print(Fore.CYAN + "Последний удар! \n Теперь он точно мертв, возможно деревня это его, рук или лап не важно, дело")
        time.sleep(0.5)
    och.append(Fore.GREEN + "Медведь побеждён")
    print(Fore.CYAN + "тут раздался взрыв и вышел тот самый ненакомец навел на вас лук и холоднокровно сказал. \n У вас два пути ваши оружия не достанут до меня отдайти мне ваши монеты или ...")
    time.sleep(0.5)
    ch = chance()
    print("_" * 150)
    if weapon.name == "":
        print("он увидел у вас в руках посох и на детую на вас броню, выпустил стрелу а она откачила, вы приказали ему бежать и он сбежал...")
        och.append("внушающий ужас")
    elif monet >= 1000:
        z3 = input("заплатить или драться?")
        if z3 == "заплатить" or z3 == "заплатить":
            print("Заплачу и уйду живым")
            time.sleep(0.5)
            monet -= 1000
            print("-'хоршо, проваливай мне хватит 1000 монет'")
            time.sleep(0.5)
            och.append("Корупционер")
            print(
                "Вы заплатитли незнакомцу - обманщику и смоли спокойно уйти. отныне будьте внимательнее прежде чем на что то соглашаться, удачи и до новых встречь ;)")
            time.sleep(0.5)
        elif z3 == "драться":
            print("Выстрел!")
            time.sleep(0.5)
            if ch < 0.5:
                print("Вы кинули в него своё оружие и мгновенно убили его")
                time.sleep(0.5)
                och.append("Убить из далека своим оружием")
            elif ch >= 0.5:
                print("Вы хотели кинуть оружие но не успели и получили стрелу в сердце")
                time.sleep(0.5)
                proig = True
        else:
            print("Он не стал разбираться что вы там сказали и просто выстрелил...")
            time.sleep(0.5)
            hp = 0
    print("_" * 150)
    if monet < 1000:
        print("Вы посмотрели на свой кашелёк в туже секунду, ЧЁРТ нехватает...")
        time.sleep(0.5)
        fg = input("сбежать или драться?")
        if fg == "сбежать" or fg == "убежать":
            och.append("Быстрые ноги люлей не получат!")
            time.sleep(0.5)
            print("вы ветляя побежали и вам удаось сбежать!")
            time.sleep(0.5)
        if fg == "драться":
            if ch < 0.5:
                print("выстрел!")
                time.sleep(0.5)
                print(
                    "Вы бросили оружие и попали \n раненый, но вы выжили. отныне будьте внимательнее прежде чем на что то соглашаться, удачи и до новых встречь ;)")
                time.sleep(0.5)
            elif ch >= 0.5:
                print("выстрел!")
                time.sleep(0.5)
                print("Вы бросили оружие и не попали \n к сожалению вы не смоги выжить")
                time.sleep(0.5)
                proig = True
    print("_" * 150)
    if answer12:
        print(Fore.CYAN + "Х а я знал, стоило отказаться от этого похода...")
        time.sleep(0.5)
        och.append("Интуиция")
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)
    print(f"Имя: {name}")
    print(f"Оружие: {weapon.name}")
    print(f"Здоровье: {hp}/{hps}")
    print(f"Опыт: {opt}")
    print(f"Монеты: {monet}")
    print(f"Достижения: {', '.join(och)}")
    print("=" * 50)

elif hp <= 0 or proig:
    print("_" * 150)
    print(Fore.RED + Style.BRIGHT + "Вы проиграли... отныне будьте внимательнее прежде чем на что то соглашаться, удачи и до новых встречь ;)")
    time.sleep(0.25)
    print("=" * 50)
    time.sleep(0.25)
    print(f"Имя: {name}")
    time.sleep(0.25)
    print(f"Оружие: {weapon}")
    time.sleep(0.25)
    print(f"Здоровье: {hp}/{hps}")
    time.sleep(0.25)
    print(f"Опыт: {opt}")
    time.sleep(0.25)
    print(f"Монеты: {monet}")
    time.sleep(0.25)
    print(Back.YELLOW + Fore.BLACK + f"Достижения: {', '.join(och)}")
    time.sleep(0.25)
    print("=" * 50)
    print("_" * 150)

# если выжил продолжение истории расскза про то откуда у тебя эти полосы про одержимых волков и вашу силу