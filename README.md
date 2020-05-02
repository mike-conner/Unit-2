# Unit-2
## Basketball Stats Tool
You have been given a list of teams and players. You've been tasked with cleaning up the player data and then organizing the players into equal teams for the upcoming basketball season.

You will apply your knowledge of built-in Python data types and combine these types to create structures to store and organize a team of Basketball players into distributed teams. This tool will not only balance the teams by the total number of players but also let you generate some statistics for a given team.

## Project Instructions
To complete this project, follow the instructions below. If you get stuck, ask a question on Slack or in the Treehouse Community.

1. Create a new script
The very first step you will want to do after opening the workspace or unzipping the .zip file into your project folder is to create a new and blank Python script named app.py or application.py.

2. Proper use of Dunder Main
Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file.

3. Import player data
Import from constants.py the players' data to be used within your program.

4. Create a clean_data function
   - Write the logic to:
     - read the existing player data from the PLAYERS constants provided in constants.py
     - clean the player data without changing the original data (see note below) 
     - save it to a new collection 
     - build a new collection with what you have learned up to this point.

   - Data to be cleaned:
     - Height: This should be saved as an integer
     - Experience: This should be saved as a boolean value (True or False)
     
    _HINT: Think Lists with nested Dictionaries might be one way._ _

    _**NOTE: Ensure you do not directly modify the data in PLAYERS or TEAMS constants. This data you should iterate and read from to build your own collection and would be ideal to clean the data as you loop over it building your new collection. If you are unsure of what this means, checkout this instruction step.**_

5. Create a balance_teams function
Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.

6. Console readability matters
When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

7. Displaying the stats
When displaying the selected teams' stats to the screen you will want to include:
   - Team's name as a string
   - Total players on that team as an integer
   - The player names as strings separated by commas
   
   _**NOTE: When displaying the player names it should not just display the List representation object. It should display them as if they are one large comma separated string so the user cannot see any hints at what data type players are held inside.**_


## Extra Credit
1.  Cleaning guardian field
When cleaning the data, clean the guardian field as well before adding it into your newly created collection, split up the guardian string into a List.

    _**NOTE: There can be more than one guardian, indicated by the " and " between their names.**_

2. Additional balancing to the team

   - Additionally, balance the teams so that each team has the same number of experienced vs. inexperienced players.

   - If this is done correctly each team stats should display the same number count for experienced total and inexperienced total as well as the same total number of players on the team.

3. Include additional stats for a given displayed team:
   - number of inexperienced players on that team
   - number of experienced players on that team
   - the average height of the team
   - the guardians of all the players on that team (as a comma-separated string)
   
   _**HINT: You can calculate the average height for a given team by keeping a running sum total of each players height on the team and dividing that total by the total number of players on that team.**_

4. Quit Menu Option
   - The user should be re-prompted with the main menu until they decide to "Quit the program".
