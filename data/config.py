from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
MODERATE_CHAT = env.str("MODERATE_CHAT")  #чат куда приходит сообщение модерации
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
DB_HOST = env.str("DB_HOST") 
DB_NAME = env.str("DB_NAME") 

