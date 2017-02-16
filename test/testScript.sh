# !/usr/bin/bash
echo "==============================================================="
echo "Test-Script fuer rmBiF.py"
echo "==============================================================="

pwd
rm test/*.mp3

touch "test/abc def ghi.mp3"
touch "test/1 aaa bbb ddd .mp3"
ls -lsa test/*.mp3
echo "-----------------------------------------------------------------------------------------------"
./rmBiF.py
echo "-----------------------------------------------------------------------------------------------"
./rmBiF.py --help
echo "-----------------------------------------------------------------------------------------------"
./rmBiF.py --dryrun --file test/b??.mp3 --file test/a*.mp3 --file test/v*.mp3 --file test/*.mp3 --file *.mp3


echo "------------------------------------- CamelCase -----------------------------------------------"
touch "test/zzz fff ghi.mp3"
ls -lsa test/zz*.mp3
./rmBiF.py --verbose --dryrun --file /test/zz*.mp3 --camelcase


echo "------------------------------------- Substitue Blank -----------------------------------------"
touch "test/zzz fff ghi.mp3"
ls -lsa test/zz*.mp3
./rmBiF.py --verbose --dryrun --file /test/zz*.mp3 --camelcase



ls -lsa test/*.mp3
