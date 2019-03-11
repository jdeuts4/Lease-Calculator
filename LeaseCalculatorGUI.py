
import Tkinter as tk
import tkMessageBox as mb

initialized = False
ab_called = True


def getValue():
    
    try:
        entry_enter_payment.delete(0,tk.END) 
        
        
        mFactor = float(entry_enter_mFactor.get())
        residual = float(entry_enter_residual.get())/100
        down = float(entry_enter_down.get())
        extra = float(entry_enter_extra.get())
        length = float(entry_enter_length.get())
        MSRP = float(entry_enter_price.get())
        tax = float(entry_enter_tax.get())/100
        discount = float(entry_enter_discount.get())
        discount_slider.set(discount)
        
        price_new = MSRP-discount
        loss_of_value = MSRP*residual
        depreciation = price_new - loss_of_value
        
        base_pay = (depreciation-down)/length
        
###     taxes = length*tax*((mFactor*(price_new+loss_of_value-down+extra)+base_pay+down)/(1-mFactor*tax*length))

        taxes = (tax*(mFactor*(price_new+loss_of_value-down+extra)*length+base_pay*length+extra+down))/(1-mFactor*length*tax)     
        
        mFactor_amount = (price_new+loss_of_value-down+extra+taxes)*mFactor
        
        simple_amount = base_pay + mFactor_amount + extra/length
        
        total_amount = simple_amount+taxes/length
        print 'real tax = ' , 36*(tax*(mFactor_amount+base_pay+extra/length+taxes/length))+tax*(down)
        

        
       
        entry_enter_payment.insert(0,total_amount)
    
    except:
        global initialized
        global ab_called        
        
        if initialized == True and ab_called == False:        
            #mb.showerror(message='Warning: Must enter all fields')
            mb.showerror(message='Warning: Must enter all fields')
            
            
        initialized = True
    
    finally:
        ab_called = False


    
    
    



root = tk.Tk() #create root node

frame = tk.Frame(root)

#create labels
money_factor_label = tk.Label(frame, text="Money Factor").grid(row=0,column=0) 
residual_label = tk.Label(frame, text="Residiual").grid(row=2,column=0) 
down_payment_label = tk.Label(frame, text="Down Payment").grid(row=4,column=0)
extra_fees_label =  tk.Label(frame, text="Extra Fees").grid(row=6,column=0)
lease_length_label = tk.Label(frame, text="Number of Months").grid(row=8,column=0)
price_car_label =  tk.Label(frame, text="Car Price").grid(row=0,column=1)
tax_rate_label = tk.Label(frame, text="Tax Rate").grid(row=2,column=1)
discount_label = tk.Label(frame, text="Discounts").grid(row=4,column=1)
payment_label = tk.Label(frame, text="Cost per month").grid(row=8,column=3)

discount_value_label = tk.Label(frame,text='Discount value').grid(row=6,column=1)




#                                 
#         
# create empy dictionaries to index variables
"""    
entry_enter_wihtdraw = {} 
entry_enter_deposit = {} 
entry_enter_balance = {} 
"""
# add field entry blank white bars
#create 10 fields    


entry_enter_mFactor = tk.Entry(frame)
entry_enter_residual = tk.Entry(frame)
entry_enter_down = tk.Entry(frame)
entry_enter_extra = tk.Entry(frame)
entry_enter_length = tk.Entry(frame)
entry_enter_price = tk.Entry(frame)
entry_enter_tax = tk.Entry(frame)
entry_enter_discount = tk.Entry(frame)
entry_enter_payment = tk.Entry(frame)


entry_enter_mFactor.grid(row=1,column=0)  
entry_enter_residual.grid(row=3,column=0)   
entry_enter_down.grid(row=5,column=0)    
entry_enter_extra.grid(row=7,column=0)   
entry_enter_length.grid(row=9,column=0)   
entry_enter_price.grid(row=1,column=1)  
entry_enter_tax.grid(row=3,column=1) 
entry_enter_discount.grid(row=7,column=1) 
entry_enter_payment.grid(row=9,column=3) 

def ab(event):
    
    entry_enter_payment.delete(0,tk.END)
    entry_enter_discount.delete(0,tk.END)
    entry_enter_discount.insert(0,discount_slider.get())
    global ab_called
    ab_called = True
    getValue()
 

discount_slider = tk.Scale(frame,from_=0, to=18000, orient='horizontal',command=ab)
discount_slider.grid(row=5,column=1)
discount_slider.set(100)

#callback function so when you press enter discount slider field
#updates
def ab2(event):
    
    discount_slider.set(entry_enter_discount.get())
 
#when you press 'Enter' it updates slider field with the typed discount
entry_enter_discount.bind('<Return>',ab2)


#discount_slider.pack()

#entry_enter_wihtdraw[str(i)].bind('<Return>',getValue)
frame.pack()    
    
tk.Button(text='Calculate', command=getValue).pack(side='left')

root.mainloop()
