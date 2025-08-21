#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path


def extract_date_from_filename(filename):
    """Extract date from filename format YYYY-MM-DD-title.md"""
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    return date_match.group(1) if date_match else "2025-08-21"


def extract_slug_from_filename(filename):
    """Extract slug from filename, removing date prefix and .md extension"""
    # Remove date prefix if present
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filename)
    # Remove .md extension
    slug = re.sub(r"\.md$", "", slug)
    return slug


def extract_category_to_tags(categories):
    """Convert old categories to new tags format"""
    if not categories:
        return ["general"]

    # If it's a string, convert to list
    if isinstance(categories, str):
        categories = [categories]

    # Map some common categories to more descriptive tags
    tag_mapping = {
        "computer-things": ["tecnología", "hardware"],
        "devops": ["devops", "automatización"],
        "networks": ["redes", "networking"],
        "random-stuff": ["miscelánea"],
        "software-development": ["desarrollo", "programación"],
    }

    tags = []
    for cat in categories:
        if cat in tag_mapping:
            tags.extend(tag_mapping[cat])
        else:
            # Clean up category name for tags
            clean_tag = cat.replace("-", " ").replace("_", " ").lower()
            tags.append(clean_tag)

    return tags


def extract_excerpt_from_content(content):
    """Extract first meaningful paragraph as excerpt"""
    # Split content into lines
    lines = content.split("\n")

    # Find first non-empty line that's not a header
    for line in lines:
        line = line.strip()
        if (
            line
            and not line.startswith("#")
            and not line.startswith("```")
            and len(line) > 20
        ):
            # Limit excerpt to about 150 characters
            if len(line) > 150:
                return line[:147] + "..."
            return line

    return "Artículo sobre tecnología y desarrollo."


def parse_old_frontmatter(content):
    """Parse old Jekyll-style frontmatter"""
    if not content.startswith("---"):
        return {}, content

    # Find end of frontmatter
    end_match = re.search(r"\n---\n", content)
    if not end_match:
        return {}, content

    frontmatter_text = content[3 : end_match.start()]
    remaining_content = content[end_match.end() :]

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter or {}, remaining_content
    except yaml.YAMLError:
        return {}, content


def create_new_frontmatter(old_frontmatter, filename, content):
    """Create new frontmatter structure"""

    # Extract date from filename
    date = extract_date_from_filename(filename)

    # Extract slug from filename
    slug = extract_slug_from_filename(filename)

    # Get title from old frontmatter or generate from filename
    title = old_frontmatter.get("title", slug.replace("-", " ").title())

    # Convert categories to tags
    categories = old_frontmatter.get("categories", old_frontmatter.get("category", []))
    tags = extract_category_to_tags(categories)

    # Extract excerpt from content
    excerpt = extract_excerpt_from_content(content)

    new_frontmatter = {
        "title": title,
        "author": "qtekfun",
        "date": date,
        "published": True,
        "slug": slug,
        "excerpt": excerpt,
        "tags": tags,
    }

    return new_frontmatter


def update_post_file(filepath):
    """Update a single post file"""
    print(f"Processing: {filepath.name}")

    # Read the file
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try with different encoding
        with open(filepath, "r", encoding="latin-1") as f:
            content = f.read()

    # Parse old frontmatter
    old_frontmatter, post_content = parse_old_frontmatter(content)

    # Create new frontmatter
    new_frontmatter = create_new_frontmatter(
        old_frontmatter, filepath.name, post_content
    )

    # Generate new content
    new_content = "---\n"
    new_content += f'title: "{new_frontmatter["title"]}"\n'
    new_content += f'author: "{new_frontmatter["author"]}"\n'
    new_content += f'date: "{new_frontmatter["date"]}"\n'
    new_content += f'published: {str(new_frontmatter["published"]).lower()}\n'
    new_content += f'slug: "{new_frontmatter["slug"]}"\n'
    new_content += f'excerpt: "{new_frontmatter["excerpt"]}"\n'
    new_content += f'tags: {new_frontmatter["tags"]}\n'
    new_content += "---\n\n"
    new_content += post_content

    # Write the updated file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Updated: {filepath.name}")
    return new_frontmatter


def main():
    posts_dir = Path("posts")

    if not posts_dir.exists():
        print("❌ Posts directory not found!")
        return

    # Find all markdown files that look like migrated posts (with date prefix)
    migrated_posts = []
    for file in posts_dir.glob("*.md"):
        # Skip files that already have the new format (no date prefix)
        if re.match(r"^\d{4}-\d{2}-\d{2}", file.name):
            migrated_posts.append(file)

    if not migrated_posts:
        print("No migrated posts found (looking for YYYY-MM-DD-*.md pattern)")
        return

    print(f"Found {len(migrated_posts)} migrated posts to update:")
    for post in migrated_posts:
        print(f"  - {post.name}")

    print("\nProcessing posts...")
    updated_count = 0

    for post_file in migrated_posts:
        try:
            update_post_file(post_file)
            updated_count += 1
        except Exception as e:
            print(f"❌ Error processing {post_file.name}: {e}")

    print(
        f"\n🎉 Successfully updated {updated_count} out of {len(migrated_posts)} posts!"
    )


if __name__ == "__main__":
    main()
