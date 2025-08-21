---
title: "Ubuntu in Termux"
author: "qtekfun"
date: "2025-02-17"
published: true
slug: "ubuntu-en-termux"
excerpt: "I've always wanted to have ubuntu in my tablet as it's lighter to move with and should be possible taking into account"
tags: ['desarrollo', 'programación']
---


# How to intsall proot Ubunut in Termux

I've always wanted to have ubuntu in my tablet as it's lighter to move with and should be possible taking into account
that Android is based on Linux. So let's go.

# Install Ubuntu's fs

1. Prerequisites

    ``` shell
    pkg update
    termux-setup-storage
    pkg install proot-distro pulseaudio vim
    ```

2.  Install proot Ubuntu

    ``` shell
    proot-distro install ubuntu
    ```

