import os


def _env(KEY, DEFAULT=None, TYPE=None):
    """
        Shorthand function to just read an environment variable
        and provide a default.

        Handles parsing of bool/int/list/str values correctly

        A couple of conventions exist when designing
        environment variables for settings.

         1. All values are stored as strings in the environment variable
         2. Bools are encoded as one of "1", "True" or "true" if True,
            all other values are interpreted as False
         3. lists are encoded as a string, with the list items
            separated with ","

                in example:  "a,b,c,   d"

            (intentinnally put whitespace in there. It is allowed)


        Default Values are preffered to be set to the same type as the setting.
        list -> [], str -> '', int -> 0, bool -> True/False etc

    """
    truthy = ["1", "True", "true"]

    if TYPE is None:
        # guessing type from default
        TYPE = type(DEFAULT) if DEFAULT is not None else str

    if TYPE is int:
        return int(os.environ.get(KEY, DEFAULT))

    elif TYPE is bool:
        return str(os.environ.get(KEY, DEFAULT)) in truthy

    elif TYPE is list:
        if KEY in os.environ:
            return [item.strip() for item in os.environ.get(KEY).split(',')]
        else:
            # This allows to put a default value of type list.
            # We wont ask for a list encoded as a comma-separated string
            # for default values. But they have to be so in the env var.
            #
            # Warning - if no default is set,
            # it will automatically be set to None.
            return DEFAULT

    return os.environ.get(KEY, DEFAULT)  # Default to string