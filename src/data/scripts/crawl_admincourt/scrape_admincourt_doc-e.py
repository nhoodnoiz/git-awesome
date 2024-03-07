import os
import hydra
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

ENCODING = "utf-8"
HREF_KEY = "href"


@hydra.main(version_base=None, config_path="./config", config_name="crawl_admincourt")
def main(cfg):
    config = cfg.crawl_data
    url_format = "https://www.admincourt.go.th/admincourt/site/{}"
    response = requests.get(url_format.format(config.source_website))
    soup = BeautifulSoup(response.text, "html.parser")
    html_links = soup.find_all("a", {"class": "btn btn-info me-md-2"})

    os.makedirs(config.output_folder, exist_ok=True)

    for html_link in tqdm(html_links):
        link = html_link[HREF_KEY]
        sub_url = url_format.format(link)
        sub_reponse = requests.get(sub_url)
        sub_reponse.encoding = ENCODING

        sub_soup = BeautifulSoup(sub_reponse.text, "html.parser")
        # sub_html_link = sub_soup.find("a", {"class": "btn btn-info text-start my-2"})
        sub_html_link = sub_soup.find("span", {"style": "font-size:18px"})
        sub_html_link = sub_html_link.find_all("a")

        file_link = sub_html_link[-1][HREF_KEY]

        # These two pages have broken url, so the urls are inserted manually.
        if html_link[HREF_KEY] == "09bookdetail-6751.html":
            file_link = url_format.format(config.source_url_1)
        if html_link[HREF_KEY] == "09bookdetail-6759.html":
            file_link = url_format.format(config.source_url_2)

        date = sub_soup.find(
            "div", {"class": "bg-info bg-gradient w-100 p-2 text-end text-reset"}
        )
        date_tag = date.contents[0].text
        data_name = "-".join(date_tag.split(":")[-1].split(" ")[1:-1])

        local_file_name = data_name + "+" + file_link.split("/")[-1]
        local_file_path = os.path.join(config.output_folder, local_file_name)

        with open(local_file_path, "wb") as file:
            file.write(requests.get(file_link).content)


if __name__ == "__main__":
    main()  # type: ignore
