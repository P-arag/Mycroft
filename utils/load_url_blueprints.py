def load_urls(username: str, location: str = "./Resources/url_blueprints.txt") -> list:
    """
    Loads the urls from the specified blueprint file and sets the username as well
    :param username
    :param location
    :return: lisitfied urls with added usernames
    """
    final_list = []
    with open(location) as file:
        for line in file.readlines():
            if "{}" in line:
                line = line.format(username)
                final_list.append(line.strip("\n"))
        file.close()
    return final_list


def dump_url(url: str, location: str = "./mycroft_dump.lst") -> None:
    """
    Dumps an url to a specified location
    :param url:
    :param location:
    :return: None
    """
    with open(location, "a") as f:
        f.write(url+"\n")
    f.close()
