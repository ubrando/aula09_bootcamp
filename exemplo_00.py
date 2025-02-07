from time import sleep
from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")
def primeira_atividade():
    logger.info("Minha primeira atividade! - Hello World!")
    sleep(2)

def segunda_atividade():
    logger.info("Minha segunda atividade! - Hello World!")
    sleep(2)

def terceira_atividade():
    logger.info("Minha terceira atividade! - Hello World!")
    sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline finalizou!")

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(10)