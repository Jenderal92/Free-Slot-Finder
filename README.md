# Free Slot Finder  

![Free-Slot-Finder](https://github.com/user-attachments/assets/4b2b20e4-b0de-4c5c-a5e7-665c3c44314b)


**Free Slot Finder** helps users find free time slots in their busy schedules by analyzing their Google Calendar events. It is especially useful for individuals managing tight schedules, allowing them to efficiently plan meetings, tasks, or personal activities.  

---

## **Features**  
- **Automated Slot Detection**: Scans Google Calendar for busy time slots and calculates the free periods.  
- **Customizable Date Range**: Users can specify the start and end dates for the search.  
- **Work Hour Support**: Can be customized to avoid non-working hours.  
- **Ease of Use**: Fully automated process with minimal setup requirements.  

---

## **How to Use**  
### Prerequisites  
1. **Google Calendar API Setup**:  
   - Go to [Google Cloud Console](https://console.cloud.google.com/).  
   - Create a new project.  
   - Enable the **Google Calendar API** for the project.  
   - Download the `credentials.json` file and place it in the project directory.  

2. **Install Dependencies**:  
   Install the required Python libraries:  
   ```bash  
   pip install --upgrade google-api-python-client oauth2client  
   ```  

### Running the Tool  
1. Clone or download the `free_slot_finder.py` file to your local directory.  
2. Ensure the `credentials.json` file is in the same directory.  
3. Run the tool using Python 2.7:  
   ```bash  
   python free_slot_finder.py  
   ```  
4. Input the desired date range in the format `YYYY-MM-DD`.  
5. The tool will analyze your calendar and display the free time slots.  

---

## **Tool Functions**  
1. **Authenticate Google Calendar**:  
   - Uses OAuth 2.0 to securely connect to your Google Calendar account.  

2. **Analyze Calendar Events**:  
   - Reads all events in the specified date range to identify busy periods.  

3. **Calculate Free Slots**:  
   - Compares busy slots with the specified date range to determine available time.  

4. **Output Results**:  
   - Displays both busy and free slots in a user-friendly format.  

---

## **Sample Output**  
```plaintext  
##############################################  
#        FREE SLOT FINDER - PROFESSIONAL     #  
#            Google Calendar Tool            #  
##############################################  

Enter start date (YYYY-MM-DD): 2024-12-23  
Enter end date (YYYY-MM-DD): 2024-12-25  

[INFO] Searching for free slots...  

[INFO] Busy Slots Found:  
- 2024-12-23T10:00:00 to 2024-12-23T11:00:00  
- 2024-12-24T14:00:00 to 2024-12-24T15:00:00  

[INFO] Free Slots:  
- 2024-12-23T11:00:00 to 2024-12-24T14:00:00  
- 2024-12-24T15:00:00 to 2024-12-25T00:00:00  
```  

---
