import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",format=",*")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger