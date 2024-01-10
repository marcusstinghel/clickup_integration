import logging as log


class Log:

    @staticmethod
    def configurator():
        open('log.txt', 'w').close()
        fmt_log = '%(asctime)s - %(levelname)s - %(message)s'
        fmt_date = '%d/%m/%Y %H:%M:%S'
        log.basicConfig(filename='log.txt', level=log.DEBUG, format=fmt_log, datefmt=fmt_date, encoding='utf-8')
