from urllib.parse import urlparse

def parse_database_uri(db_uri):
    """
    Parses the database URI into a dictionary of connection parameters.
    :param db_uri (str): The database URI to parse.
    :return: A dictionary containing the connection parameters
    """
    parsed_uri = urlparse(db_uri)

    # Extract components
    connection_params = {
        "dbname": parsed_uri.path.lstrip('/'),  # Remove leading slash
        "user": parsed_uri.username,
        "password": parsed_uri.password,
        "host": parsed_uri.hostname,
        "port": parsed_uri.port
    }

    return connection_params