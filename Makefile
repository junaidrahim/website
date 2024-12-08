update-theme:
	git submodule update --recursive --remote

server:
	hugo server

build:
	hugo


define new_post_content
cat > content/posts/new_post.md << EOF
---
title: "New Post"
date: "$(date '+%Y-%m-%d')"
summary: "New Post Description"
description: "New Post Description"
toc: true
readTime: true
autonumber: false
math: true
draft: false
---
EOF
endef

export script = $(value new_post_content)

newpost:; @eval "$$script"
	
	
