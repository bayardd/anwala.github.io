import tweepy
import pickle
import json
import requests
import csv
import copy

def grabFollowers(userID):

    consumerKey = "C4ahlSSZeiKXVeBseLJTyJuiA"
    consumerSecret = "XRTXkeKYlJt1D17PXWa9hXcJgKtBpUo9RDFCBeGqnsLnAweW2E"
    accessToken = "1093707702033891329-XPvqu21IqAK6yJhTgm8e63X4ICJnfu"
    accessSecret = "ToCPaNh7nr7dEJonE1OmNMsJqKRqaSA1RicLAxVoENTvU"


    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    maxFriends = 200;
    tweetsCountMax = 100;
    followers = []
    counter = 0

    try:
        for user in tweepy.Cursor(api.followers, screen_name="acnwala").items():
            followers.append(user)
            counter += 1

    except:
        print("error")
                    ## Encode To JSON File
    with open('EncodedFollowers.json', 'wb') as file:
        pickle.dump(followers, file, protocol=pickle.HIGHEST_PROTOCOL)

    # for follower in followers:
        # print(follower)
        # print(follower.name)
        # print(follower.followers_count)

    with open('FollowerRecords.csv', mode='w') as csv_file:
        fieldnames = ['User', 'FriendCount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'User' : "acnwala", 'FriendCount' : counter})
        for follower in followers:
            writer.writerow({'User': follower.name, 'FriendCount': follower.followers_count})

def grabFollowing():

    consumerKey = "C4ahlSSZeiKXVeBseLJTyJuiA"
    consumerSecret = "XRTXkeKYlJt1D17PXWa9hXcJgKtBpUo9RDFCBeGqnsLnAweW2E"
    accessToken = "1093707702033891329-XPvqu21IqAK6yJhTgm8e63X4ICJnfu"
    accessSecret = "ToCPaNh7nr7dEJonE1OmNMsJqKRqaSA1RicLAxVoENTvU"


    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    maxFriends = 200;
    tweetsCountMax = 100;
    following = []
    writeData = []
    counter = 0

    try:
        # Returns an array of integers for each friends id
        following = tweepy.Cursor(api.friends_ids, screen_name="acnwala").items()
            
        for item in following:
            counter += 1
            # print(counter)
            # print(item)
            
            user = api.get_user(user_id=item)
            
            formatFollowing = {'Friend_Name' : user.screen_name, 'Number_Following' : user.friends_count}

            toDict = copy.copy(formatFollowing)

            writeData.append(toDict)
    except:
        print("error")
                    ## Encode To JSON File
    with open('EncodedFollowersExtraCredit.json', 'wb') as file:
        pickle.dump(writeData, file, protocol=pickle.HIGHEST_PROTOCOL)

   

    with open('FollowerRecordsExtraCredit.csv', mode='w') as csv_file:
        fieldnames = ['User', 'FriendCount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'User' : "acnwala", 'FriendCount' : counter})

        for follower in writeData:
            writer.writerow({'User': follower['Friend_Name'], 'FriendCount': follower['Number_Following']})




    # uri = "https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=acnwala&skip_status=true&include_user_entities=false"
    # response = requests.get(uri, allow_redirects=True, timeout=30)
    # print(response.text)
