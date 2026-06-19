from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """Represents a single keyword note with metadata."""
    keyword: str
    content: str
    source_url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_string(self) -> str:
        """Return a human-readable representation of the note."""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        url_str = self.source_url or "无来源"
        return (
            f"关键词: {self.keyword}\n"
            f"内容: {self.content}\n"
            f"来源: {url_str}\n"
            f"标签: {tag_str}\n"
            f"创建时间: {self.created_at}"
        )


@dataclass
class KeywordNoteCollection:
    """A collection of keyword notes with formatting utilities."""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        """Add a single note to the collection."""
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        """Return all notes containing the given keyword."""
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        """Return all notes that have the specified tag."""
        return [n for n in self.notes if tag in n.tags]

    def format_all(self, separator: str = "=" * 40) -> str:
        """Format all notes into a single readable string."""
        if not self.notes:
            return "暂无笔记。"
        parts = []
        for i, note in enumerate(self.notes, start=1):
            parts.append(f"笔记 #{i}")
            parts.append(note.to_string())
            parts.append(separator)
        return "\n".join(parts)

    def summary(self) -> str:
        """Return a brief summary of the collection."""
        return f"共 {len(self.notes)} 条笔记"


def main() -> None:
    """Demonstrate usage with example data."""
    collection = KeywordNoteCollection()

    collection.add_note(
        KeywordNote(
            keyword="爱游戏",
            content="爱游戏是一款专注于休闲娱乐的移动应用，提供丰富的游戏内容。",
            source_url="https://mainofficial-aiyouxi.com.cn",
            tags=["游戏", "娱乐", "移动端"]
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="爱游戏更新",
            content="爱游戏近期发布了新版本，优化了用户体验和性能。",
            source_url="https://mainofficial-aiyouxi.com.cn/updates",
            tags=["游戏", "更新"]
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="休闲游戏",
            content="休闲游戏是爱游戏平台的主要类别之一，适合碎片时间游玩。",
            tags=["游戏", "休闲"]
        )
    )

    print(collection.summary())
    print()
    print(collection.format_all())

    print("\n--- 搜索关键词 '爱游戏' ---")
    for note in collection.find_by_keyword("爱游戏"):
        print(note.to_string())
        print("-" * 30)

    print("\n--- 搜索标签 '游戏' ---")
    for note in collection.find_by_tag("游戏"):
        print(note.to_string())
        print("-" * 30)


if __name__ == "__main__":
    main()