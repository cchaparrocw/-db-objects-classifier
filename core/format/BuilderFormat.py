# coding=utf-8
from core.format.ConstraintForeingKeyFormatter import ConstraintForeingKeyFormatter
from core.format.NoForeingKeyFormatter import NoForeingKeyFormatter
from core.format.IndexFormatter import IndexFormatter
from core.format.PackageFormatter import PackageFormatter
from core.format.ViewFormatter import ViewFormatter

from core.format.NotFormatter import NotFormatter
class BuilderFormat:

	def build(self):
		constraintForeingKeyFormatter = ConstraintForeingKeyFormatter()
		noForeingKeyFormatter = NoForeingKeyFormatter()
		constraintForeingKeyFormatter.setNext( noForeingKeyFormatter )
		indexFormatter = IndexFormatter()
		noForeingKeyFormatter.setNext(indexFormatter)

		packageFormatter= PackageFormatter()
		indexFormatter.setNext(packageFormatter)

		viewFormatter=ViewFormatter()
		packageFormatter.setNext(viewFormatter)

		notFormatter = NotFormatter()
		viewFormatter.setNext(notFormatter)

		return constraintForeingKeyFormatter
