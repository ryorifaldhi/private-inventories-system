from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Private Inventories System ')
root.iconbitmap('c:/ALPRO/TUBES/logo.ico')
root.geometry("1000x500")

# Database
data = []

def insertItem () :
    itemId = str(idEntry.get())
    itemName = str(itemEntry.get())
    itemPrice = str(priceEntry.get())
    itemQuantity = str(quantityEntry.get())
    dataEntry = []
    dataEntry.append(itemId)
    dataEntry.append(itemName)
    dataEntry.append(itemPrice)
    dataEntry.append(itemQuantity)
    data.append(dataEntry)
    refreshItem()
    idEntry.delete(0, 'end')
    itemEntry.delete(0, 'end')
    priceEntry.delete(0, 'end')
    quantityEntry.delete(0, 'end')

def refreshItem () :
    for i in my_tree.get_children() :
        my_tree.delete(i)  

    count = 0
    for key, record in enumerate(data): 
        if count % 2 == 0: 
            my_tree.insert(parent='', index='end', iid=key, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow'))
        else:
            my_tree.insert(parent='', index='end', iid=key, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow'))
        count += 1

def deleteItem () :
    selected_item = int(my_tree.focus())
    my_tree.delete(selected_item)
    data.remove(data[selected_item])
    refreshItem()

def deleteAll () :
    data.clear()
    refreshItem()
    my_tree.selection_clear()

def editItem () :
    selected_item = int(my_tree.focus()) #I001
    itemId = idEntry.get()
    itemName = itemEntry.get()
    itemPrice = priceEntry.get()
    itemQuantity = quantityEntry.get()
    dataEntry = []
    dataEntry.append(itemId)
    dataEntry.append(itemName)
    dataEntry.append(itemPrice)
    dataEntry.append(itemQuantity)

    #data["I001"] -> data[0]
    data[selected_item] = dataEntry
    
    idEntry.delete(0, 'end')
    itemEntry.delete(0, 'end')
    priceEntry.delete(0, 'end')
    quantityEntry.delete(0, 'end')
    refreshItem()
    my_tree.selection_clear()


def item_selected (self):
    idEntry.delete(0, 'end')
    itemEntry.delete(0, 'end')
    priceEntry.delete(0, 'end')
    quantityEntry.delete(0, 'end')

    selected_item = my_tree.focus()
    item = my_tree.item(selected_item,'values')

    if item != "" :
        idEntry.insert(0,item[0])
        itemEntry.insert(0,item[1])
        priceEntry.insert(0,item[2])
        quantityEntry.insert(0,item[3])


# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
my_tree.pack()

my_tree.bind('<<TreeviewSelect>>', item_selected)

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("ID", "Name", "Price", "Quantity")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Name", anchor=CENTER, width=140)
my_tree.column("Price", anchor=CENTER, width=140)
my_tree.column("Quantity", anchor=CENTER, width=140)


# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Name", text="Product Name", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

idLabel = Label(data_frame, text="ID")
idLabel.grid(row=0, column=0, padx=10, pady=10)
idEntry = Entry(data_frame)
idEntry.grid(row=0, column=1, padx=10, pady=10)

itemLabel = Label(data_frame, text="Product Name")
itemLabel.grid(row=0, column=2, padx=10, pady=10)
itemEntry = Entry(data_frame)
itemEntry.grid(row=0, column=3, padx=10, pady=10)

priceLabel = Label(data_frame, text="Price")
priceLabel.grid(row=0, column=4, padx=10, pady=10)
priceEntry = Entry(data_frame)
priceEntry.grid(row=0, column=5, padx=10, pady=10)

quantityLabel = Label(data_frame, text="Quantity")
quantityLabel.grid(row=0, column=6, padx=10, pady=10)
quantityEntry = Entry(data_frame)
quantityEntry.grid(row=0, column=7, padx=10, pady=10)


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

enterButton = Button(button_frame, text="Enter", command=insertItem)
enterButton.grid(row=0, column=0, padx=10, pady=10)

updateButton = Button(button_frame, text="Update Item", command=editItem)
updateButton.grid(row=0, column=1, padx=10, pady=10)

deleteItem = Button(button_frame, text="Delete Item", command=deleteItem)
deleteItem.grid(row=0, column=2, padx=10, pady=10)

deleteallButton = Button(button_frame, text="Delete All", command=deleteAll)
deleteallButton.grid(row=0, column=3, padx=10, pady=10)



root.mainloop()