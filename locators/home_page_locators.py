from selenium.webdriver.common.by import By


class HomePageLocators:
	SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[ text()="Войти в аккаунт" ]')  #кнопка входа в аккаунт
	CHECKOUT_BUTTON = (By.XPATH, '//button[ text()="Оформить заказ" ]')  #кнопка оформить заказ
	INVALID_PASSWORD_ERROR = (By.XPATH, '//p[ text()="Некорректный пароль" ]')  #ошибка неккоректный пароль
	PERSONAL_ACCOUNT_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')  #личный кабинет
	RESET_PASSWORD_LINK = (By.XPATH, '//a[ text()="Восстановить пароль" ]')  #ссылка на кнопку восстановить пароль
	CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]')  #constructor button
	LOGO_STELLAR_BURGER_HOME_PAGE = (
	By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  #лого
	BUTTON_FEED_ORDERS = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
	INGREDIENT_LINK = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
	FEED_BUTTON = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
	MAKE_BURGER_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')
	DETAILS_OF_INGREDIENT = (By.XPATH, '//p[contains(text(),"Калории,ккал")]')
	INGREDIENT_FROM_CONSTRUCTOR = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
	INGREDIENT_FROM_CONSTRUCTOR_2 = (By.XPATH, '//img[@alt="Соус традиционный галактический"]')
	INGREDIENT_FROM_CONSTRUCTOR_3 = (By.XPATH, '//img[@alt="Биокотлета из марсианской Магнолии"]')
	BUTTON_CLOSE_MODAL_WINDOW_DETAILS_ING = (By.XPATH, '//section[contains(@class, '
									'"Modal_modal_opened")]//button[contains(@class, "close")]')
	BURGER_CONSTRUCTOR_BASKET = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
	COUNTER_INGREDIENT_IN_BASKET = (By.XPATH, '//p[@class="text text_type_digits-medium mr-3"]')
	MODAL_WINDOW_AFTER_CREATE_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
											 '(@class, "Modal_modal__container")]')
	#крестик для закрытия окна
	CLOSE_MOD_WINDOW_AFTER_CREATE_ORDER = By.XPATH, "//button[@type='button']"
	MODAL_NEW_ORDER_NUMBER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

