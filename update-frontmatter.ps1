# PowerShell script to update front matter in migrated blog posts

$postsPath = "d:\repos\MyBlogJS\posts"
$author = "qtekfun"

# Get all migrated posts (those with date in filename)
$migratedPosts = Get-ChildItem -Path $postsPath -Name "*.md" | Where-Object { $_ -match '^\d{4}-\d{2}-\d{2}-' }

foreach ($file in $migratedPosts) {
    $filePath = Join-Path $postsPath $file
    Write-Host "Processing: $file"
    
    # Extract date from filename (YYYY-MM-DD format)
    if ($file -match '^(\d{4}-\d{2}-\d{2})-(.+)\.md$') {
        $date = $matches[1]
        $slug = $file -replace '\.md$', ''
        
        # Read the file content
        $content = Get-Content -Path $filePath -Raw
        
        # Extract current front matter
        if ($content -match '^---\s*\n(.*?)\n---\s*\n(.*)$' -replace "`r", "") {
            $frontMatter = $matches[1]
            $bodyContent = $matches[2].Trim()
            
            # Extract title and category from old front matter
            $title = ""
            $category = ""
            
            if ($frontMatter -match 'title:\s*"([^"]+)"' -or $frontMatter -match "title:\s*'([^']+)'" -or $frontMatter -match 'title:\s*(.+)') {
                $title = $matches[1].Trim()
            }
            
            if ($frontMatter -match 'categories:\s*(.+)') {
                $category = $matches[1].Trim()
            }
            
            # Generate excerpt from first paragraph of content
            $lines = $bodyContent -split "`n"
            $excerpt = ""
            foreach ($line in $lines) {
                $line = $line.Trim()
                if ($line -and $line -notmatch '^#' -and $line -notmatch '^>') {
                    $excerpt = $line -replace '^\*\*|^\*|^-|^\d+\.' # Remove markdown formatting
                    if ($excerpt.Length -gt 100) {
                        $excerpt = $excerpt.Substring(0, 100) + "..."
                    }
                    break
                }
            }
            
            # Convert category to tags array
            $tags = @()
            switch ($category) {
                "software-development" { $tags = @("desarrollo", "programación", "software") }
                "devops" { $tags = @("devops", "sistemas", "administración") }
                "computer-things" { $tags = @("tecnología", "hardware", "sistemas") }
                "networks" { $tags = @("redes", "networking", "tecnología") }
                "random-stuff" { $tags = @("misc", "tips", "tecnología") }
                default { $tags = @("tecnología", "desarrollo") }
            }
            
            # Create new front matter
            $newFrontMatter = @"
---
title: "$title"
author: "$author"
date: "$date"
published: true
slug: "$slug"
excerpt: "$excerpt"
tags: [$($tags | ForEach-Object { '"' + $_ + '"' } | Join-String -Separator ', ')]
---
"@
            
            # Combine new front matter with body content
            $newContent = $newFrontMatter + "`n`n" + $bodyContent
            
            # Write back to file
            Set-Content -Path $filePath -Value $newContent -Encoding UTF8
            Write-Host "Updated: $file" -ForegroundColor Green
        }
    }
}

Write-Host "`nFront matter update completed!" -ForegroundColor Yellow
