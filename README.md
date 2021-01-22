# Smart Auto Insta

### Automate your Instagram postings with Python!

## Prepare

Place your credentials inside the [`cred.py`](src/cred.py) file and your new post info and post photo inside the [utils](utils) folder, as [`post_image.jpg`](utils/post_image.jpg) and [`post_info`](utils/post_info).

## Run

> Possibly outdated.
> Download the new Chrome driver version or update the XPath for the Instagram login page

Inside the [src](src) folder, run:

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip3 install -r requirements.txt`
4. `python3 insta_poster.py`
5. Wait for the Chrome Driver to open
6. Watch Python being an insta expert!

## Facebook Scrapper

The module [fb_scrap.py](src/fb_scrap.py) contains some code that scraps Facebook pages and downloads the most recent post info.