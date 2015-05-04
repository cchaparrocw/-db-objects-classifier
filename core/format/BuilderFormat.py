# coding=utf-8
from core.format.ConstraintForeingKeyFormatter import ConstraintForeingKeyFormatter
from core.format.NoForeingKeyFormatter import NoForeingKeyFormatter

from core.format.NotFormatter import NotFormatter
class BuilderFormat:

	def build(self):
		constraintForeingKeyFormatter = ConstraintForeingKeyFormatter()
		noForeingKeyFormatter = NoForeingKeyFormatter()
		constraintForeingKeyFormatter.setNext( noForeingKeyFormatter )

		notFormatter = NotFormatter()
		noForeingKeyFormatter.setNext(notFormatter)
		return constraintForeingKeyFormatter
