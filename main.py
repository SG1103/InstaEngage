import instapy
from instapy import InstaPy

# Credentials
USERNAME = ''  # Fill in your Instagram username
PASSWORD = ''  # Fill in your Instagram password

# Settings
HASHTAGS_TO_LIKE = ["bike", "velo"]
AMOUNT_TO_LIKE = 5
FOLLOW_PERCENTAGE = 50
COMMENT_PERCENTAGE = 50
COMMENTS = ["Nice!", "Sweet!", "Great"]


def main():
    # Initialize the session
    session = InstaPy(username=USERNAME, password=PASSWORD)
    session.login()

    # Like posts by tags
    session.like_by_tags(HASHTAGS_TO_LIKE, amount=AMOUNT_TO_LIKE)

    # Set following settings
    session.set_do_follow(True, percentage=FOLLOW_PERCENTAGE)

    # Set commenting settings
    session.set_do_comment(True, percentage=COMMENT_PERCENTAGE)
    session.set_comments(COMMENTS)

    # Interact with your followers
    # This will go through a given number of your followers and interact with their posts
    # This can be useful to see changes in followers' content.
    session.interact_user_followers([USERNAME], amount=10, randomize=True)

    # Interact with posts for specific hashtags and leave comments
    # This is useful for engaging with communities relevant to the hashtags
    for hashtag in HASHTAGS_TO_LIKE:
        session.interact_by_URL(urls=[f"https://www.instagram.com/explore/tags/{hashtag}/"], randomize=True,
                                interact=True)

    session.end()


if __name__ == "__main__":
    main()
