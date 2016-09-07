/* Spice Rack Locator */
/* Let Alexa help you find the spices you own. */

'use strict';


exports.handler = (event, context) => {

var skillName = 'Spice Rack Locator'
var skillInvoke = 'Spice Rack'

  try{
    if (event.session.new) {
      // New Session
      console.log("NEW SESSION")
    }

    switch (event.request.type) {

      case "LaunchRequest":
        // > Launch Request
        console.log("LAUNCH REQUEST")
        sayThis = "Welcome to " + skillName
        sayThis += "You can ask: '" + skillInvoke + ", where is the cumin?' or any other spices,"
        sayThis += "For more, say 'ask " + skillInvoke + " for help'"
        sayThis += "Would you like to set up your spice rack now?"
        context.succeed(
          generateResponse(
            buildSpeechletResponse(sayThis, true),
            {}
          )
        )
        break;

      case "IntentRequest":
        // > Intent Request
        console.log("INTENT REQUEST")

        switch(event.request.intent.name) {

          case "GetSpiceLocation":
            sayThis = "The spice is on the shelf."
            context.succeed(
              generateResponse(
                buildSpeechletResponse(sayThis, true),
                {}
              )
            )

          case "SetSpiceLocation":
            sayThis = "Okay"
            context.succeed(
              generateResponse(
                buildSpeechletResponse(sayThis, true),
                {}
              )
            )

          case "Help":
            sayThis = "Here are some things you can say:"
            sayThis += "Ask " + invokeName + "for cumin"
            sayThis += "Tell " + invokeName + "The cumin is on row two column three,"
            sayThis += "Once you start organizing you can also say 'the next spice is pepper'"
            context.succeed(
              generateResponse(
                buildSpeechletResponse(sayThis, true),
                {}
              )
            )

        }
          break;

      case "SessionEndedRequest":
        // > Session Ended Request
        console.log("SESSION ENDED REQUEST")
        break;

      default:
        context.fail("INVALID REQUEST TYPE: ${event.request.type}")

    }
  } catch(error) { context.fail("Exception: ${error}") }
}

// Helpers
buildSpeechletResponse = (outputText, shouldEndSession) => {
  return {
    outputSpeech: {
    type: "PlainText",
    text: outputText
    },
    shouldEndSession: shouldEndSession
  }
}

generateResponse = (speechletResponse, sessionAttributes) => {
  return {
    version: "1.0",
    sessionAttributes: sessionAttributes,
    response: speechletResponse
  }
}
