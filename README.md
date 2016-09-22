# Spice Rack
This project creates an Amazon Alexa voice skill that helps you quickly locate
a particular spice in a crowded spice cabinet. You can use your voice to ask
"Where is the cinnamon?" and it will tell you the row and column of the spice.

There is a second, optional level of functionality planned, but not yet 
implemented. If used with a physical spice rack enhanced with a Raspberry Pi, 
it will turn on a light above the spice bottle.

## Use Cases
* Tell SR the location of a spice
* Tell SR the location of each spice in the rack
* Remove a spice from the rack
* Ask SR the location of a spice
* Ask SR the locations of several spice

# Installation
If you want to use the skill on your Amazon Echo or other Alexa-enabled
device:
* Say, "Alexa, install the Spice Finder skill"
* On your phone, you can use the Alexa app.
* On your computer, you can go to https://alexa.amazon.com 
 
Say "Alexa, run Spice Finder" to verify that is has been installed.

# Installation For Program Modification
If you want to install the source code in your Amazon developer account
and make changes to it, you must install the Alexa skill and the Lambda 
function.

These instructions are so bare bones they are more like a check list. This
short tutorial video might help fill in the blanks.
https://www.youtube.com/watch?v=zt9WdE5kR6g 

## Lambda Function Setup
1. Go to https://console.aws.amazon.com and select Lambda.
2. Click "Create a Lambda Function"
3. On the "Select blueprint" page, click "Skip"
4. On the "Configure triggers" page, click the empty box and select "Alexa
Skills Kit"
5. On the "Configure Function" page:
    - Name: pySpiceRack
    - Description: Locates spice
    - Runtime: Python 2.7
    - Handler: lambda_function.lambda_handler
    - Code entry type: Edit code inline
    - Code: Copy in the spicerack.py file
    - Role: Existing role, alexa-dynamodb
6. On the "Review page" click "Create function"
7. Make note of the ARN at the top right.

## Alexa Skill Setup
Go to https://developer.amazon.com/edw/home.html#/skills/list and create a new
skill. Fill in three pages:

### Skill Information
* Skill type: Custom integration model
* Name: Spice Finder
* Invocation name: Spice Finder
* Audio player: No

### Interaction Model
From the speechAssets folder, copy intentSchema.json, 
customSlotTypes/LIST_OF_SPICES.txt, and sampleUtterances.txt into their
respective fields.

### Configuration
1.  Enter the ARN of the lambda function you created before.
2.  Select "North America".

# Latest Version
Found at https://github.com/mikec964/alexa-spicerack 

# Licensing
See the file called LICENSE.
