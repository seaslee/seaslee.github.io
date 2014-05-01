cp -r ~/myblog/output/*  .
cp -r ~/myblog/images .
git add --all .
git commit -m 'change the blog content'
git push origin master
