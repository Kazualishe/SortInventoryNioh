import pyautogui
import time
import keyboard
import mouse

def ClickKey(key: str):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    time.sleep(0.1)

def KeyClick_Down():
    ClickKey("s")

def KeyClick_Up():
    ClickKey("w")

def KeyClick_E():
    ClickKey("e")

def KeyClick_Q():
    ClickKey("q")

def KeyClick_1():
    ClickKey("1")

def KeyClick_2():
    ClickKey("2")

def TryFoundElement(elem: str):
    try:
        print("try find " + elem)
        pyautogui.locateCenterOnScreen(elem, confidence=0.9)
        print("FIND " + elem)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def ClickToElement(elem: str):
    try:
        TryClickToElement(elem)
    except pyautogui.ImageNotFoundException:

        KeyClick_Down
        KeyClick_Up
        
        ClickToElement(elem)

def TryClickToElement(elem: str):
    print("try find " + elem)
    uiElem = pyautogui.locateCenterOnScreen(elem, confidence=0.9)
    print("FIND " + elem)
    pyautogui.click(uiElem)

def TestFunction():
    favorite = pyautogui.locateOnScreen("element.png")
    pyautogui.doubleClick(favorite)

    time.sleep(0.1)

    ClickToElement("element_2.png")

    time.sleep(0.1)

    ClickToElement("deleting_from_favorites.png")

    time.sleep(0.1)

    ClickToElement("items.png")

    time.sleep(0.1)

    ClickToElement("element_2.png")

    time.sleep(0.1)

    ClickToElement("set_button.png")

def SortOrangeOptions():
    ClickToElement("element.png")
    # переключиться на панель со всей эквипой
    KeyClick_1()

    # зайти в фильтры
    KeyClick_E()
    KeyClick_Down()
    KeyClick_E()

    # выбрать передаваемые свойства
    for i in range(5):
        KeyClick_Up()
    KeyClick_E()

    # выбрать перманентно передаваемые
    KeyClick_Down()
    KeyClick_Down()
    KeyClick_E()

    # вернуть фокус в изначальную позицию и отфильтровать
    for i in range(6):
        KeyClick_Down()
    KeyClick_E()

    print("фильтр задействован")

    time.sleep(0.5)

    # todo
    while not TryFoundElement('./Res/FiltersOptions/NotFound.png'):
        # если найден отфильтрованный итем, то лочим и перекладываем на склад
        #  заблокировать
        KeyClick_E()
        KeyClick_Down()
        KeyClick_Down()
        KeyClick_E()
        #  скинуть на склад
        KeyClick_E()
        KeyClick_Up()
        KeyClick_E()

#TestFunction()
SortOrangeOptions()