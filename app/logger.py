import logging
import logging.config


class Logger:
    @staticmethod
    def setup_logger():
        logging.config.dictConfig({
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                },
            },
            'handlers': {
                'default': {
                    'level': 'DEBUG',
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': 'DEBUG',
                    'propagate': True
                }
            }
        })

        app_logger = logging.getLogger(__name__)
        app_logger.debug("Logger is set up.")
        return app_logger


logger = Logger.setup_logger()
