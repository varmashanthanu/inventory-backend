# Logging configuration
from project.env import DEBUG #, PAPERTRAIL_ENDPOINT, PAPERTRAIL_PORT TODO figure out logging solution

# We'll add 2 formatters, one basic standard, and one coloured for readability
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [SAVEMARTAPP] %(levelname)s %(name)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "colored": {
            "()":  "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(asctime)s [SAVEMARTAPP] %(levelname)s %(name)s %(bold_white)s%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG" if DEBUG else "INFO",
            "class": "logging.StreamHandler",
            "formatter": "colored",
            "filters": [],
        },
    },
    "loggers": {
        logger_name: {
            "level": "WARNING",
            "propagate": True,
            # "handlers": ["console"] if DEBUG else ["console", "papertrail"],
        } for logger_name in ("django", "django.request", "django.db.backends", "django.template",)
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
}
#
# if not DEBUG:
#     LOGGING["loggers"]["savemart_app"] = {
#         "level": "INFO",
#         "propagate": True
#     }
#     LOGGING["handlers"]["papertrail"] = {
#             "level": "INFO",
#             "class": "logging.handlers.SysLogHandler",
#             "formatter": "standard",
#             "address": (PAPERTRAIL_ENDPOINT, int(PAPERTRAIL_PORT)),
#         }
#     LOGGING["root"]["handlers"].append("papertrail")
