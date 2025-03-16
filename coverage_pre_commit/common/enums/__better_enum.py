from enum import Enum, EnumMeta, IntEnum, StrEnum


class __MetaEnum(EnumMeta):
	def __new__(metacls, cls, bases, classdict, **kwds):
		prefix = kwds.pop("prefix", "")

		enum_class = super().__new__(metacls, cls, bases, classdict, **kwds)

		for member in enum_class.__members__.values():
			if isinstance(member._value_, str):
				member._value_ = prefix + member._value_

		return enum_class

	@property
	def names(cls):
		return sorted(cls._member_names_)

	@property
	def values(cls):
		return sorted(list(map(lambda x: x.value, cls._member_map_.values())))


class __BetterEnum(Enum, metaclass=__MetaEnum):
	pass


class __BetterIntEnum(IntEnum, metaclass=__MetaEnum):
	pass


class __BetterStrEnum(StrEnum, metaclass=__MetaEnum):
	pass
