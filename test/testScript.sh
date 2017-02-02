# !/usr/bin/bash

pwd
rm *.mp3
rm test/*.mp3

touch "abc def ghi.mp3"
touch "test/1 aaa bbb ddd .mp3"
ls -lsa *.mp3
ls -lsa test/*.mp3

./rmBiF.py --file test/b??.mp3 --file test/a*.mp3 --file test/v*.mp3 --file test/*.mp3 --file *.mp3


ls -lsa *.mp3
ls -lsa test/*.mp3
