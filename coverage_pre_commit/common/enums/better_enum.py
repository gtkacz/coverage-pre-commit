from enum import Enum, EnumMeta, IntEnum, StrEnum
from typing import List


class MetaEnum(EnumMeta):
	"""
	Metaclass for `BetterEnum`. Allows to add a prefix to all the values of an enum.
	Also adds `names` and `values` properties to the enum.
	"""

	def __new__(metacls, cls, bases, classdict, **kwargs):  # noqa: ANN001, ANN003, ANN204, D102
		prefix = kwargs.pop("prefix", "")

		enum_class = super().__new__(metacls, cls, bases, classdict, **kwargs)

		for member in enum_class.__members__.values():
			if isinstance(member._value_, str):
				member._value_ = prefix + member._value_

		return enum_class

	@property
	def names(cls) -> List[str]:
		"""
		Returns the names of the enum.

		Returns:
			List[str]: Names of the enum.
		"""
		return cls._member_names_

	@property
	def values(cls) -> List[str]:
		"""
		Returns the values of the enum.

		Returns:
			List[str]: Values of the enum.
		"""
		return list(map(lambda x: x.value, cls._member_map_.values()))


class BetterEnum(Enum, metaclass=MetaEnum):
	"""
	BetterEnum is an `enum.Enum` subclass that allows to add a prefix to all the values of the enum.
	Also adds `names` and `values` properties to the enum.

	Args:
		prefix (str, optional): Prefix to add to all the values of the enum. Defaults to "".
	"""


class BetterIntEnum(IntEnum, metaclass=MetaEnum):
	"""
	BetterIntEnum is an `enum.IntEnum` subclass that allows to add a prefix to all the values of the enum.
	Also adds `names` and `values` properties to the enum.

	Args:
		prefix (str, optional): Prefix to add to all the values of the enum. Defaults to "".
	"""


class BetterStrEnum(StrEnum, metaclass=MetaEnum):
	"""
	BetterIntEnum is an `enum.StrEnum` subclass that allows to add a prefix to all the values of the enum.
	Also adds `names` and `values` properties to the enum.

	Args:
		prefix (str, optional): Prefix to add to all the values of the enum. Defaults to "".
	"""
