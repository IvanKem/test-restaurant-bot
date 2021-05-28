from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
host = env.str("ip")  # Тоже str, но для айпи адреса хоста
db_pass = env.str('DB_PASS')
db_user = env.str('DB_USER')