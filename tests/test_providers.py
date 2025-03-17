from coverage_pre_commit.common.enums import Providers


class TestProviders:
	def test_providers_enum_names(self):
		assert "UNITTEST" in Providers.names
		assert "PYTEST" in Providers.names

	def test_providers_enum_values(self):
		unittest_provider = Providers.UNITTEST.value
		pytest_provider = Providers.PYTEST.value

		assert unittest_provider["name"] == "unittest"
		assert pytest_provider["name"] == "pytest"

		assert unittest_provider["command"] == "coverage run -m unittest"
		assert pytest_provider["command"] == "pytest"

		assert unittest_provider["dependencies"] == []
		assert pytest_provider["dependencies"] == ["pytest-cov>=2.0.0"]
