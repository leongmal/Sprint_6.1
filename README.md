# Sprint_6
Проект автоматизации сервиса "Самокат"

1.Фреймворк:
    Pytest - основа написания тестов
2.Технические требования:
    Selenium для автоматизации браузера
    GeckoDriver последней версии / webgriver
    Firefox актуальной версии
3.Необходимые установки :
	pip install pytest
	pip install selenium
    pip install -r requirements.txt
    pip install allure-pytest
4.Команда для запуска –
    pytest  -v                              # тестов
    pytest --alluredir=./allure-results     # запустить все тесты и записать отчет
    allure serve ./allure-results           # посмотреть отчет по прогону htm
