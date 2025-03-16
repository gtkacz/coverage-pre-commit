from enum import Enum, EnumMeta, IntEnum, StrEnum


class MetaEnum(EnumMeta):
	def __new__(metacls, cls, bases, classdict, **kwds):
		prefix = kwds.pop("prefix", "")

		enum_class = super().__new__(metacls, cls, bases, classdict, **kwds)

		for member in enum_class.__members__.values():
			if isinstance(member._value_, str):
				member._value_ = prefix + member._value_

		return enum_class

	@property
	def names(cls):
		return cls._member_names_

	@property
	def values(cls):
		return list(map(lambda x: x.value, cls._member_map_.values()))


class BetterEnum(Enum, metaclass=MetaEnum):
	pass


class BetterIntEnum(IntEnum, metaclass=MetaEnum):
	pass


class BetterStrEnum(StrEnum, metaclass=MetaEnum):
	pass
