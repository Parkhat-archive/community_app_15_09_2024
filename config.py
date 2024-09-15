class Config:  # Определяем базовый класс конфигурации
    DEBUG = False  # Устанавливаем режим отладки в False (выключен)
    TESTING = False  # Устанавливаем режим тестирования в False (выключен)
    # SQLALCHEMY_DATABASE_URI = ('sqlite:///:memory:example')  # Пример URI для базы данных SQLite в памяти (закомментировано)
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:parhat1994@localhost:3306/Community_pulse'  # Пример URI для подключения к MySQL (закомментировано)
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:/Users/Parkhat Bazakov/PycharmProjects/pythonProject/Community_Pulse_final_project/your_database_name.db"  # URI для подключения к базе данных SQLite по указанному пути

class DevelopmentConfig(Config):  # Класс конфигурации для разработки, наследует от Config
    DEBUG = True  # Включаем режим отладки

class TestingConfig(Config):  # Класс конфигурации для тестирования, наследует от Config
    DEBUG = True  # Включаем режим отладки
    TESTING = True  # Включаем режим тестирования
