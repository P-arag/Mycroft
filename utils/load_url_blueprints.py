def load_urls(location: str = "./Resources/url_blueprints.txt") -> list:
    """
    Loads the urls from the specified file
    :param location:
    :return: list
    """
    final_list = []
    with open(location) as file:
        for line in file.readlines():
            if "{}" in line:
                final_list.append(line.strip("\n"))
        file.close()
    return final_list
