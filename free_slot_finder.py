from __future__ import print_function
import datetime
import os
import sys
from googleapiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import argparser, run_flow


def print_banner():
	print("""
=====================================================
        FREE SLOT FINDER   
        Google Calendar Tool 
=====================================================
    """)

def authenticate_google_calendar():
    creds_file = 'credentials.json'
    token_file = 'token.json'

    flow = flow_from_clientsecrets(creds_file, scope='https://www.googleapis.com/auth/calendar.readonly')
    storage = Storage(token_file)
    credentials = storage.get()

    if not credentials or credentials.invalid:
        flags = argparser.parse_args(args=[])
        credentials = run_flow(flow, storage, flags)

    service = build('calendar', 'v3', credentials=credentials)
    return service

def find_free_slots(service, start_date, end_date):
    print("\n[INFO] Searching for free slots...")
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_date.isoformat() + 'Z',
        timeMax=end_date.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print("No events found. Your calendar is free!")
        return

    print("\n[INFO] Busy Slots Found:")
    busy_times = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print("- {} to {}".format(start, end))
        busy_times.append((start, end))

    print("\n[INFO] Calculating free slots...")
    calculate_free_slots(busy_times, start_date, end_date)

def calculate_free_slots(busy_times, start_date, end_date):
    free_slots = []
    current_time = start_date

    for start, end in busy_times:
        start_dt = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%fZ')
        if current_time < start_dt:
            free_slots.append((current_time, start_dt))
        current_time = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S.%fZ')

    if current_time < end_date:
        free_slots.append((current_time, end_date))

    print("\n[INFO] Free Slots:")
    for free_start, free_end in free_slots:
        print("- {} to {}".format(free_start, free_end))

def main():
    print_banner()
    service = authenticate_google_calendar()

    try:
        start_date = datetime.datetime.strptime(raw_input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
        end_date = datetime.datetime.strptime(raw_input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
    except ValueError:
        print("[ERROR] Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)
    find_free_slots(service, start_date, end_date)

if __name__ == '__main__':
    main()
