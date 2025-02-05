from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    UL_ORDER_FEED = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')  # Список всех заказов
    TITLE_ORDER_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')  # Заголовок "Лента заказов"
    FIRST_BURGER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]')  # модальное окно с заказом
    TITLE_MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]//h2')  # Заголовок модального окна
    ALL_ORDERS_QUANTITY = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')  # Всего заказов
    TODAY_ORDERS_QUANTITY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')  # Заказы сегодня
    ORDER_LIST_READY = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')  # заказы в работе
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    TITLE_ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    NUMBER_ORDER_IN_FEED_PAGE = (By.XPATH, './/*[text()="{order_id}"]')
    ID_ORDER_CARD = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
    CNT_ORDERS_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    CNT_ORDERS_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    # номер заказа в работе
    NUM_ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, '
                                   '"OrderFeed_orderListReady")]/li[contains(@class, '
                                   '"text_type_digits-default")]')
