update-theme:
	hugo mod get -u

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
	
	
