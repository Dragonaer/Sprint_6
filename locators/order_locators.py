from selenium.webdriver.common.by import By

class OrderButtons:
    """Локаторы на первой странице заказа"""
    NAME = (By.XPATH, "//input[@placeholder='* Имя']") #поле Имя
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']") #поле Фамилия
    ADRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") #поле Адреса доставки самоката
    SUBWAY_STATION_BUTTON = (By.XPATH, "//input[@placeholder='* Станция метро']") #поле со станцией метро
    SUBWAY_STATION = (By.XPATH, "//button//div[@class='Order_Text__2broi' and text()='Черкизовская']") # станция метро
    NUMBER_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") #поле с контактным номером

    FARTHER_BUTTON = (By.XPATH, "//div//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']") #кнопка Далее

    """Локаторы на второй странице заказа"""
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") #дата доставки самоката
    BODY = (By.XPATH, '//div[@class="Order_Header__BZXOb"]') #кликнуть на область вне поля    
    TERM = (By.CSS_SELECTOR, "div.Dropdown-root") #поле срока аренды
    TERM_ONE_DAY = (By.XPATH, "//div[text()='сутки']") #срок аренды 1 день
    TERM_TWO_DAY = (By.XPATH, "//div[text()='двое суток']") #срок аренды 2 дня
    BLACK_COLOUR = (By.XPATH, "//label[@for='black']") # цвет самоката Черный
    GREY_COLOUR = (By.XPATH, "//label[@for='grey']") # цвет самоката Серый
    BACK_BUTTON = (By.XPATH, "//button[contains(@class, Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i ') and text()='Назад']") # кнопка Назад
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") # кнопка Заказать в форме заказа

    """Локаторы в окне подтверждения заказа"""
    YES_BUTTON = (By.XPATH, "//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']") # кнопка Да в окне подтверждения заказа
    
    """Локатор в окне об успешном подтверждении заказа"""
    POPUP_TEXT = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space()='Посмотреть статус']") # кнопка Посмотреть статус в окне успешного заказа

