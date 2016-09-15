#!/usr/bin/env python

# Spice Rack Locator
# Let Alexa help you find the spices you own.

from __future__ import print_function
import json
import boto3

APP_ID = "amzn1.ask.skill.55ae683e-0f28-442f-b1e3-175ef28b5ecb" # Set APP_ID to ensure only your skill calls this lambda handler
SKILL_NAME = "Spice Rack Locator"
SKILL_INVOKE = "Spice Rack"
DB_TABLENAME = "spicerack-map"
DB_REGION = "us-west-1"


def lambda_handler(event, context):
    """ Returns a JSON response to Alexa with: outputSpeech, reprompt, card, shouldEndSession """

    if (event["session"]["application"]["applicationId"] != 'amzn1.echo-sdk-ams.app.[unique-value-here]'):
        if (APP_ID != ""):
            if (event["session"]["application"]["applicationId"] != APP_ID):
                raise ValueError("Invalid Application ID", event["session"]["application"]["applicationId"],APP_ID)

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


def on_session_started(session_started_request, session):
    return

def on_session_ended(session_ended_request, session):
    return


def on_launch(launch_request, session):
    """ Skill launched with no or Help intent """
    return launch_response()


def on_intent(intent_request, session):
    """ Skill launched with intent. Get intent from JSON and call appropriate function """

    print("Determining intent.")
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "GetSpiceLocation":
        return get_spice_location(intent)
    elif intent_name == "SetSpiceLocation":
        return set_spice_location(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_launch_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Unsupported intent")


def launch_response():
    """ No intent. Provide help."""

    session_attributes = {}
    card_title = SKILL_NAME
    speech_output = "Welcome to " + SKILL_NAME + ". \n" \
                    "Try: Tell " + SKILL_INVOKE + " the cumin is on row 2, column 4. " \
                    "Or try: Ask " + SKILL_INVOKE + " for the cumin."
    reprompt_text = "Tell me where the first bottle is."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_spice_location(intent):
    session_attributes = {}
    card_title = "" # no card
    speech_output = ""
    reprompt_text = ""
    should_end_session = True

    if "spice" in intent["slots"]:
        spice_name = intent["slots"]["spice"]["value"]
        speech_output = "The " + spice_name + " is on the shelf."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def set_spice_location(intent):
    session_attributes = {}
    card_title = "" # no card
    speech_output = ""
    reprompt_text = ""
    should_end_session = True

    spice_name = ""
    row = 0
    column = 0
    if "spice" in intent["slots"]:
        spice_name = intent["slots"]["spice"]["value"]
    if "row" in intent["slots"]:
        row = intent["slots"]["row"]["value"]
    if "column" in intent["slots"]:
        column = intent["slots"]["column"]["value"]
    if spice_name != "" and row != 0 and column != 0:
        speech_output = "The " + spice_name + " is on row " + row + ", column " + column + ". "

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    """ Requested Cancel or Stop """

    card_title = "" # no card
    speech_output = "Thanks for using " + SKILL_NAME + "."
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def get_table():
    """ Create table if it doesn't exist """

    client = boto3.client('dynamodb')
    try:
        response = client.describe_table(TableName = DB_TABLENAME)
        # parsed = json.loads(response)
        # print(json.dumps(parsed, indent=4, sort_keys=True))
        # print(response)
    except Exception, e:
        print(e)
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.create_table(
            TableName = DB_TABLENAME,
            KeySchema=[
                { "AttributeName": "spiceName", "KeyType": "HASH" },
            ],
            AttributeDefinitions = [
                { "AttributeName": "spiceName", "AttributeType": "S" },
            ],
            ProvisionedThroughput = {
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=DB_TABLENAME) # Might take 20 seconds locally!

def store_spice(spiceName, spiceLocation, spiceRow, spiceColumn):
    """ Store spice location in db """

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DB_TABLENAME)
    try:
        response = dynamodb.describeTable(DB_TABLENAME)
        print (response)
    except Exception, e:
        table.put_item(
            Item = {
                "spiceName": spiceName,
                "spiceLocation": spiceLocation,
                "spiceRow": spiceRow,
                "spiceColumn": spiceColumn,
            }
        )


def recall_spice(spiceName):
    """ Recall spice location from db """

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DB_TABLENAME)
    response = table.get_item(
        Key = {
            'spiceName': spiceName
        }
    )
    try:
        item = response['Item']
    except Exception, e:
        raise


def build_speechlet_response(title, output, reprompt_text, should_end_session):

    if title == "":
        return {
            "outputSpeech": {
                "type": "PlainText",
                "text": output
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": reprompt_text
                }
            },
            "shouldEndSession": should_end_session
        }
    else:
        return {
            "outputSpeech": {
                "type": "PlainText",
                "text": output
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": reprompt_text
                }
            },
            "shouldEndSession": should_end_session,
            "card": {
                "type": "Simple",
                "title": title,
                "content": output
            }
        }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
