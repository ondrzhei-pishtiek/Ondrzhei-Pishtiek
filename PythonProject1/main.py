import logging
import time
import os
from datetime import datetime

# Створити папку logs, якщо її немає
os.makedirs("logs", exist_ok=True)

# Налаштування логера
logging.basicConfig(
    filename="logs/task.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

start_time = time.time()

try:
    for i in range(0, 60, 5):
        current_time = datetime.now().strftime("%H:%M:%S")
        elapsed = int(time.time() - start_time)
        logging.info(f"Програма працює {elapsed} секунд(и). Поточний час: {current_time}")
        time.sleep(5)
    logging.error("Task completed")
except Exception as e:
    logging.error(f"Помилка: {str(e)}")
