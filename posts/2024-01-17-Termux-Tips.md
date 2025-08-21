---
title: "Termux Tips"
author: "qtekfun"
date: "2024-01-17"
published: true
slug: "Termux-Tips"
excerpt: "To start working fast after installing Termux, the command I always run is:"
tags: ['desarrollo', 'programación']
---


To start working fast after installing Termux, the command I always run is:

```
pkg install root-repo x11-repo vim git openssh -y &&
pkg upgrade -y && 
termux-setup-storage && 
termux-change-repo
```