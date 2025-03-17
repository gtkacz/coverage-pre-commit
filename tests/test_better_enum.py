from coverage_pre_commit.common.enums import BetterEnum, BetterIntEnum, BetterStrEnum


class TestBetterEnum:
	def test_better_enum_names_and_values(self):
		class TestEnum(BetterEnum):
			ONE = "one"
			TWO = "two"
			THREE = "three"

		assert TestEnum.names == ["ONE", "TWO", "THREE"]
		assert TestEnum.values == ["one", "two", "three"]

	def test_better_enum_with_prefix(self):
		class TestEnum(BetterEnum, prefix="prefix_"):
			ONE = "one"
			TWO = "two"
			THREE = "three"

		assert TestEnum.ONE.value == "prefix_one"
		assert TestEnum.TWO.value == "prefix_two"
		assert TestEnum.THREE.value == "prefix_three"

		assert TestEnum.values == ["prefix_one", "prefix_two", "prefix_three"]

	def test_better_enum_access_by_name(self):
		class TestEnum(BetterEnum):
			ONE = "one"
			TWO = "two"
			THREE = "three"

		assert TestEnum["ONE"] == TestEnum.ONE
		assert TestEnum["TWO"] == TestEnum.TWO
		assert TestEnum["THREE"] == TestEnum.THREE


class TestBetterIntEnum:
	def test_better_int_enum(self):
		class TestIntEnum(BetterIntEnum):
			ONE = 1
			TWO = 2
			THREE = 3

		assert TestIntEnum.names == ["ONE", "TWO", "THREE"]
		assert TestIntEnum.values == [1, 2, 3]

		# Test integer operations
		assert TestIntEnum.ONE + 1 == 2
		assert TestIntEnum.TWO * 2 == 4
		assert TestIntEnum.THREE // 2 == 1


class TestBetterStrEnum:
	def test_better_str_enum(self):
		class TestStrEnum(BetterStrEnum):
			ONE = "one"
			TWO = "two"
			THREE = "three"

		assert TestStrEnum.names == ["ONE", "TWO", "THREE"]
		assert TestStrEnum.values == ["one", "two", "three"]

		# Test string operations
		assert TestStrEnum.ONE + "_suffix" == "one_suffix"
		assert TestStrEnum.TWO.upper() == "TWO"
		assert TestStrEnum.THREE.replace("e", "a") == "thraa"

	def test_better_str_enum_with_prefix(self):
		class TestStrEnum(BetterStrEnum, prefix="prefix_"):
			ONE = "one"
			TWO = "two"
			THREE = "three"

		assert TestStrEnum.ONE.value == "prefix_one"
		assert "prefix" in TestStrEnum.ONE
		assert TestStrEnum.values == ["prefix_one", "prefix_two", "prefix_three"]
