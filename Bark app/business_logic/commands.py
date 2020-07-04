from db.db_manager import DatabaseManager
from datetime import datetime
import sys

import requests

db = DatabaseManager("bookmarks.db")


class CreateBookmarksTableCommand:
    """Class that creates bookmarks table"""

    def execute(self):
        db.create_table(
            "bookmarks",
            {
                "id": "integer primary key autoincrement",
                "title": "text not null",
                "url": "text not null",
                "notes": "text",
                "date_added": "text not null",
                "date_updated": "text not null",
            },
        )


class AddBookMarkCommand:
    """Command for adding bookmark and returning success string"""

    def execute(self, data, timestamp=None):
        data["date_added"] = timestamp or datetime.utcnow().isoformat()
        data["date_updated"] = data["date_added"]
        db.add("bookmarks", data)
        return "Bookmarks Added"


class ListBookmarksCommand:
    """Command for getting all the bookmarks ordered by date added"""

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self):
        return db.select("bookmarks", order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    """Command for deleting a single bookmark"""

    def execute(self, data):
        db.delete("bookmarks", {"id": data})
        return "Bookmark deleted!"


class QuitCommand:
    """Command to exit the console"""

    def execute(self):
        sys.exit()


class ImportGitHubStarsCommand:
    def _extract_bookmark_info(self, repo):
        return {
            "title": repo["name"],
            "url": repo["html_url"],
            "notes": repo["description"],
        }

    def execute(self, data):
        bookmarks_imported = 0
        github_username = data["github_username"]
        next_page_of_results = f"https://api.github.com/users/{github_username}/starred"
        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"},
            )
            next_page_of_results = stars_response.links.get("next", {}).get("url")
            for repo_info in stars_response.json():
                repo = repo_info["repo"]
                if data["preserve_timestamps"]:
                    timestamp = datetime.strptime(
                        repo_info["starred_at"], "%Y-%m-%dT%H:%M:%SZ"
                    )
                else:
                    timestamp = None
                bookmarks_imported += 1
                AddBookMarkCommand().execute(
                    self._extract_bookmark_info(repo), timestamp=timestamp,
                )
        return f"Imported {bookmarks_imported} bookmarks from starred repos!"


class EditBookmarkCommand:
    def execute(self, data):
        db.update(
            "bookmarks", {"id": data["id"]}, data["update"],
        )
        return "Bookmark updated!"
