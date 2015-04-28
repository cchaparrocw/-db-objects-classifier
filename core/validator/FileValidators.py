# coding=utf-8

from enum import Enum
class FileValidators(Enum):
    NO_VALID = 0
    TABLE = 1
    SEQUENCE = 2
    INDEX = 3
    PACKAGE = 4
    PACKAGE_BODY = 5
    CONSTRAINT_FK = 6
    CONSTRAINT_NOFK = 7
    TRIGGER = 8
    VIEW_BI = 9
    VIEW_DATA = 10
    VIEW_JOIN =  11
    VIEW_LOV = 12
    VIEW_REPORT = 13
