## Twitter API Session (GC Digital Research Bootcamp)

### Getting your API key

1\. Join Twitter [here](https://twitter.com/signup?lang=en), if you're not already a member. You should enter your phone number when prompted.  
2\. If you already have a Twitter account, make sure you have a phone number attached to your account. (This is for verification purposes before Twitter will issue you a developer key.) To add a number, click your avatar on the top right of the Twitter home screen and click Settings. On the Settings menu, select Mobile and enter a valid phone number.  
3\. While logged in to your Twitter account, go [here](https://dev.twitter.com/apps/new) to begin the process of getting your API key.  
4\. Fill out the form. You will be asked for a website, but note that Twitter doesn't check if it's a real website or not as long as it's in this format http://www.xyz.com  
5\. You'll be redirected to a new screen that shows the name you entered for your application. Click the tab at the top that says"Keys and Access Tokens"  
6\. You'll see your Consumer Key and Consumer Secret, which look like long strings of letters and numbers. Copy them to an empty text file on your computer. Make sure to note which is the Key and which is the Secret!  
7\. Nearly done! While still on the "Keys and Access Tokens" page, scroll all the way to the bottom and click the "Create my access token" button.  
8\. Under the "Your Access Token" heading, copy the Access Token and Access Token Secret and put them in the text document. You should now  have four numbers: Consumer Key, Consumer Secret, Access Token Key, and Access token Secret.  

### Accessing the API

1\. Clone (or [download](https://github.com/smythp/twitter-workshop/archive/master.zip)) this repository to your computer and navigate to the folder once it's downloaded.  
2\. Open the my_keys.py file in your text editor.  
3\. Copy your four numbers (Consumer Key, Consumer Secret, Access Token Key, and Access Token Secret), replacing the xxx is on each relevant line. Make sure to keep the single quotes around the numbers.  
4\. Save the my_keys.py file  
5\. Make sure you have the Tweepy library for Python installed. To check, type

	python

at the command line. When you see the >>> prompt, type

    import tweepy

If you see no output, then Tweepy is already installed, so skip to step #7. If you get an error, follow step #6. Once you're finished with Python, type

    exit()

to return to the bash shell  
6\. If Tweepy isn't installed, run

	pip install tweepy

at the bash shell to install the library.  
7\. To test out your key, run the api.py script:

	python api.py

If you see the name of your Twitter account, everything is working!  
8\. Once you have the api.py script working, open it with your editor and try uncommenting some of the other lines at the bottom. You should be able to post a tweet to your account and to perform a Twitter search.  
9\. Once you're comfortable connecting to the Twitter API, you can use the twitterbot.py script in this repository to create your own Twitterbot!  


### API Resources

[Programmable Web](http://www.programmableweb.com), a list of web-based APIs you can use in your projects.  
[Twitterbot examples](http://nymag.com/following/2015/11/12-weirdest-funniest-smartest-twitter-bots.html)  

