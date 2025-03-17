from unittest import mock

from coverage_pre_commit.util import (
	get_metadata,
)


class TestMetadata:
	@mock.patch("configparser.RawConfigParser")
	def test_get_metadata_specific_key(self, mock_config_parser):
		mock_instance = mock_config_parser.return_value
		mock_instance.items.return_value = {"version": "0.1.0", "name": "coverage-pre-commit"}.items()

		result = get_metadata("version")
		assert result == "0.1.0"

		mock_instance.read.assert_called_once_with("setup.cfg")

	@mock.patch("configparser.RawConfigParser")
	def test_get_metadata_all(self, mock_config_parser):
		mock_instance = mock_config_parser.return_value
		expected_metadata = {"version": "0.1.0", "name": "coverage-pre-commit"}
		mock_instance.items.return_value = expected_metadata.items()

		result = get_metadata()
		assert result == expected_metadata

		mock_instance.read.assert_called_once_with("setup.cfg")
