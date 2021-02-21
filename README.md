Discord Bot: DisConnect<a name="TOP"></a>
===================

- - - - 
# Description #

A discord bot that allows the students to raise issues, ask questions, create suggestions all in a centralized manner to the professors. The professors and students could also connect in an off topic manner as well to build a connection. Students can also make a profile in which other students can access and could potentially build a connection.

- - - - 
# How to Run #
1. Create a .env file in the src folder in FrontEnd
2. Create a discord bot using the discord developer portal
3. In the .env file put DISCORD_TOKEN="<YOUR_TOKEN>" where YOUR_TOKEN is your bot token
4. Run the main.py file (python 3.7.9)
5. Run intellij 
6. Edit the configuration 
7. Set the main class as DisConnectApplication.java which is found in the src/main/java directory

- - - - 
# Commands #
_(note that the only the administrator can use administrator commands)_
## Administrator Commands ##
View Questions - !viewAsk {user}
 - {user} - The user's question list you want to look up (Optional) (Checks own list without argument)

View Suggestions - !viewSuggest {user}
 - {user} -  The user's question list you want to look up (Optional) (Checks own list without argument)

View All User Questions - !viewSuggestAll

View All User Suggestions - !viewSuggestAll

View Number of Queries - !mail

Answer Question - !resolveAsk {user} {index} "{message}"
 - {user} - The user's list you want to answer from
 - {index} - The number of the question you want to answer (Optional) (Resolves all without argument)
 - "{message}" - Your answer to the question in quotations (Optional)

Answer Suggestion - !resolveSuggest {user} {index} "{message}"
 - {user} - The user's list you want to answer from
 - {index} - The number of the suggestion you want to answer (Optional) (Resolves all without argument)
 - "{message}" - Your answer to the suggestion in quotations (Optional)


## Non-Administrator Commands ##

Ask - !ask "{message}"
 - "{message}" - The question you want to ask in quotations

Suggest - !suggest "{message}"
 - "{message}" - The suggestion you want to send in quotations

View Questions - !viewAsk

View Suggestions - !viewSuggest

Remove Question - !removeAsk {index}
 - {index} - The number of the question you want to remove

Remove Suggestion - !removeSuggest {index}
 - {index} - The number of the suggestion you want to remove

Start Poll - !poll "{options}"
 - "{options}" - The poll options you want in quotations. Can have up to 10 options
