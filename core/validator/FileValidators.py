# coding=utf-8

from enum import Enum
class FileValidators(Enum):
    TABLE = 1
    SEQUENCE = 2
    INDEX = 3
    PACKAGE = 4
    PACKAGE_BODY = 5
<<<<<<< Updated upstream
    CONSTRAINT = 6
    NO_CONSTRAINT = 7
    VIEW_BI = 8
    VIEW_DATA = 9
    VIEW_JOIN =  10
    VIEW_LOV = 11
    VIEW_REPORT = 12
=======
    CONSTRAINT_FK = 6
    CONSTRAINT_NOFK = 7
    TRIGGER = 8
    VIEW_BI = 9
    VIEW_DATA = 10
    VIEW_JOIN =  11
    VIEW_LOV = 12
    VIEW_REPORT = 13
>>>>>>> Stashed changes
