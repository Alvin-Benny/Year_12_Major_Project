import sys, os, datetime, time, pyaudio, wave, sqlite3, speech_recognition, pygame
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QAbstractItemView
from PyQt5.QtCore import QObject, QThread, pyqtSignal
os.chdir('Major Project/voice_recordings')
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    recording = False
    #DECLARING PARAMETERS
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    # 'Frames' is an attribute of the worker object so it is preserved when we pause the recording
    frames = []
    # Transcript is initially set to none incase the module does not recognise any words
    transcript = "None"

    def record(self):
        CHUNK = Worker.CHUNK
        FORMAT = Worker.FORMAT
        CHANNELS = Worker.CHANNELS
        RATE = Worker.RATE
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input = True, frames_per_buffer=CHUNK)
    
        frames = Worker.frames                            
       

        while Worker.recording == True:    
            data = stream.read(CHUNK)
            frames.append(data)
       
        stream.stop_stream()
        stream.close()
        audio.terminate()

        self.finished.emit() # Import for sending signal that thread has finished

    def save (self, rec_name):
        FORMAT = Worker.FORMAT
        CHANNELS = Worker.CHANNELS
        RATE = Worker.RATE
        frames = Worker.frames
        audio = pyaudio.PyAudio()
        sound_file = wave.open(str(rec_name+".wav"), 'wb')
        sound_file.setnchannels(CHANNELS)
        sound_file.setsampwidth(audio.get_sample_size(FORMAT))
        sound_file.setframerate(RATE)
        sound_file.writeframes(b''.join(frames)) #combining binary input to one big string
        sound_file.close()

    def transcribe_audio(self, file_name):
        # We create a new speech recogniser object called reader
        reader = speech_recognition.Recognizer()

        # We get the name/path of the audio from the parameter variable file_name
        # Then with the AudioFile method of the speech recognition software defined as 'source' to easy reference
        # We use the speech recogniser object 'reader' to play through the audio and 'read' the contents of the file
        # Then use a speech recognition API to transcribe the read file
        # This part of the software unfortuately requires an internet connection to operate using Google's API
        # After performing the speech recognition, whatever is in the transcript module is written to a new .txt file created from the file name.
        AUDIO_FILE = str(file_name+".wav")
        with speech_recognition.AudioFile(AUDIO_FILE) as source:
            audio = reader.record(source)
    
        try:
            Worker.transcript = reader.recognize_google(audio)
        except:
            pass
        with open('text_files/'+file_name+'.txt', 'w') as fh:
            fh.write(Worker.transcript)
            fh.close()
        self.finished.emit()

from UI_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.recording = False
        self.recording_path = "None"
        self.main_win.setWindowTitle("The Voice")

       
        current_time = datetime.datetime.now()
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page) #CHANGE
        
        # Automatically updating date box, month box to the current date and month
        # Has to be string
        year = int(current_time.strftime("%Y")) # For the  loop for adding extra years based on current year

        self.ui.date_cbo.setCurrentText(current_time.strftime("%d"))
        self.ui.month_cbo.setCurrentText(current_time.strftime("%b"))

       
        # Generating the indexes of the year selection based on the current date
        year = int(current_time.strftime("%Y"))
        self.ui.year_cbo.addItem(str(year))
        self.ui.db_year_cbo.addItem(str(year)) # For pre-populating the database when the db_screen button is called
        i = 1
        while i < 4:   
            self.ui.year_cbo.addItem(str(year+i))
            self.ui.db_year_cbo.addItem(str(year+i))
            i = i + 1 
        #For prepopulating the database, filtered by year    
        # Starts at 1 because 0 is a blank space
        self.ui.db_year_cbo.setCurrentIndex(1)
        #navigation
        self.ui.home_db_btn.clicked.connect(self.db_screen)
        self.ui.db_back_btn.clicked.connect(self.home_screen)
        self.ui.note_back_btn.clicked.connect(self.text_change)

        # Recording/pause
        self.ui.rec_pause_btn.hide()
        self.ui.rec_btn.clicked.connect(self.record)
        self.ui.rec_pause_btn.clicked.connect(self.stop_record)

        # Saving
        self.ui.home_save_btn.clicked.connect(self.save_record)

        # Deleting the current session
        self.ui.home_delete_btn.clicked.connect(self.rec_delete)

        # Prevents the database table from being edited by the user
        # The function is called for data to be loaded into the table
        self.ui.db_tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.ui.db_search_btn.clicked.connect(self.display_data)

        #Playback module
        self.ui.db_select_btn.clicked.connect(self.load_file)

        self.ui.note_play_btn.clicked.connect(self.play_file)
        self.ui.note_pause_btn.setCheckable(True)
        self.ui.note_pause_btn.clicked.connect(self.pause_file)

        # delete module
        self.ui.db_delete_btn.clicked.connect(self.saved_delete)
        self.ui.note_delete_btn.clicked.connect(self.saved_delete)

        # Results updating dynamically without the search button
        self.ui.db_date_cbo.currentIndexChanged.connect(self.display_data)
        self.ui.db_month_cbo.currentIndexChanged.connect(self.display_data)
        self.ui.db_year_cbo.currentIndexChanged.connect(self.display_data)
        self.ui.db_search_txt.textChanged.connect(self.display_data)

    def show(self):
	    self.main_win.show()
    
    def db_screen(self):
        self.display_data() # Automatically populates database queried for current 'year' when user clicks to see the db screen
        self.ui.stackedWidget.setCurrentWidget(self.ui.db_page)
        # If the user exits the 'note' screen then the audio file is automatically stopped.
        try:
            pygame.mixer.music.unload()
        except:
            pass
        
    def home_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    # recording functionality
    # We had to create a worker class above the mainwindow code to define the code that runs concurrently with the interface code.
    # A QThread is used to run multiple python functions at once without freezing the entire program.
    # So the QThread object in our case connects with the modules of the worker class and calls the 'record' module.
    
    def record(self):
        self.ui.home_title_lbl.setText("Record a new note") #Incase user had previous invalid recording name
        self.ui.home_title_lbl.setStyleSheet("color: black")
        Worker.recording = True
        self.ui.rec_btn.hide()
        self.ui.rec_pause_btn.show()
        self.ui.home_delete_btn.setEnabled(False)
        self.ui.home_save_btn.setEnabled(False)
        self.ui.home_db_btn.setEnabled(False)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.record)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        
        self.thread.start()
        #Disable the button while the thread is running.
        # Renable when it is finished
        # This is done so the program does not crash if the button is recording button is spammed
        time.sleep(0.3) # So recording does not get cut off at beginning if user talks too quickly.
        self.ui.rec_btn.setEnabled(False)
        self.thread.finished.connect(lambda: self.ui.rec_btn.setEnabled(True))
        
    
    # Here we are setting the recording attribute of the worker class to False so the recording stops.
    # This is done in a 2 button setup because using the original record button to call another function while the QThread is happening
    # crashes the program because the QThread is abruptly forced to stop without receiving the 'finished' signal.
    def stop_record(self):
        time.sleep(0.5) # So the recording doesn't get abruptly cut off at the end
        Worker.recording = False
        self.ui.rec_btn.show()
        self.ui.rec_pause_btn.hide()
        self.ui.home_delete_btn.setEnabled(True)
        self.ui.home_save_btn.setEnabled(True)
        self.ui.home_db_btn.setEnabled(True)
   
    # Should be only able to save after pausing and when the subject text is alphanumeric without special characters.
    # Resets the 'frames' to nothing so previous takes are not included in newly saved files.
    # Set the recording button to be disabled so it is not clicked while the text file is being transcripted
    # Gets the parameters selected by the user on the recording screen and uses it to construct a file name
    def save_record(self):
        if Worker.recording == False and Worker.frames != [] and self.ui.subject_txt.text().isalnum():

            #So program doesn't crash if button is spammed
            self.ui.home_save_btn.setEnabled(False) 
            self.ui.home_db_btn.setEnabled(False)
            self.ui.home_delete_btn.setEnabled(False)

            current_time = datetime.datetime.now()
            
            rec_subject = self.ui.subject_txt.text()
            rec_date = self.ui.date_cbo.currentText()
            rec_month = self.ui.month_cbo.currentText()
            rec_year = self.ui.year_cbo.currentText()
            rec_time = current_time.strftime("%H;%M") # Provides time in 24 hour format. Had to use fullstop due to reserved characters in Windows
            rec_name = rec_subject+"_"+rec_date+"-"+rec_month+"-"+rec_year+"_"+rec_time
         
            Worker.save(self, rec_name)
            Worker.frames = []
            Worker.file_name = rec_name

            # Code for finished message pre-declared up here
            def finished_confirmation():
                yes_saved = QMessageBox()
                yes_saved.setIcon(QMessageBox.Information)
                yes_saved.setText("Your recording has been saved!")
                yes_saved.setWindowTitle("Confirmation")
                yes_saved.exec()

            # Another subthread from the main thread is required so the main interference does not freeze whilst calculating the transcription
            self.thread = QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(lambda: self.worker.transcribe_audio(rec_name))
            self.worker.finished.connect(lambda: self.ui.home_save_btn.setEnabled(True))
            self.worker.finished.connect(lambda: self.ui.home_db_btn.setEnabled(True))
            self.worker.finished.connect(lambda: self.ui.home_delete_btn.setEnabled(True))
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.finished.connect(finished_confirmation)
            self.thread.start()

            conn = sqlite3.connect("recordings.db") 
            c = conn.cursor()

            # Creating a SQlite database in the code itself so a pre-formatted db file is not required.
            # Using a try and except incase the file already exists and the code runs into an error
            try:
                c.execute("""CREATE table recordings (
                    subject text, 
                    date integer,
                    month text,
                    year integer,
                    time text
                )""")
            except: 
                pass

            c.execute ("INSERT INTO recordings VALUES (:subject, :date, :month, :year, :current_time)", 
                {'subject': rec_subject, 'date': rec_date, "month": rec_month, 'year': rec_year, 'current_time': rec_time})

            conn.commit()

        elif self.ui.subject_txt.text().isalnum() == False:
            no_saved = QMessageBox()
            no_saved.setIcon(QMessageBox.Warning)
            no_saved.setText("Please ensure subject text only contains alphaneumeric characters i.e., ABC123")
            no_saved.setWindowTitle("Save Error")
            no_saved.exec()


    # Function for loading the database items into the UI QtTableWidget
    # First the variables take any set parameters in the drop down box
    # Next a selection is made from the database using the required parameters in a sequential order
    # it is done in this manner so the selection is continuously filtered based on what parameters are available
    # Available parameters are ones where the drop down list is not empty    
    def display_data(self):
            chosen_subject = self.ui.db_search_txt.text()
            chosen_date = self.ui.db_date_cbo.currentText()
            chosen_month = self.ui.db_month_cbo.currentText()
            chosen_year = self.ui.db_year_cbo.currentText()
            results = []
        
            conn = sqlite3.connect("recordings.db")
            c = conn.cursor()
                        
            if chosen_year != "":
                c.execute("SELECT * FROM recordings WHERE year = :year ORDER by date, month, year", {'year': chosen_year})
            
            if chosen_month !="":
                c.execute("SELECT * FROM recordings WHERE month = :month ORDER by date, month, year", {'month': chosen_month})

            if chosen_date !="":
                c.execute("SELECT * FROM recordings WHERE date = :date ORDER by date, month, year", {'date': chosen_date})
            
            if chosen_subject!="":
                c.execute("SELECT * FROM recordings WHERE subject = :subject ORDER by date, month, year", {'subject': chosen_subject})
            
            conn.commit()
            results = c.fetchall()

            self.ui.db_tbl_widget.setRowCount(len(results))
            row = 0
            # So for each item in the 'results' array of records
            # Add a sub-item of that item sequentially
            # Columns are hard coded as '0, 1, 2...' because they're definite
            for info in results:
                self.ui.db_tbl_widget.setItem(row, 0, QTableWidgetItem(str(info[0])))
                self.ui.db_tbl_widget.setItem(row, 1, QTableWidgetItem(str(info[1])))
                self.ui.db_tbl_widget.setItem(row, 2, QTableWidgetItem(str(info[2])))
                self.ui.db_tbl_widget.setItem(row, 3, QTableWidgetItem(str(info[3])))
                self.ui.db_tbl_widget.setItem(row, 4, QTableWidgetItem(str(info[4])))
                row = row + 1

    
    def load_file(self):
        # Function for recording the currently selected row and using it to retrieve information
        # This information is used to create a file path using the same format of the recording module
        # recording_path is a global variable so it can be used by the playback module
        try:
            row = self.ui.db_tbl_widget.currentRow()
            subject = self.ui.db_tbl_widget.item(row, 0).text()
            date = self.ui.db_tbl_widget.item(row, 1).text()
            month = self.ui.db_tbl_widget.item(row, 2).text()
            year = self.ui.db_tbl_widget.item(row, 3).text()
            time = self.ui.db_tbl_widget.item(row, 4).text()
            
            self.recording_path = subject+"_"+date+"-"+month+"-"+year+"_"+time
        
            
            if os.path.exists(self.recording_path+".wav") == True:
                #For if the user exists previously while recording was paused.
                self.ui.note_pause_btn.setChecked(False)
                self.ui.name_of_file_lbl.setText(subject+"-"+date+"-"+month+"-"+year) 
                
                # Open the text file using the constructed file name from of the selected row
                # Encoding is set to uf-8-sig when reading because or else â€™ appears at the end of some sentences
                # I think it's because of some encoding issue so we use utf-8 for most common standard.
                try:
                    with open('text_files/'+self.recording_path+".txt", 'r', encoding = 'utf-8-sig') as fh:
                        transcript = fh.read()
                        self.ui.trans_txt.setText(transcript)
                        fh.close()
                except:
                    self.ui.trans_txt.setText("None")

                self.ui.stackedWidget.setCurrentWidget(self.ui.note_page)
            else:
                self.saved_delete()
        except:
            no_select = QMessageBox()
            no_select.setIcon(QMessageBox.Warning)
            no_select.setText("Please ensure you have selected a row")
            no_select.setWindowTitle("Selection error")
            no_select.exec()
    
    # A dedicated button to initialise the music player and play the sound
    # Checks whether file exists before playing
    # if not the file is deleted
    def play_file(self):
            path = self.recording_path+".wav"
            if os.path.exists(path) == True:
                self.ui.note_pause_btn.setChecked(False)

                pygame.mixer.init()
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()

    # Dedicated pause button to check if it has been toggled to pause and unpause the audio file.

    def pause_file(self):
        if self.ui.note_pause_btn.isChecked() == True:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    

    def saved_delete(self):
        # The delete function uses the information stored in the selected row to delete the entry
        # The selected row is stored even when the stackedwidget changes screen hence this is possible
        # Current row returns -1 if no row is selected
        # Extract the data from the database viewer (table widget) and use it to provide paramaters for the SQL delete query
        # It also calls the 'file_delete' function to delete the file from the recordings folder.
        if self.ui.db_tbl_widget.currentRow() > -1:
            confirmation = QMessageBox()
            confirmation.setIcon(QMessageBox.Warning)
            confirmation.setText("Are you sure you want to delete this recording?")
            confirmation.setWindowTitle("Confirm Delete")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            answer = confirmation.exec()

            if answer == QMessageBox.Yes:
                row = self.ui.db_tbl_widget.currentRow()
                subject = self.ui.db_tbl_widget.item(row, 0).text()
                date = self.ui.db_tbl_widget.item(row, 1).text()
                month = self.ui.db_tbl_widget.item(row, 2).text()
                year = self.ui.db_tbl_widget.item(row, 3).text()
                time = self.ui.db_tbl_widget.item(row, 4).text()

                self.recording_path = subject+"_"+date+"-"+month+"-"+year+"_"+time

                conn = sqlite3.connect("recordings.db") 
                c = conn.cursor()
                c.execute("DELETE from recordings where subject = :subject AND date = :date AND month = :month AND year = :year AND time = :time",
                {'subject': subject, 'date': date, 'month': month, 'year': year, 'time': time})
                
                # Try and except here just incase the audio playback module wasn't initialised
                try:
                    pygame.mixer.music.unload()
                except:
                    pass
                self.ui.stackedWidget.setCurrentWidget(self.ui.db_page)
                self.file_delete()

                conn.commit()
                self.display_data()


    def file_delete(self):
        # Here we are removing any currently loaded file in the pygame music player in order to delete
        self.ui.stackedWidget.setCurrentWidget(self.ui.db_page)
        try:
            os.remove(self.recording_path+".wav")
        except:
            pass

        try:
            os.remove('text_files/'+self.recording_path+".txt")
        except:
            pass

    def text_change(self):
        # When the user exists the note viewing screen, any changes to the transcripted text is saved into its file
        try:
            with open('text_files/'+self.recording_path+".txt", 'w') as fh:
                    fh.truncate(0) #Deletes everything currently in the file
                    fh.write(self.ui.trans_txt.toPlainText())
                    fh.close()
        except:
            pass
        self.ui.stackedWidget.setCurrentWidget(self.ui.db_page)

    # User should be only able to delete recording session if the recording button is paused
    def rec_delete(self):
        if Worker.recording == False:
            Worker.frames = []
            session_delete = QMessageBox()
            session_delete.setIcon(QMessageBox.Information)
            session_delete.setWindowTitle("Session clear")
            session_delete.setText("Current session cleared")
            session_delete.exec()
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

