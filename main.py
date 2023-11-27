import instaloader
import os
import time

def download_data(target_account):
    L = instaloader.Instaloader()
    username = "williampottsCS"
    password = "Willi@m2004Uni"
    L.login(username, password)

    profile = instaloader.Profile.from_username(L.context, target_account)

    output_folder = os.path.join(os.getcwd(), f"{target_account}_data")
    os.makedirs(output_folder, exist_ok=True)

    followers_list = []
    for follower in profile.get_followers():
        followers_list.append(follower.username)

    followers_file_path = os.path.join(output_folder, f"{target_account}_followers.txt")
    with open(followers_file_path, "w+") as followers_file:
        followers_file.write("\n".join(followers_list))

    total_posts = profile.mediacount

    likes_count = {}
    comments_count = {}

    for i, post in enumerate(profile.get_posts(), 1):
        likes_list = []
        for like in post.get_likes():
            likes_list.append(like.username)

            # Count likes for each user
            if like.username in likes_count:
                likes_count[like.username] += 1
            else:
                likes_count[like.username] = 1

        comments_list = []
        for comment in post.get_comments():
            comments_list.append(comment.text)

            # Count comments for each user
            commenter_username = comment.owner.username  # Use username attribute instead of owner_username
            if commenter_username in comments_count:
                comments_count[commenter_username] += 1
            else:
                comments_count[commenter_username] = 1

        comments_file_path = os.path.join(output_folder, f"{target_account}_post_{post.shortcode}_comments.txt")
        likes_file_path = os.path.join(output_folder, f"{target_account}_post_{post.shortcode}_likes.txt")

        with open(comments_file_path, "w+") as comments_file:
            comments_file.write("\n".join(comments_list))

        with open(likes_file_path, "w+") as likes_file:
            likes_file.write("\n".join(likes_list))

        time.sleep(45)

    # Get top 3 liked users
    top_liked_users = sorted(likes_count.items(), key=lambda x: x[1], reverse=True)[:3]

    # Get top 3 commenters
    top_commenters = sorted(comments_count.items(), key=lambda x: x[1], reverse=True)[:3]

    return top_liked_users, top_commenters