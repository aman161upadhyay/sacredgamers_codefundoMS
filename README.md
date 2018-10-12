# Team_sacredgamers_codefundoMS
Microsoft CodeFunDo++ 2018 Hackathon-Natural Disasters Prediction and Control Systems.

*Predicting natural disasters and calamities by sentiment analysis and automated alert system*

  The users of the social network tend to generate a large amount of information, which can definitely help in generating useful results by the use of highly accurate recommender systems. The only existing methodology of reporting people is the media, i.e. news, radio etc. Such methodologies are time consuming and fail to report people immediately, resulting in human and economic losses.

  We are going to implement mechanisms for keyword extraction from tweets using Stemming Algorithm along with location and time of the tweets. The system can use this information to analyze the peaks of the keywords like “flood”, “earthquake”, “tsunami”, “help”, “scarcity”, “smog”, “accident”, etc. at a specific time and location.   
  So, basically we are going to build a webapp which, on taking the location of the user as an input, outputs the status of impending dangers or disasters they should be alerted about, if any.  
Things we are going to consider and execute:
1] Tweet crawler - Real time city-wise (location-wise) analysis for natural disasters such as impending stormfalls, famines, diseases, pollution smog, cyclones, hurricanes, water scarcity: Basically everything the public needs to be alerted about and can be alerted about!
2]Tweet Crawler will analyze the rate of increase of keywords tweeted i.e. sentiment analysis:
  -Considering the repeated tweets by the same individual only if they are separated by a particular time interval threshold.
  -Considering only those tweets whose id was created at least three hours ago, in order to filter spam. 
  A dashboard will be present wherein major updates will be displayed. Notifications will be sent to people who’ve signed up, including but not limited to email alerts. We will send the email to subscribed users as well as to all of the available rescue teams and government authorities in case of level 3 warning.(B2B and B2C)

Technologies Used:
MongoDB | Node.js | GitHub | Microsoft Azure | State-of-the-art NLP Algorithms | 
