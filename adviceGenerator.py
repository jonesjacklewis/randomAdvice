def getResponse(u):
    """
    param:
        u: 
            URL to get
    returns:
        r.content:
            Content of requested URL


    """
    import requests  #  Imports request module

    r = requests.get(u)  #  Store value of requests.get in r

    return r.content  #  Return content of the URL



def convertToJson(data):
    """"
    param:
        data:
            Data to be converted to JSON
    returns:
        jsonData:
            JSON fomat of the data
    """

    import json #  Import JSON module

    decodedData = data.decode("utf8")  #  Decode from utf-8

    jsonData = json.loads(decodedData)  #  Load in as JSON

    return jsonData  #  Return the jsonData


def getAdvice(jsonData): 
    """
    param:
        jsonData:
            Some JSON data to extract advice from
    returns:
        advice:
            some advice
    
    """

    import json  #  Import JSON module

    slipInfo = jsonData.get("slip")  #  Extract the 'slip' tag 
    advice = slipInfo.get("advice")  #  Extract the 'advice' tag

    return advice  #  Return the advice


def adviceGettter():
    """
    param:
        None
    returns:
        advice:
            some advice
    
    """

    url = "https://api.adviceslip.com/advice"  #  end point URL


    responseData = getResponse(url)  #  Get the content of a request to the endpoint
    jsonResponse = convertToJson(responseData)  #  Convert endpoint response to JSON

    advice = getAdvice(jsonResponse)  #  Get the advice field

    return advice  #  Return the advice

def censorText(text):
    """
    param:
        tex:
            Text to be censored

    returns:
        jsonData.get("result"):
            The section of json under result tag

    """
    import json # import JSON module

    url = "https://www.purgomalum.com/service/json?text=" + text  #  endpoint url

    binaryData = getResponse(url)  #  get the request from endpoint

    jsonData = convertToJson(binaryData)  #  convert response to JSON

    return jsonData.get("result")  # get the censored text

def mainMenu():
    """
    param:
        None
    Returns:
        None
    """
    import PySimpleGUI as sg  #  import PySimpleGUI with the alias sg

    layout  = [
        [sg.Text("Get some Random Advice")],
        [sg.Text(" " * 256, key="quote")],
        [sg.Button("Get Advice")]
    ]  #  Layout of text on top row, text with quote on middle row and button on bottom

    window = sg.Window("Random Advice", layout, element_justification = 'c')  #  Windows with title "Random Advice" using predifned layout and centred justification

    while True:  #  until quit
        event, values = window.read()  #  Read events and values

        if event == sg.WIN_CLOSED:  #  if the user clicks the X arrow
            break  #  break out of loop
        if event == "Get Advice":
            newQuote = adviceGettter()  #  Get some advice 
            censoredQuote = censorText(newQuote)  #  Censor advice
            window.Element("quote").Update(censoredQuote)  #  Update text field with censored quote
    window.close()  #  Close window


mainMenu()
