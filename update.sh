git commit -m 'Commiting any local changes to production branch' -a
git push
git checkout master
git pull
git checkout production
git merge master production -m 'Keeping production up to date with master'
git push
/home/jonathanrbarney/elichor.com/env/bin/python /home/jonathanrbarney/elichor.com/bid/manage.py collectstatic
touch /home/jonathanrbarney/tmp/restart.txt

