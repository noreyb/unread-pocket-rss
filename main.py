from repository.pocket import PocketRepository
from dotenv import load_dotenv
import os
from feedgenerator import Rss201rev2Feed
import xml.etree.ElementTree as ET


def main():
    # fetch unread & _untagged_ items
    load_dotenv()
    pocket = PocketRepository(
        consumer_key=os.environ.get("POCKET_CONSUMER_KEY"),
        access_token=os.environ.get("POCKET_ACCESS_TOKEN"),
    )

    # pickup 15 items randomly
    items = pocket.fetch_items_randomly(state="unread", tag="_untagged_", count=15)

    # rss
    feed = Rss201rev2Feed(
        title="Pocket Random",
        link="https://getpocket.com/",
        description="Pocket Random",
        language="ja",
    )

    for item in items:
        feed.add_item(
            title=item["title"],
            link=item["url"],
            description=item["excerpt"],
        )

    output_path = "./output/rss.xml"
    with open(output_path, "w") as f:
        f.write(feed.writeString("utf-8"))
    tree = ET.parse(output_path)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':
    main()
