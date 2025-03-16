import configparser
from typing import Dict, Optional, Union


def get_metadata(key: Optional[str] = None) -> Union[str, Dict[str, str]]:
	"""
	Retrieve metadata from setup.cfg. If key is provided, return the value of that key.
	Otherwise, return the entire metadata dictionary.

	Args:
			key (Optional[str], optional): The key to retrieve from the metadata. Defaults to None.

	Returns:
			Union[str, Dict[str, str]]: The value of the key if provided, otherwise the entire metadata dictionary.
	"""
	config = configparser.RawConfigParser()
	config.read("setup.cfg")

	metadata = dict(config.items("metadata"))

	if key:
		return metadata[key]

	return metadata
