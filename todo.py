import PySimpleGUI as sg


layout = [
    [sg.CalendarButton("Set Date",size=(20,2)),sg.T("_______________",key="-DATE-")],
		[sg.T("Enter Your Task:",font="Bold",size=(15,1)),sg.I(key="-TASK-",font="Futura",size=(35,1))],
		[sg.Table(values='',headings=["INDEX","DATE","TASK"],key="-TABLE-",size=(500,10),auto_size_columns=False,col_widths=[5,9,30],vertical_scroll_only=False,justification="l",font="None 15")],
		[sg.B("Add",button_color="green",size=(10,1)),sg.B("Delete", key="-DEL-",button_color="red",size=(10,1)),sg.Exit()],
		]
window = sg.Window("To DO List", layout)
tasks = []
counter = 1
while True:
	event, values = window.read()
	if event in ("Exit",sg.WIN_CLOSED):
		window.close()
		break
	elif event == "Add":
		date = window["-DATE-"].get().split()[0]
		task = [[counter,date,values["-TASK-"]]]
		tasks += task
		window["-TABLE-"].update(tasks)
		window["-TASK-"].update('')
		counter += 1
	elif event == "-DEL-":
		if values["-TABLE-"]:
			indx = values["-TABLE-"][0]
			del tasks[indx]
			window["-TABLE-"].update(tasks)


	print(event, values)
	
			
