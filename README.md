# Team_sacredgamers_codefundo_MS
Microsoft CodeFunDo++ 2018 Hackathon-Natural Disasters Prediction and Control Systems.

*Predicting natural disasters and calamities by sentiment analysis and automated alert system*

  The users of social networks tend to generate a large amount of information, which can definitely help in generating useful results by the use of highly accurate recommender systems. The only existing methodology of reporting is the media, i.e. news, radio etc. Such methodologies are time consuming and fail to report people immediately, resulting in human and economic losses. Cities like Mumbai and Delhi face severe problems of floods and smog respectively on a regular basis and public has not enough information to decide if they should get out of their home to work. A fire event takes around 3 hours to be shown in news while there is a substantial presence of it in social media under just 15 minutes. 

  We are going to implement mechanisms for keyword extraction from tweets doing sentiment analysis. Users will be authenticated using certain criteria. Particle filter mechanisms can be used to estimate the location of calamities. The system can use this information to analyze spatial and temporal pattern of an event (considering  twitter users as sensors) as well as the peaks of keywords like “flood”, “earthquake”, “tsunami”, “scarcity”, “smog”, “accident”, etc. Stemming algorithm will be used to reduce all variants of a word to a common word.
  So, basically we are going to build a webapp which outputs the status of impending/occured dangers or disasters public, rescue teams, and government authorities should be alerted about.  
Applications of out Tweet crawler - Real time location-wise analysis for natural disasters such as impending stormfalls, famines, diseases, pollution smog, cyclones, hurricanes, water scarcity: Basically everything the public needs to be alerted about.
Tweet Crawler will analyze the rate of increase of keywords tweeted i.e. sentiment analysis:
  -Considering the repeated tweets by the same individual only if they are separated by a particular time interval threshold.
  -Considering only those tweets whose id was created at least three hours ago, in order to filter spam. 
  A dashboard will be present wherein major updates will be displayed. Notifications will be sent to people who’ve signed up, including but not limited to email alerts. We will send the email to subscribed users as well as to all of the available rescue teams and government authorities in case of level 3 warning.(B2B and B2C)

Technologies Used:
| MongoDB | Node.js | GitHub | Microsoft Azure | State-of-the-art NLP and ML Algorithms | 
