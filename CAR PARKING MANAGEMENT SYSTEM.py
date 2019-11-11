''' Parking Management System Construction Underway'''
###################################################
from tkinter import *
##################################################
startscreen=Tk()
startscreen.title("Welcome!")
def YesWE():
    FirstScreen = Toplevel()
    FirstScreen.title("Please Fill Out The Entries Below To Book A Parking Slot!")
    ###################
    """Size of city screen image = 720x200 px"""
    WelcomePic = PhotoImage(file="Photos\CITYWALLPAPERLOWERTOOLBAR.png")
    WelcomePicPlacement = Label(FirstScreen, image=WelcomePic)
    WelcomePicPlacement.pack(side="top", fill="both")
    ######################
    """Drop Drop Menus On The Top Of The Screen"""
    #######################
    DropDownMenuToShowcase = Menu(FirstScreen)
    FirstScreen.configure(menu=DropDownMenuToShowcase)

    WhatWeDo = Menu(DropDownMenuToShowcase)
    DropDownMenuToShowcase.add_cascade(label="What We Do", menu=WhatWeDo)
    WhatWeDo.add_command(label="Reservations For Hotel Parking")
    WhatWeDo.add_command(label="Reservations For Clubs")
    WhatWeDo.add_command(label="Reservations For Events")
    WhatWeDo.add_command(label="Reservations For Institutions ")
    WhatWeDo.add_command(label="Reservations For Workplaces")

    WhatCanYouExpect = Menu(DropDownMenuToShowcase)
    DropDownMenuToShowcase.add_cascade(label="What Can You Expect From Us?", menu=WhatCanYouExpect)
    WhatCanYouExpect.add_command(label="Implementation Of Our High-Class Management System")
    WhatCanYouExpect.add_command(label="Valet Service For VIP Guests")
    WhatCanYouExpect.add_command(label="Hassle-Free Ticket System")
    WhatCanYouExpect.add_command(label="Congestion-Free Systematic Parking")

    CurrentTieUps = Menu(DropDownMenuToShowcase)
    DropDownMenuToShowcase.add_cascade(label="Where Are Our Current Tie-Ups?", menu=CurrentTieUps)
    CurrentTieUps.add_command(label="Sun And Sands Hotel")
    CurrentTieUps.add_command(label="Parkinson Hotel")
    CurrentTieUps.add_command(label="Microsoft HQ")
    CurrentTieUps.add_command(label="Army Public School")

    ###########################################################
    """Triple Image Below CityScape Pic"""
    ###########################################################
    canvas = Canvas(FirstScreen, width=720, height=400)
    canvas.pack()

    PhotoOffice = PhotoImage(
        file="Photos\wvu medicine corporate officePNG.png")
    PhotoOfficePlacement = Label(canvas, image=PhotoOffice)
    PhotoOfficePlacement.pack(side=LEFT)
    CarInfrontOfHotel = PhotoImage(
        file="Photos\gaudy-car-parked-in-front-of-hotelPNG.png")
    CarInfrontOfHotelPlacement = Label(canvas, image=CarInfrontOfHotel)
    CarInfrontOfHotelPlacement.pack(side=LEFT)
    CarClub = PhotoImage(file="Photos\CarClubPNG.png")
    CarClubPlacement = Label(canvas, image=CarClub)
    CarClubPlacement.pack(side=LEFT)

    #############################
    """Entry Form Below"""
    #############################


    EntryForm = Frame(FirstScreen)

    VariableForDestination = StringVar()
    VariableForCars = StringVar()
    ####################################################################################RADIOBUTTONS FOR DESTINATION
    Label(EntryForm, text="Choose Your Place").grid(row=0, column=0)
    Radiobutton(EntryForm, text="Army Public School", variable=VariableForDestination, value="Army Public School").grid(
        row=0, column=1)
    Radiobutton(EntryForm, text="Microsoft HQ", variable=VariableForDestination, value="Microsoft HQ").grid(row=0,
                                                                                                            column=2)
    Radiobutton(EntryForm, text="Sun And Sands Hotel", variable=VariableForDestination,
                value="Sun And Sands Hotel").grid(row=0, column=3)
    Radiobutton(EntryForm, text="Parkinson Hotel", variable=VariableForDestination, value="Parkinson Hotel").grid(row=0,
                                                                                                                  column=4)
    ListOfDestinations = ["Army Public School", "Microsoft HQ", "Parkinson Hotel", "Sun And Sands Hotel"]
    DestinationName = VariableForDestination.get()
    ####################################################################################RADIO BUTTONS FOR DESTINATION



    Label(EntryForm, text="Full Name**").grid(row=6)
    FullNameEntry = Entry(EntryForm)
    FullNameEntry.grid(row=6, column=1)

    Label(EntryForm, text="Car License Plate No.**").grid(row=7)
    CarLicensePlateNoEntry = Entry(EntryForm)
    CarLicensePlateNoEntry.grid(row=7, column=1)

    Label(EntryForm, text="E-mail Address**").grid(row=8)
    EmailAddressEntry = Entry(EntryForm)
    EmailAddressEntry.grid(row=8, column=1)

    Label(EntryForm, text="Phone Number**").grid(row=9)
    PhoneNumberEntry = Entry(EntryForm)
    PhoneNumberEntry.grid(row=9, column=1)

    Label(EntryForm, text="Enter Date (DD\MM\YY**").grid(row=10)
    DateEntry = Entry(EntryForm)
    DateEntry.grid(row=10, column=1)

    Label(EntryForm, text="Entry Time (Hours:Minutes)").grid(row=11)
    EntryTimeEntry = Entry(EntryForm)
    EntryTimeEntry.grid(row=11, column=1)

    Label(EntryForm, text="Exit Time(Hours:Minutes)").grid(row=13)
    ExitTimeEntry = Entry(EntryForm)
    ExitTimeEntry.grid(row=13, column=1)

    Label(EntryForm, text="No. Of Parking Spaces To Be Reserved**", activebackground="#33B5E5").grid(row=15)
    NoOfParkingSpaces = Entry(EntryForm)
    NoOfParkingSpaces.grid(row=15, column=1)

    BookedOrNotBooked = Label(EntryForm, text="Will Display If Space Is Available Or Not", relief="raised", fg="red",
                              bg="white")
    BookedOrNotBooked.grid(row=18)

    ##########################################################################Radiobuttons For Car Type
    Label(EntryForm, text="Choose Car Type").grid(row=17, column=0)
    Radiobutton(EntryForm, text="Sedan", variable=VariableForCars, value="Sedan").grid(row=17, column=1)
    Radiobutton(EntryForm, text="SUV", variable=VariableForCars, value="SUV").grid(row=17, column=2)
    Radiobutton(EntryForm, text="Van", variable=VariableForCars, value="Van").grid(row=17, column=3)
    ListOfCarTypes = ["Sedan", "SUV", "Van"]
    CarType = VariableForCars.get()
    ############################################################################Radiobuttons For Car Type

    EntryFormButton = canvas.create_window(1, 20, anchor='nw', window=EntryForm)

    ##########################################################
    """Quit Button On The Bottom Of The Screen"""
    ##########################################################
    from tkinter import messagebox
    def quit_window():
        result = messagebox.askquestion("Quit", "Are You Sure?(All Unsaved Form Data Will Be Lost)", icon='warning')
        if (result == 'yes'):
            FirstScreen.quit()

    quit_button = Button(FirstScreen, text="Quit", command=quit_window, anchor='w',
                         width=10, activebackground="#33B5E5")
    quit_button_window = canvas.create_window(650, 370, anchor='nw', window=quit_button)

    ###########################################################
    ##########################################################

    #######################################
    """Back End System Start"""
    ######################################

    #################################
    """STORAGE OF THE VALUES INPUTTED BY THE USER"""
    ###################################
    ############
    """FUNCTIONS FOR STORING THE NAMES AND VALUES"""

    ############

    def StoreFullName(event):
        global FullName
        FullName = FullNameEntry.get()


    def StoreCarLicensePlateNo(en):
        global CarLicensePlateNo
        CarLicensePlateNo = CarLicensePlateNoEntry.get()


    def StoreEmailAddress(en):
        global EmailAddress
        EmailAddress= EmailAddressEntry.get()

    def StorePhoneNumber(en):
        global PhoneNumber
        PhoneNumber = PhoneNumberEntry.get()

    def StoreDate(en):
        global Date
        Date = DateEntry.get()

    def StoreEntryTime(en):
        global EntryTime
        EntryTime = EntryTimeEntry.get()


    def StoreExitTime(en):
        global ExitTime
        ExitTime = ExitTimeEntry.get()

    def StoreNumberOfParkingSlots(en):
        global NumberOfParkingSlots
        NumberOfParkingSlots = NoOfParkingSpaces.get()
    # DestinationName=VariableForDestination.get()
    # CarType= VariableForCars.get()

    ##########################################################
    """Binding Entries To Functions With Press Of ENTER KEY"""
    ##########################################################

    FullNameEntry.bind('<Return>', StoreFullName)
    CarLicensePlateNoEntry.bind('<Return>', StoreCarLicensePlateNo)
    EmailAddressEntry.bind('<Return>', StoreEmailAddress)
    PhoneNumberEntry.bind('<Return>', StorePhoneNumber)
    DateEntry.bind('<Return>', StoreDate)
    EntryTimeEntry.bind('<Return>', StoreEntryTime)
    ExitTimeEntry.bind('<Return>', StoreExitTime)
    NoOfParkingSpaces.bind('<Return>', StoreNumberOfParkingSlots)

    #########################################################
    """INDEX OF PARKING SPACES"""
    #########################################################
    PlacesWithParkingSpaces = {
        "Army Public School": {"Sedan": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                          "Parking Slot4": 1, "Parking Slot5": 1},
                               "SUV": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                       "Parking Slot4": 1, "Parking Slot5": 1},
                               "Van": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                       "Parking Slot4": 1, "Parking Slot5": 1}},
        "Microsoft HQ": {"Sedan": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                    "Parking Slot4": 1, "Parking Slot5": 1},
                         "SUV": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                 "Parking Slot4": 1, "Parking Slot5": 1},
                         "Van": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                 "Parking Slot4": 1, "Parking Slot5": 1}},
        "Sun And Sands Hotel": {"Sedan": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                           "Parking Slot4": 1, "Parking Slot5": 1},
                                "SUV": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                        "Parking Slot4": 1, "Parking Slot5": 1},
                                "Van": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                        "Parking Slot4": 1, "Parking Slot5": 1}},
        "Parkinson Hotel": {"Sedan": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                       "Parking Slot4": 1, "Parking Slot5": 1},
                            "SUV": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                    "Parking Slot4": 1, "Parking Slot5": 1},
                            "Van": {"Parking Slot1": 1, "Parking Slot2": 1, "Parking Slot3": 1, \
                                    "Parking Slot4": 1, "Parking Slot5": 1}}}

    ########################################################
    """LOOPING AND STORING FOR RECEIPT"""
    #########################################################
    """ Variables For Reference And QuickView"""
    """"""
    ParkingPlaceInfo= "0"
    YesAvailable = "NO"

    def SearchingForSpace():

        DestinationName = VariableForDestination.get()
        CarType = VariableForCars.get()
        for i in PlacesWithParkingSpaces:
            if (DestinationName == i):
                for j in PlacesWithParkingSpaces[i]:
                    if (CarType == j):
                        for k in PlacesWithParkingSpaces[i][j]:
                            if PlacesWithParkingSpaces[i][j][k] == 1:
                                BookedOrNotBooked.config(text="Yes! Place Is Available")
                                global YesAvailable
                                YesAvailable="YES"
                                break
                            else:
                                BookedOrNotBooked.config(text="Pre-Booked.Choose Another Destination\Car Make")
                                
                                NotAvailable = "NO"

    def FinallyReservingParkingBySubmitButton():
        global YesAvailable
        if ((YesAvailable == "YES") and (len(str(FullNameEntry.get())) > 3) and (
        len(str(CarLicensePlateNoEntry.get())) > 3) and (len(str(EmailAddressEntry.get())) > 3) and (
        len(str(PhoneNumberEntry.get())) > 3) and (len(str(DateEntry.get())) > 3) and (len(str(NoOfParkingSpaces.get())) >= 1)):
            result = messagebox.askquestion("Book Now",
                                            "Are You Sure You Want To Book This?(Once Booked, It can not be cancelled)",
                                            icon='warning')
            if (result == "yes"):
                DestinationName = VariableForDestination.get()
                CarType = VariableForCars.get()
                for i in PlacesWithParkingSpaces:
                    if (DestinationName == i):
                        for j in PlacesWithParkingSpaces[i]:
                            if (CarType == j):
                                for k in PlacesWithParkingSpaces[i][j]:
                                    if PlacesWithParkingSpaces[i][j][k] == 1:
                                        PlacesWithParkingSpaces[i][j][k] = 0
                                        global ParkingPlaceInfo
                                        ParkingPlaceInfo = "Place: " + str(i) + "\n" +"Car Type: " + str(j) + "\n" +"Parking Slot Index: "+ str(k)
                ReceiptWindow=Toplevel()
                ReceiptWindow.title("Thank You For Booking! Here's Your Receipt! Enjoy!")
                """WILL GENERATE A WINDOW WITH RECIEPT OF THE PARKING"""
                ReceiptCanvas = Canvas(ReceiptWindow)
                ReceiptCanvas.pack()

                AudiForReceiptWindow = PhotoImage(file="Photos\AudiR8PNG.png")
                AudiForReceiptWindowPlacement = Label(ReceiptCanvas,image=AudiForReceiptWindow)
                AudiForReceiptWindowPlacement.pack(side=TOP, fill=BOTH)



                TextBoxForReceipt=Text(ReceiptWindow, height=20, width=40)
                TextBoxForReceipt.pack(side=TOP)
                TextBoxExtended= ("Entry Time: "+str(EntryTimeEntry.get())+"\n"+"Exit Time: "+str(ExitTimeEntry.get())+"\n"+"Date: "+str(DateEntry.get())+"\n"+ ParkingPlaceInfo)
                TextBoxForReceipt.insert(END, "Full Name: "+ str(FullNameEntry.get())+ "\n" + "Email Address: " + str(EmailAddressEntry.get()) + "\n" + "License Plate No.: " + str(CarLicensePlateNoEntry.get()) + "\n" +TextBoxExtended )
                ReceiptWindowIsCreatedHere=ReceiptCanvas.create_window(300, 50, anchor='nw', window=TextBoxForReceipt)


                ReceiptWindow.mainloop()


        else:
            result = messagebox.showinfo("Form Not Complete", "Fill Up The Fields To Book")


    ################################################################################
    """Submit Button"""

    SubmitButton = Button(EntryForm, text="Submit", width=10, command=FinallyReservingParkingBySubmitButton)
    SubmitButton.grid(row=20, column=4)
    #################################################################################

    #################################################################################
    "ENTRY BUTTON"

    Button(EntryForm, text="Check For Availability", command=SearchingForSpace).grid(row=21)
    #################################################################################

    ######################
    FirstScreen.mainloop()

##Photo Car##
PhotoCarRed = PhotoImage(file="Photos\Best-High-Resolution-Photos-For-Cars.png")
PlacementPhotoCarRed = Label(startscreen, image = PhotoCarRed)
PlacementPhotoCarRed.pack(side="top", fill=X )
###ToolBar on the bottom of the screen
toolbar= Frame(startscreen,bg="gray")
Button1 = Button(toolbar, text="Book A Parking Space Right Now!", relief = RAISED, command = YesWE)
Button1.pack(side="left", padx=10, pady=10)
toolbar.pack(side="bottom")

startscreen.mainloop()

