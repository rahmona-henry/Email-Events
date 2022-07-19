filtered_events = []
filtered_offset = ""
filtered_hasMore = True

while filtered_hasMore == True:
    filtered_response = requests.get(f'https://api.hubspot.com/email/public/v1/events?limit=1000&campaignId=189798110&eventType=OPEN&portalId=6377009&offset={filtered_offset}&excludeFilteredEvents=True',auth=HubSpotAuth())
    filtered_parsed_response = filtered_response.json()
    filtered_events.extend(filtered_parsed_response["events"])

    filtered_offset = filtered_parsed_response["offset"]
    filtered_hasMore = filtered_parsed_response["hasMore"]

# filtered_events = [event for event in raw_events["events"] if (event["appName"] == "Batch" or event["appName"] =="Workflow") and event["type"]=="OPEN"]

filtered_unique_recipient = {event["recipient"] + ";" + str(event["emailCampaignId"]):event for event in filtered_events}



filtered_data_frame = pd.DataFrame(filtered_unique_recipient.values())
