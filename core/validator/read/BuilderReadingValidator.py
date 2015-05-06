# coding=utf-8

from  core.validator.DefaultFileValidator import DefaultFileValidator
from core.validator.read.IndexReadingValidator import IndexReadingValidator
from core.validator.read.TablesReadingValidator import TablesReadingValidator
from core.validator.read.ConstraintReadingValidator import ConstraintReadingValidator

class BuilderReadingValidator:
    def build(self):

        indexValidator = IndexReadingValidator()
        tablesValidator = TablesReadingValidator()
        indexValidator.setNext(tablesValidator)

        constraintValidator = ConstraintReadingValidator()
        tablesValidator.setNext( constraintValidator )

        default = DefaultFileValidator()
        tablesValidator.setNext(default)
        return indexValidator 
