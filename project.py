from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import requests

def data_get():
 city=city_name.get()
 if not city.strip():
  messagebox.showerror("Error", "Please enter a city name")
  return
 
 try:
  
  response = requests.get(
   "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197",
   timeout=5
  )

  if response.status_code != 200:
   messagebox.showerror("Error", f"City not found or API error. Status code: {response.status_code}")
   return
  
  data = response.json()

  if "weather" not in data or "main" not in data:
   messagebox.showerror("Error", "Invalid response from API")
   return
  
  w_label1.config(text=data["weather"][0]["main"])
  wb_label1.config(text=data["weather"][0]["description"])
  temperature_c = int(data["main"]["temp"] - 273.15)
  temp_label1.config(text=f"{temperature_c} °C")
  pressure_hpa = data["main"]["pressure"]
  per_label1.config(text=f"{pressure_hpa} hPa")
  
 except requests.exceptions.Timeout:
  messagebox.showerror("Error", "Request timed out. Please try again.")
 except requests.exceptions.ConnectionError:
  messagebox.showerror("Error", "No internet connection or API server is down.")
 except requests.exceptions.RequestException as e:
  messagebox.showerror("Error", f"Request failed: {str(e)}")
 except (KeyError, IndexError, ValueError) as e:
  messagebox.showerror("Error", f"Error parsing response data: {str(e)}")
 except Exception as e:
  messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


win=Tk()
win.title("wscube tech")
win.config(bg="blue")
win.geometry("500x570")
name_label=Label(win,text="wscube weather app",font=("time New roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="wscube weather app",values=list_name,font=("time new roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="weather climates",font=("time new roman",15))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=("time new roman",20))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label=Label(win,text="weather description",font=("time new roman",15))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1=Label(win,text="",font=("time new roman",15))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text="Temperature",font=("time new roman",15))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("time new roman",15))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label=Label(win,text="Pressure",font=("time new roman",15))
per_label.place(x=25,y=470,height=50,width=210)
per_label1=Label(win,text="",font=("time new roman",15))
per_label1.place(x=250,y=470,height=50,width=210)
done_button=Button(win,text="done",font=("time new roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()