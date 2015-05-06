# coding=utf-8

from  core.validator.DefaultFileValidator import DefaultFileValidator
from core.validator.read.IndexReadingValidator import IndexReadingValidator
from core.validator.read.TablesReadingValidator import TablesReadingValidator
from core.validator.read.ConstraintReadingValidator import ConstraintReadingValidator

class BuilderReadingValidator:
    def build(self):
        tablesValidator     = TablesReadingValidator()
        constraintValidator = ConstraintReadingValidator()
        tablesValidator.setNext(constraintValidator)
        indexValidator      = IndexReadingValidator()
        constraintValidator.setNext(indexValidator)
        default             = DefaultFileValidator()
        indexValidator.setNext(default)
        return tablesValidator
