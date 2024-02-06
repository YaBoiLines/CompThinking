
def total_sales():
    days = ['Monday','Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']
    sales = []


    for day in days:
        sale_amount = float(input(f'Enter sale for {day}: $'))
        
    total_sale = sum(sales)
    print(f'\nTotal sales for the week: {total_sale:.2f}')
    
def main():
    total_sales()
    
if __name__ == '__main__':
    main()
    

