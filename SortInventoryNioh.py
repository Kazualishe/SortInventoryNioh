import pyautogui
import time
import keyboard
import mouse
from enum import Enum

class Pages(Enum):
    Favorite = 0
    Active = 1
    New = 2
    AllWeapon = 3
    Katana = 4
    DualKatana = 5
    Spear = 6
    Axe = 7
    Kusa = 8
    Odati = 9
    Tonfa = 10
    DualAxes = 11
    Scythe = 12
    Staff = 13
    Fists = 14
    Bow = 15
    Rifle = 16
    Cannon = 17
    AllArmor = 18
    Helmet = 19
    Chest = 20
    Pants = 21
    Boots = 22
    Amulet = 23
    Core = 24
    Quest = 25
    Panel = 26
    Ammo = 27
    Forge = 28
    Teaware = 29
    Scroll = 30
    AllItems = 31

class FiltrOptions(Enum):
    Use = 0
    ScrollOption = 1
    ValSpecialOption2 = 2
    SpecialOption2 = 3
    ValSpecialOption1 = 4
    InheritSpecialOption1 = 5
    SpecialOption1 = 6
    Markered = 7
    Familiarity = 8
    BlockStatus = 9
    PlusValue = 10
    Rarity = 11
    Lvl = 12
    Name = 13

class InputKey:

    _curFiltrInd = 0
    _countFiltrOption = 14

    _curPageInd = 0
    _countPages = 32

    _inputDelay = 0.1

    def _clickKey(self, key: str):
        time.sleep(self._inputDelay)
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        time.sleep(self._inputDelay)

    def Up(self):
        self._clickKey("w")

    def Down(self):
        self._clickKey("s")

    def Left(self):
        self._clickKey("a")

    def Right(self):
        self._clickKey("d")

    def E(self):
        self._clickKey("e")

    def Q(self):
        self._clickKey("q")

    def Digit_1(self):
        self._clickKey("1")

    def Digit_2(self):
        self._clickKey("2")

    def SelectPage(self, ind: Pages):
        nextInd = 0
        curInd = 0

        if abs(ind.value - self._curPageInd) > self._countPages / 2:
            if ind.value > self._curPageInd:
                nextInd = ind.value
                curInd = self._countPages + self._curPageInd
            else:
                nextInd = self._countPages + ind.value
                curInd = self._curPageInd
        else:
            nextInd = ind.value
            curInd = self._curPageInd
        self._curPageInd = ind.value

        if nextInd > curInd:
            for _ in range(nextInd - curInd):
                self.Digit_2()
        elif nextInd < curInd:
            for _ in range(curInd - nextInd):
                self.Digit_1()

    def OpenFilters(self):
        self.E()
        self.Down()
        self.E()

    def SelectVertMenuElem(self, ind: int):
        if ind > 0:
            for _ in range(ind):
                self.Up()
        elif ind < 0:
            for _ in range(abs(ind)):
                self.Down()
        self.E()
    
    def SelectFiltersOption(self, ind: FiltrOptions):
        if ind.value == self._curFiltrInd:
            self.E()
            return
        
        nextInd = 0
        curInd = 0

        if abs(ind.value - self._curFiltrInd) > self._countFiltrOption / 2:
            if ind.value > self._curFiltrInd:
                nextInd = ind.value
                curInd = self._countFiltrOption + self._curFiltrInd
            else:
                nextInd = self._countFiltrOption + ind.value
                curInd = self._curFiltrInd
        else:
            nextInd = ind.value
            curInd = self._curFiltrInd
        self._curFiltrInd = ind.value

        if nextInd > curInd:
            for _ in range(nextInd - curInd):
                self.Up()
        elif nextInd < curInd:
            for _ in range(curInd - nextInd):
                self.Down()
        self.E()

    def BlockItem(self):
        Inkey.E()
        Inkey.Down()
        Inkey.Down()
        Inkey.E()

    def StoreItem(self):
        Inkey.E()
        Inkey.Up()
        Inkey.E()

Inkey = InputKey()

class PyGui:
    def TryFoundElement(self, elem: str):
        try:
            print("TryFoundElement " + elem)
            pyautogui.locateCenterOnScreen(elem, confidence=0.9)
            print("FTryFoundElementND " + elem + " SUCCESS")
            return True
        except pyautogui.ImageNotFoundException:
            print("TryFoundElement " + elem + "FAILED")
            return False

    def ClickToElement(self, elem: str):
        try:
            print("ClickToElement " + elem)
            uiElem = pyautogui.locateCenterOnScreen(elem, confidence=0.9)
            pyautogui.click(uiElem)
            print("FTryFoundElementND " + elem + " SUCCESS")
        except pyautogui.ImageNotFoundException:
            print("Update " + elem)
            Inkey.Down
            Inkey.Up
            self.ClickToElement(elem)

GUI = PyGui()

def TestFunction():
    favorite = pyautogui.locateOnScreen("element.png")
    pyautogui.doubleClick(favorite)

    GUI.ClickToElement("element_2.png")

    GUI.ClickToElement("deleting_from_favorites.png")

    GUI.ClickToElement("items.png")

    GUI.ClickToElement("element_2.png")

    GUI.ClickToElement("set_button.png")

def SortOrangeOptions():
    # переключиться на панель со всей эквипой
    Inkey.SelectPage(Pages.AllItems)
    # зайти в фильтры
    Inkey.OpenFilters()
    # выбрать передаваемые свойства
    Inkey.SelectFiltersOption(FiltrOptions.InheritSpecialOption1)
    # выбрать перманентно передаваемые
    Inkey.SelectVertMenuElem(-2)
    # вернуть фокус в изначальную позицию и отфильтровать
    Inkey.SelectFiltersOption(FiltrOptions.Use)
    print("Фильтр по перманентно наследуемым свойствам применён")
    # обработка итемов до тех пор пока не выведется сообщение об отсутсвии
    while not GUI.TryFoundElement('./Res/FiltersOptions/NotFound.png'):
        # если найден отфильтрованный итем, то лочим и перекладываем на склад
        #  заблокировать
        Inkey.BlockItem()
        #  скинуть на склад
        Inkey.StoreItem()
        time.sleep(0.3)
    # TODO: сброс состояния фильтра
    Inkey.E()

# Отборка по наследованию редкости
def SortInheritanceRarity():
    # переключиться на панель со всей эквипой
    Inkey.SelectPage(Pages.AllItems)
    # зайти в фильтры
    Inkey.OpenFilters()
    # выбрать фильтр по особым свойствам
    Inkey.SelectFiltersOption(FiltrOptions.SpecialOption2)
    # выбрать свойство Наследование редкости (слияние) TODO: надо вынести эти свойства в дальнейшем
    for _ in range(6):
        Inkey.Left()
    Inkey.SelectVertMenuElem(7)
    # вернуть фокус в изначальную позицию и отфильтровать
    Inkey.SelectFiltersOption(FiltrOptions.Use)
    print("Фильтр по наследование редкости задействован")
    while not GUI.TryFoundElement('./Res/FiltersOptions/NotFound.png'):
        # если найден отфильтрованный итем, то лочим и перекладываем на склад
        #  заблокировать
        # TODO пропускать с наследованием милости
        Inkey.BlockItem()
        #  скинуть на склад
        Inkey.StoreItem()
        time.sleep(0.3)
    # TODO: сброс состояния фильтра
    Inkey.E()

# Отборка по наследованию мислости
def SortInheritanceGrace():#
    pass

GUI.ClickToElement("element.png")
#TestFunction()
SortOrangeOptions()
SortInheritanceRarity()