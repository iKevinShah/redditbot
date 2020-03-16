# Reddit bot script to reply to comments based on a keyword. Original script from https://www.reddit.com/user/doug89
import praw

def remember(word):
    global matchedword
    matchedword = word
    return True

SUBREDDIT_NAME = 'somesubreddit'
KEYWORDS = ['keyword1','keyword2','keyword3','keyword4','keyword5']
 
USERNAME = 'SomeBot'
PASSWORD = 'SomeBotPassword'
CLIENT_ID = 'SomeID'
CLIENT_SECRET = 'SomeSecret'
 
USER_AGENT = 'script:replies to certain keywords in title / comments / post'

print("Authenticating as {}".format(USERNAME));
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent=USER_AGENT,
    username=USERNAME)

print("Authenticated as {}".format(reddit.user.me()));
print("---")
for comment in reddit.subreddit(SUBREDDIT_NAME).stream.comments():
    if comment.saved:
        continue
    has_keyword = any(k.lower() in comment.body.lower() and remember(k.lower()) for k in KEYWORDS)
    not_self = comment.author != reddit.user.me()
    if has_keyword and not_self:
        RESPONSE = 'Keyword matched: ' + matchedword
        comment.save()
        reply = comment.reply(RESPONSE)
        print('Comment posted: http://reddit.com{}'.format(reply.permalink));
        print('Comment body: {}'.format(RESPONSE));
        print('---');
