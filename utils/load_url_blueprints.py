def load_urls( username: str, location: str = "./Resources/url_blueprints.txt") -> list:
    """
    Loads the urls from the specified blueprint file and sets the username as well
    :param username:
    :param location:
    :return: list
    """
    final_list = []
    with open(location) as file:
        for line in file.readlines():
            if "{}" in line:
                line = line.format(username)
                final_list.append(line.strip("\n"))
        file.close()
    return final_list
