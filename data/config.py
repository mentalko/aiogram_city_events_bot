from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
MODERATE_CHAT = env.str("MODERATE_CHAT")  #чат куда приходит сообщение модерации
WEBHOOK_URL = env.str("WEBHOOK_URL")  #чат куда приходит сообщение модерации
DB_HOST = env.str("DB_HOST") 
DB_NAME = env.str("DB_NAME") 
DB_USER = env.str("DB_USER") 
DB_PASS = env.str("DB_PASS") 

