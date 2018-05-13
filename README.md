# Bailiff
Bailiff is a script that checks the EC2 Instances of an AWS tenant. It verifies the enforcing of several rules, and then posts a message on our Slack. 

While I scripted this to be generic, the implemented rules here may be specific to our team, so feel free to fork and modify it to suit your needs.

## Motivation
We have a free access to the AWS tenant of our team, at least for the EC2 part. Which means anyone in the team can create an instance, in any region. With the team size increasing, our rules were sometimes forgotten : 
 - Your instance must have a name
 - This name must start with your identifier in the company (a trigram or quadrigram)
 - You must stop your instance if you do not use it
 - You must delete your instance if you do not plan to use it anymore

I used to check these by myself before, but now that we're approaching 40 people it becomes uneffective. I found several long-running forgotten instances in weird regions (which we could forbid though), people do not name their instances, etc. Therefore, I decided to script these operations and publish the result on our Slack, to make people more accountable.

I chose the name because it makes me think of the Bailiff, who comes and says "you owe us something, man" ahah.

## Screenshots
![Screenshot of Slack](/../screenshots/assets/capture.png?raw=true)

## Tech
All of this is scripted in Python 3, with the main libraries being `boto3`, `pytest`, `slackclient`, and the awesome `tabulate` which spared me few hours.

## Features
The script grabs all the instances in the specified regions, and then computes some information on these:
- Name
- Trigram or quadrigram if exists
- Launch date
- Last action date (if exists, otherwise it is the launch date)
- Region (obviously)

Based on this information, it classifies the instances in different categories according to which rules they follow correctly. Then it prints this in sweet nice tables in a Slack channel.

Everything is configurable through environment vars (cloud native, mate!):
- Credentials for AWS
- Credential for Slack
- Threshold for inactivity

### Askbob
Askbob is our internal people reference. It exposes an API that bailiff uses to gather the emails of people based on their trigram. Therefore, we will be able in a near future to link this with the slack users, and ping them with direct notification hopefully.
This part of the code is not linked to the execution right now, but already well-covered with tests. We may get some more soon once I have made a choice for mocking/patching with pytest. Stay tuned.
I will make this feature flippable, so you can easily use the project without it.

## Tests
I tested what could be tested, so mainly the logic and not the printing stuff. All done with PyTest : `python -m pytest tests/` to run the tests, or `pytest` if you have the current dir in your python path.

## How to use?
### As a dev
I built this as a script and not a library. I do not plan on making it a library, as I feel it does not have a real meaning. If you want to start from it, `git clone`.

### As a user
Everything you need to deploy on your tenant is in the `deploy/` directory. More to come on this topic.

## Contribute
Feel free to fork and contribute, that would be an awesome reward!


