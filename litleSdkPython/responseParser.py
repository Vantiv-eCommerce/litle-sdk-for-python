import io


class ResponseParser:
    def __init__(self, responseFile):
        self.responseFile = responseFile
        self.reader = io.open(responseFile, 'r')

    def getNextTag(self, tagToLookFor):
        currentStartingTagInFile = ''
        retString = ''
        currentEndingTagInFile = ''

        startRecordingStartingTag = False
        startRecordingEndingTag = False
        startRecordingRetString = False

        lastChar = ' '

        openingTagToLookFor = '<' + tagToLookFor
        closingTagToLookFor = '</' + tagToLookFor + '>'

        ch = ' '
        while ch != '':
            ch = self.reader.read(1)
            if startRecordingRetString:
                retString += ch

                if lastChar == '<' and ch == '/':
                    startRecordingEndingTag = True
                    currentEndingTagInFile += lastChar

                if (tagToLookFor.lower() == 'batchresponse'or
                    tagToLookFor.lower() == 'litleresponse') and ch == '>':
                    retString += closingTagToLookFor
                    break

            if ch == '<' and not startRecordingRetString:
                startRecordingStartingTag = True

            if startRecordingStartingTag:
                currentStartingTagInFile += ch

                if self.okToStartRecordingString(openingTagToLookFor, currentStartingTagInFile):
                    startRecordingRetString = True
                    retString += currentStartingTagInFile
                    startRecordingStartingTag = False
                    currentStartingTagInFile = ''

                if ch == '>':
                    if tagToLookFor.lower() == 'transactionresponse' and \
                        currentStartingTagInFile.lower() == '</batchresponse>':
                        raise Exception("All payments in this batch have already been retrieved.")
                    startRecordingStartingTag = False
                    currentStartingTagInFile = ''

            if startRecordingEndingTag:
                currentEndingTagInFile += ch
                if ch == '>':
                    startRecordingEndingTag = False
                    if self.okToStopRecordingString(closingTagToLookFor, currentEndingTagInFile):
                        startRecordingRetString = False
                        break
                    currentEndingTagInFile = ''
            lastChar = ch
        return retString

    def okToStartRecordingString(self, openingTagToLookFor, currentStartingTagInFile):
        retVal = False

        if openingTagToLookFor.lower() == '<transactionresponse' and \
            (currentStartingTagInFile.lower() == '<authorizationResponse'.lower() or
            currentStartingTagInFile.lower() == '<saleResponse'.lower() or
            currentStartingTagInFile.lower() == '<captureResponse'.lower() or
            currentStartingTagInFile.lower() == '<forceCaptureResponse'.lower() or
            currentStartingTagInFile.lower() == '<captureGivenAuthResponse'.lower() or
            currentStartingTagInFile.lower() == '<creditResponse'.lower() or
            currentStartingTagInFile.lower() == '<echeckSalesResponse'.lower() or
            currentStartingTagInFile.lower() == '<echeckCreditResponse'.lower() or
            currentStartingTagInFile.lower() == '<echeckVerificationResponse'.lower() or
            currentStartingTagInFile.lower() == '<echeckRedepositResponse'.lower() or
            currentStartingTagInFile.lower() == '<authReversalResponse'.lower() or
            currentStartingTagInFile.lower() == '<registerTokenResponse'.lower() or
            currentStartingTagInFile.lower() == '<updateSubscriptionResponse'.lower() or
            currentStartingTagInFile.lower() == '<cancelSubscriptionResponse'.lower() or
            currentStartingTagInFile.lower() == '<updateCardValidationNumOnTokenResponse'.lower() or
            currentStartingTagInFile.lower() == '<updatePlanResponse'.lower() or
            currentStartingTagInFile.lower() == '<createPlanResponse'.lower() or
            currentStartingTagInFile.lower() == '<activateResponse'.lower() or
            currentStartingTagInFile.lower() == '<deactivateResponse'.lower() or
            currentStartingTagInFile.lower() == '<loadResponse'.lower() or
            currentStartingTagInFile.lower() == '<unloadResponse'.lower() or
            currentStartingTagInFile.lower() == '<balanceInquiryResponse'.lower() or
            currentStartingTagInFile.lower() == '<accountUpdateResponse'.lower()):
            retVal = True

        elif openingTagToLookFor.lower() == currentStartingTagInFile.lower():
            retVal = True
        return retVal


    def okToStopRecordingString(self, closingTagToLookFor, currentStartingTagInFile):
        retVal = False

        if closingTagToLookFor.lower() == '</transactionresponse>' and \
            (currentStartingTagInFile.lower() == '</authorizationResponse>'.lower() or
            currentStartingTagInFile.lower() == '</saleResponse>'.lower() or
            currentStartingTagInFile.lower() == '</captureResponse>'.lower() or
            currentStartingTagInFile.lower() == '</forceCaptureResponse>'.lower() or
            currentStartingTagInFile.lower() == '</captureGivenAuthResponse>'.lower() or
            currentStartingTagInFile.lower() == '</creditResponse>'.lower() or
            currentStartingTagInFile.lower() == '</echeckSalesResponse>'.lower() or
            currentStartingTagInFile.lower() == '</echeckCreditResponse>'.lower() or
            currentStartingTagInFile.lower() == '</echeckVerificationResponse>'.lower() or
            currentStartingTagInFile.lower() == '</echeckRedepositResponse>'.lower() or
            currentStartingTagInFile.lower() == '</authReversalResponse>'.lower() or
            currentStartingTagInFile.lower() == '</registerTokenResponse>'.lower() or
            currentStartingTagInFile.lower() == '</updateSubscriptionResponse>'.lower() or
            currentStartingTagInFile.lower() == '</cancelSubscriptionResponse>'.lower() or
            currentStartingTagInFile.lower() == '</updateCardValidationNumOnTokenResponse>'.lower() or
            currentStartingTagInFile.lower() == '</updatePlanResponse>'.lower() or
            currentStartingTagInFile.lower() == '</createPlanResponse>'.lower() or
            currentStartingTagInFile.lower() == '</activateResponse>'.lower() or
            currentStartingTagInFile.lower() == '</deactivateResponse>'.lower() or
            currentStartingTagInFile.lower() == '</loadResponse>'.lower() or
            currentStartingTagInFile.lower() == '</unloadResponse>'.lower() or
            currentStartingTagInFile.lower() == '</balanceInquiryResponse>'.lower() or
            currentStartingTagInFile.lower() == '</accountUpdateResponse>'.lower()):
            retVal = True

        elif closingTagToLookFor.lower() == currentStartingTagInFile.lower():
            retVal = True
        return retVal