from os import rename, path, stat
import hashlib

from bot_models.db import Database

class TelegramModel:
    def save_pending_gif(self, get_file, file_id):
        gif_temp_path = f"static/temp/{file_id}.mp4"
        get_file(file_id).download(gif_temp_path)
        return gif_temp_path

    def submit_gif(self, pending_gif_url):
        file_hash = File().video_sha256_hash(pending_gif_url)
        new_gif_path = f"static/gifs/{file_hash}.mp4"
        status = "new"
        if File().exists(new_gif_path):
            status = "exists"
        rename(pending_gif_url, new_gif_path)
        return {"gif_path": new_gif_path, "status": status}

    def find_related_gifs(self, query):
        keywords = query.split(" ")
        is_query_empty = query == ""
        keywords_len = len(keywords)
        all_gifs = Database().get_all_gifs()
        gifs_included_similarities = list()
        for gif in all_gifs:
            descripton = gif.description
            included_keywords_count = 0
            if is_query_empty is True:
                gifs_included_similarities.append((1, gif))
            else:
                for keyword in keywords:
                    if keyword in descripton:
                        included_keywords_count += 1
                similarity = included_keywords_count / keywords_len
                if similarity != 0:
                    gifs_included_similarities.append((similarity, gif))
        gifs_included_similarities.sort(key=lambda gif: gif[0], reverse=True)
        return gifs_included_similarities
        

class File:
    def video_sha256_hash(self, filename):
        with open(filename, "rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha256(bytes).hexdigest();
            f.close()
            return readable_hash
    def exists(self, file_path):
        return path.exists(file_path)